# main.py {Streamlit} - shorter version
# Switch provider by changing the import line:
import io

from hf import generate_response
# from groq import generate_response
import streamlit as st

SYSTEM_PROMPT = """You are a Math Mastermind. For every math problem:
1) Show step by step solution 2) Explain reasoning 3)Give alternate method if possible:
4) Verify answer if possible 5) Use proper notation 6) Break complex problems into parts
format: Problem -> Steps -> **Final Answer** -> Concepts used.Be precise and educational."""

def main_generate(problem: str,level: str , temperature=0.1, max_tokens: 1024) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nMath Problem ({level}): {problem}"
    return generate_response(prompt, temperature=temperature, max_tokens=max_tokens)

def export_txt(history):
    txt = "n\n".join([f"Q{i}: {h['a']} for i, h in enumrate(history, 1)])])"])
    return io.BytesIO(txt.encode("utf-8"))

def setup_ui():
    st.set_page_config(page_title="Math Mastermind", layout="centered")
    st.title("Math Mastermind")
    st.write("Solve any math problem with detailed step by step explanations.")

    with st.expander("Examples"):
        st.markdown(
            '- Alegra: "Solve 2x2 + 5X'
        )
