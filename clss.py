import streamlit as st

# 1. Custom Title


st.set_page_config(page_title="📊 Math Genie", layout="centered")
st.title("📊 Math Genie")

# 2. Example Problem Customization


with st.expander("🧠 My Example Problems"):
    st.markdown("""
    **Probability:** Tossing coins, rolling dice
    - Example: "What's the probability of getting heads twice in 3 coin tosses?"
    
    **Algebra:** Word problems and equations
    - Example: "A number increased by 5 is 12. What’s the number?"
    """)


# 3. Updated Difficulty


level = st.selectbox("Choose your level", ["Beginner", "Regular", "Challenging"], index=1)

# 4. Custom Prompt


system_prompt = """You are a Math Wizard built by Aanya – always precise, patient, and full of clarity.
For every math problem:
1. Show detailed steps
2. Explain the method
3. Highlight the final answer"""

# 5. Optional: Change styles in CSS


# (Change background, font colors in `.history-box` or `.answer`)



