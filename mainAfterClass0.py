# main.py
# Type groq to use Groq OR type hf to use Hugging Face:
from groq import generate_response
# from hf import generate_response

def prompt_engineering_activity():
    print("Welcome to the AI Prompt Engineering Tutorial!")

    vague_prompt = input("Enter a vague prompt: ")
    print("\nAI's response to vague prompt:")
    print(generate_response(vague_prompt))

    specific_prompt = input("\nNow, make it more specific: ")
    print("\nAI's response to specific prompt:")
    print(generate_response(specific_prompt))

    contextual_prompt = input("\nNow, add context to your specific prompt: ")
    print("\nAI's response to contextual prompt:")
    print(generate_response(contextual_prompt))

    print("\n--- Reflection ---")
    print("1. How did the AI's response change when the prompt was made more specific?")
    print("2. How did the AI's response improve with the added context?")
    print("3. Which prompt produced the most relevant and tailored response? Why?")

if __name__ == "__main__":
    prompt_engineering_activity()
