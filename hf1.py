import config
from huggingface_hub import InferenceClient

MODELS = getattr(
    config,
    "HF_MODELS",
    ["meta-llama-3.1-8b-instruct"],

)

def generate_response(prompt:str,temperature:float=0.3, max_tokens:int=512) -> str:
    key = getattr(config, "HF_API_KEY", None)
    if not key:
        return "Error: HF_API_KEY not found in config."
    client = InferenceClient(token=key)

    last_error = None
    for m in MODELS:
        try:
           c = InferenceClient(model=m, token=key)
           r = c.chat_completion(
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return r.choices[0].message.content 
        
        except Exception as e:
            last_error = e

    return (
       "Hugging Face model failed,\n"
       f"tried models: {MODELS}\n"
       "Fix:\n"
       "1)Switch to groq by importing groq by importing groq.py in main.py 0R\n"
       "2)Replace Hugging Face model in hf.py (HF_MODELS).\n"
       f"Details: {type(last_error).__name__}: {last_error}"
    )
