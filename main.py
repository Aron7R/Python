# Switch provider by changing the import line:
from hf import generate_response
# from groq import generate_response

import io
import streamlit as st

CSS = """
<style>
.history-wrap {max-height: 420px; overflow-y: auto; padding-right: 6px;}
.qa-card{
border: 1px solid #e6e6e6;
background: #ffffff;
border-radius: 10px;
padding: 14px 16px;
margin: 10px 0;
box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
}
.q{font-weight: 700; color: #0a6ebd; margin-bottom: 8px;}
.a{white-space: pre-wrap; color: #333; line-height: 1.5;}
</style>
"""
def export_bytes(history):
    text = "".join([f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n" for i, h in enumerate(history, 1)])
    return io.BytesIO(text.encode("utf-8"))

def setup_ui():
    st.set_page_config(page_title="AI Teaching Assistant", layout="centered")
    st.title("AI Teaching Assistant")
    st.write("Ask any question and get an answer from the AI model. You can also export the Q&A history as a text file.")
    st.session_state.setdefault("history", [])

    col_clear, col_export = st.columns([1, 2])
    with col_clear:
        if st.button("Clear Conversation"):
        st.session_state.history = []
        st.rerun()
    with col_export:
        if st.button("Export History"):
            if st.session_state.history:
                st.download_button(
                    label="Download Q&A History",
                    data=export_bytes(st.session_state.history),
                    file_name="qa_history.txt",
                    mime="text/plain"
                )

user input = st.text_input("Your Question:", key="input")
if st.button("Ask"):
    q = st.button("Ask")
    if q:
        with st.spinner("Generating answer..."):
            a = generate_response(q, temperature=0.3)
            st.session_state.history.insert(0, {"question": q, "answer": a})
            st.rerun()
    else:
        st.warning("Please enter a question before asking.")

        st.markdown("### Conversation History")
        st.markdown(CSS, unsafe_allow_html=True)

        cards = []
        for i, h in enumerate(st.session_state.history, 1):
            cards.append(f'<div class="qa-card"><div class="q">Q{i}: {h["question"]}</div><div class="a">A{i}: {h["answer"]}</div></div>')
            st.markdown('<div class="history-wrap">' + "".join(cards) + '</div>', unsafe_allow_html=True)

            def main():
                setup_ui()
            if __name__ == "__main__":
                main()
    