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
    txt = "\n\n".join([f"Q{i}: {h['q']}\nA{i}: {h['a']}" for i, h in enumerate(history, 1)])
    return io.BytesIO(txt.encode("utf-8"))

def setup_ui():
    st.set_page_config(page_title="Math Mastermind", layout="centered")
    st.title("Math Mastermind")
    st.write("Solve any math problem with detailed step by step explanations.")

    with st.expander("Examples"):
        st.markdown(
            '- Alegra: "Solve 2x2 + 5X - 3 = 0"\n'
            '- Calculus: "Derivative of sin(x2) + In(x)"\n'
            '- Geometry: "Area of a triangle (0,0), (3,4), (6,0)"\n'
            '- Probability: "P(sum=7 with two dies)"'
        )

        st.session_state.setdefault("history", [])
        st.session_state.setdefault("k", 0)

        c1,c2 = st.columns([1,2])
        if c1.button("Clear"):
            st.session_state.history = []; st.rerun()
            if st.session_state.history:
                c2.download_button("Export", export_txt(st.session_state.histooory),
                                   "Math_Mastermind_Solutions.txt, "text/plain")
                        
        with st.form("math_form", clear_on_submit=True):
            problem = st.text_area("Enter your math problem here:", height=100,placeholder="Example: Solve 2x2 + 5X - 6 = 0", key=f"q_{st.session_state.k}")
            a,b = st.columns([3,1])
            solve = a.form_submit_button("Solve", use_container_width=True)
            level = b.selectbox("Level", ["Basic", "Intermediate", "Advanced"], index=1)

            if solve:
            if not q.strip(): st.warning("Enter a problem first.")
            else:
                with st.spinner("Solving..."):
                    ans = math_generate(q.strip(), level)
                    ans = math_generate(q.strip(), level)
                    st.session_state.history.insert(0, {"q": q.strip(), "a": ans, "lvl": level})
                    st.session_state.k += 1; st.rerun()

                    if not st.session_state.history: return
                    st.markdown('### Solution History (Latest First)')
                    st.markdown("""<style>
                    .box { max-height: 500px; overflow-y: auto; border: 2px solid #4CAF50; padding: 12px; background: #f7fbff; border-radius: 10px; }
                    .q{font wight: 700; color;#2E7D32;margin-top:12px}
                    .lvl{display:inline-block;background:#FF9800;color:#fff;
                    padding:2px 8px;radius:5px;font-size:12px;font-size:12px;margin-left:8px}
                    .a{margin-space:pre-wrap;color:#185E20;background:#fff:padding:10px;border-radius:8px:borderleft:4px solid #4CAF50;margin:6px 0 14px}
                    </style>""", unsafe_allow_html=True)

                    html = '<div class="box">'
                    for i, h in emumerate(st.session_state.history, 1):
                        html += f'<div class="q">Q{i}: {h["q"]} <span class="lvl">{h["lvl"]}</span></div>'
                        html += f'<div class="a">{h["a"]}</div>'
                    st.markdown(html + "</div>", unsafe_allow_html=True)
if __name__ == "__main__":
    setup_ui()