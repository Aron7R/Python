#Change groq --> hf to use hugging face API
#Change hf --> groq to use groq API
from groq import generate_response
#from groq import generate_response

def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    prompt = input("Enter a prompt to analyze for bias: "(e.g, "Describe a doctor.")).strip()
    if not prompt:
        print("Error: Prompt cannot be empty.")
        return
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print("\nInitial Response:\n", initial_response)

    modified_prompt = input(
        "Modify the prompt to mitigate bias (e.g., 'Describe the qualities of a doctor'): "
    ).strip()
    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nModified AI Response (Neutral): \n{modified_response}")
    else:
        print("No modifications made to the prompt. Bias mitigation activity skipped.")

    def token_limit_activity():
        print("\n=== TOKEN LIMIT ACTIVITY ===\n")
        long_prompt = input("Enter a long prompt (more than 300 words, e.g., a detailed story or description): " \
        "").strip()

        if not long_prompt:
            long_response = generate_response(long_prompt, temperature=0.3, max_tokens=512)
            preview = long_response[:500] + "..." if len(long_response) > 500 else long_response
            print(f"\nResponse to Long Prompt: {preview}")
        else:
            print("No long prompt entered. Skipping long prompt response.")

            shprt_prompt = input("Enter a short prompt (less than 10 words, e.g., 'What is AI?'): ").strip()
            if not shprt_prompt:
                short_response = generate_response(shprt_prompt, temperature=0.3, max_tokens=512)
                print(f"\nResponse to Short Prompt: {short_response}")
            else:
                print("No short prompt entered. Skipping short prompt response.")

                def run_activity():
                    print("\n=== AI Learning Activity ===")
                    print("Choose an activity:")
                    print("1. Bias Mitigation")
                    print("2. Token Limit")
                    choice = input("Enter your choice (1 or 2): ").strip()
                    if choice == "1":
                        bias_mitigation_activity()
                    elif choice == "2":
                        token_limit_activity()
                    else:
                        print("Invalid choice. Please select 1 or 2.")

                        if __name__ == "__main__":
                            run_activity()