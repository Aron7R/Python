import config
from openai import OpenAI


GROQ_URL = "https://api.groq.com/openai/v1"
MODELS = getattr(config, "GROQ_MODELS", ["11ama-3.1-8b-instant", "mixtral-8x7b-32768"])

def generate_response(prompt:str,temperature:float=0.3, max_tokens:int=512) -> str:
    key = getattr(config, "GROQ_API_KEY", None)
    if not key:
        return "Error: GROQ_API_KEY not found in config."
    client = OpenAI(api_key=key, base_url=GROQ_URL)

    last_error = None
    for m in MODELS:

        try:
            r = c.chat.completions.create(
                model=m,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return r.choices[0].message.content
        except Exception as e:
            last_error = e
    return (
        "Groq model failed,\n"
        f"tried models: {MODELS}\n"
        "Fix:\n"
        "1)Switch to hf by importing hf by importing hf.py in main.py 0R\n"
        "2)Replace Groq model in groq.py (GROQ_MODELS).\n"
        f"Details: {type(last_error).__name__}: {last_error}"















    )