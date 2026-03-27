#Change groq --> hf to use hugging face API
#Change hf --> groq to use groq API
from groq import generate_response as groq_generate_response
#from groq import generate_response

def reinforcement_learning_activity():
    print("\n== Reinforcement Learning Activity ==\n")
    prompt = input("Enter a prompt for the AI model (e.g., 'Describe the icon'):").strip()
    if not prompt:
        print("Please enter a prompt to learn the activity.")
        return
    
    initial_response = groq_generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response:\n{initial_response}\n")

    # Rating + feedback loop
    try:
        rating = int(input("Rate the response on a scale of 1 (bad) to 5 (good): ").strip())
        if rating < 1 or rating > 5:
            print("Invalid rating. Using 3.")
            rating = 3
            return
    except ValueError:
        print("Invalid input. Using 3.")
        rating = 3
        return
    
    feedback = input("Provide feedback to improve the response: ").strip()
    improved_response = f"{initial_response} (improved based on feedback: {feedback})"
    print(f"\nImproved AI Response:\n{improved_response}\n")
    
    print("\nReflection:")
    print("1) How did the initial response meet your expectations?")
    print("2) How did your feedback influence the improved response?")
    
    def role_based_prompt_activity():
        print("\n== Role-Based Prompt Activity ==\n")
        category = input("Enter a category (e.g , science,history,math): ").strip()
        item = input(f"Enter an specific {category} topic (e.g., 'photosynthesis' for science): ").strip()
    
        if not category or not item:
            print("Please enter both category and item to learn the activity.")
            return
        
        teacher_prompt = f"Act as a teacher and explain {item} in simple terms."
        expert_prompt = f"Act as an expert and provide a detailed explanation of {item}."
    
        teacher_response = groq_generate_response(teacher_prompt, temperature=0.3, max_tokens=1024)
        expert_response = groq_generate_response(expert_prompt, temperature=0.3, max_tokens=1024)
    
        print(f"\nTeacher Response:\n{teacher_response}\n")
        print(f"\nExpert Response:\n{expert_response}\n")
    
        print("\nReflection:")
        print("1) How did the teacher response differ from the expert response?")
        print("2) Which response did you find more helpful and why?")
    
    def run_activity():
        print("\n== AI Prompting Activities ==\n")
        print("Choose an activity:")
        print("1. Reinforcement Learning")
        print("2. Role-Based Prompting")
        choice = input(">").strip()

        if choice == "1":
            reinforcement_learning_activity()
        elif choice == "2":
            role_based_prompt_activity()    
        else:
            print("Invalid choice. Please select 1 or 2.")
    if __name__ == "__main__":
    run_activity()  