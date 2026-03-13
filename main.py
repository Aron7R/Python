from doctest import Example

from groq import generate_response


def run_activity():
    print("ZERO-SHOT, ONE-SHOT AND FEW-SHOT LEARNING ACTIVITY")

    category = input("Enter a category (e.g., 'animals', 'countries', 'fruits'): ")
    item = input(f"Enter a specific {category} to classify: ").strip()

    if not category or not item:
        print("Error: Both category and item must be provided.")
        return
    
    # Zero-Shot example
    zero_shot = f"Is {item} a {category}? Answer with 'yes' or 'no'."
    print("\nZero-Shot Learning:")
    print(f"Response: {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")

    # One-Shot example
    one_shot = f"""Example:

    Category: animals
    Item: dog
    Answer: yes,dog is an animal.

    Now you try:
    Category: {category}
    Item: {item}
    Answer:"""
    print("\nOne-Shot Learning:")
    print(f"Response: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")

    # Few-Shot example
    few_shot = f"""Examples 1:

    Category: animals
    Item: dog
    Answer: yes,dog is an animal.

    Now you try:
    Category: {category}
    Item: {item}
    Answer:"""
    print("\nFew-Shot Learning:")
    print(f"Response: {generate_response(few_shot, temperature=0.3, max_tokens=1024)}")

    creative_prompt = f"""Example 1 : Word: moon

Story: The moon winked at the lovers as they shared their first kiss.

Word: {item}

Story:"""
    print("\n--- CREATIVE FEW-SHOT LEARNING ---")
    print(f"Response: {generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}")

    #Reflection Questions
    print("\n--- REFLECTION QUESTIONS ---")
    print("1. How did the model's responses differ between zero-shot, one-shot, and few-shot prompts?")
    print("2. Did the model understand the category and item correctly in each case?")  
    print("3. How did the creative few-shot prompt influence the model's response compared to the more structured prompts?")

if __name__ == "__main__":
    run_activity()


    