from io import BytesIO
try:
    import requests
except Exception:
    # Fallback minimal requests-like wrapper using urllib if requests not available
    import json
    from urllib import request as _request
    from urllib.error import URLError, HTTPError

    class _SimpleResponse:
        def __init__(self, status_code, content):
            self.status_code = status_code
            self._content = content
        def raise_for_status(self):
            if not (200 <= self.status_code < 300):
                raise HTTPError(None, self.status_code, 'HTTP Error', hdrs=None, fp=None)
        def json(self):
            return json.loads(self._content.decode('utf-8'))

    class _RequestsFallback:
        @staticmethod
        def post(url, json=None, timeout=None):
            data = None
            headers = {'Content-Type': 'application/json'}
            if json is not None:
                data = bytes(__import__('json').dumps(json), 'utf-8')
            req = _request.Request(url, data=data, headers=headers, method='POST')
            try:
                with _request.urlopen(req, timeout=timeout) as resp:
                    content = resp.read()
                    return _SimpleResponse(resp.getcode(), content)
            except HTTPError as e:
                return _SimpleResponse(e.code if hasattr(e, 'code') else 500, e.read() if hasattr(e, 'read') else b'')
            except URLError as e:
                raise

    requests = _RequestsFallback()
import streamlit as st
from huggingface_hub import InferenceClient

import config
MODEL_ID = "stabilityai/stable-diffusion-3-medium-diffusers"
FILTER_API_URL= "https://filters-zeta.vercel.app/api/filter"

ENCHANCE_SYS = (
    "Improve prompts for text to image , Return ONLY the enchanced prompt."
    "Add subjects, style, lighting, camera angle, background, colours. Keep it safe."
)

#This is only for image quality quidance, not safety filtering
NEGATIVE = "low quality,blurry,distorted,watermark,text.cropped"

img_client = InferenceClient(provider="hf-inference",api_key=config.HF_API_KEY, model=MODEL_ID)

def check_prompt_with_filter_api(prompt:str):
    try:
        response = requests.post(
            FILTER_API_URL,
            json={"input": prompt},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict):
            return {"ok": False, "reason": "Invalid filter API response"}

        return data
    except Exception as e:
        return {
            "ok": False,
            "reason": f"Filter API error: {str(e)}"
        }

def enchance_prompt(raw: str) -> str:
    from hf import generate_response

    out = generate_response(
        f"{ENCHANCE_SYS}\nUser prompt: {raw}",
        temperature=0.4,
        max_tokens=220,
    )
    return out.strip()


def gen_image(prompt:str):
    filter_result = check_prompt_with_filter_api(prompt)
    if not filter_result.get("ok"):
        return None, f"Prompt failed safety filter: {filter_result.get('reason','Unsafe prompt')}"
    
    try:
        return img_client.text_to_image(
            prompt=prompt,
            negative_prompt=NEGATIVE,
            model=MODEL_ID,
        ), None
    
    except Exception as e:
        msg =  str(e)

        if "negative_prompt" in msg or "unexpected keyword" in msg:
            try:
                return img_client.text_to_image(
                    prompt=prompt,
                    model=MODEL_ID,
                ), None
            except Exception as e2:
                msg = str(e2)

        if any(x in msg for x in ["402", "Payment Required", "pre-paid credits"]):
            return None, "Image backend requires credits or model not available on hf-inference.\n\nRaw: " + msg

        if "404" in msg or "Not found" in msg:
            return None, "Model not served on this provider route (hf-inference),\n\nRaw: " + msg

        return None, "Image generation failed: " + msg


def main():
    st.set_page_config(page_title="AI Image Generator", layout="centered")
    st.title("Safe AI image generator")
    st.info("Flow: Enter a prompt -> check if using t6he deployed safety API -> generate the image.")

    with st.form("prompt_form"):
        raw = st.text_area(
            "Image Description,",
            height=120,
            placeholder="Example: A cozy cabin in snowy mountain at sunrise, climate lighting"
        )
        submit = st.form_submit_button("Generate Image")

    if submit:
        raw = raw.strip()
        if not raw:
            st.warning("Please enter a prompt.")
            return
        
        raw_check = check_prompt_with_filter_api(raw)
        if not raw_check.get("ok"):
            st.error(f"Prompt failed safety filter: {raw_check.get('reason','Unsafe prompt')}")
            return
        with st.spinner("Enchancing prompt..."):
            final_prompt = enchance_prompt(raw)

        enchanced_check = check_prompt_with_filter_api(final_prompt)
        if not enchanced_check.get("ok"):
            st.error(f"Enchanced prompt failed safety filter: {enchanced_check.get('reason','Unsafe prompt')}")
            return
        
        st.markdown("#### Enchanced Prompt:")
        st.code(final_prompt)

        with st.spinner("Generating image..."):
            img, err = gen_image(final_prompt)
            if err:
                st.error(err)
                return
            
        st.image(img, caption="Generated Image", use_column_width=True)
        st.session_state.generated_image = img

        img = st.session_state.get("generated_image")
        if img:
            buf = BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button(
                "Download Image",
                byte_im,
                "ai_generated_image.png",
                "image/png"
            )


if __name__ == "__main__":
    main()


