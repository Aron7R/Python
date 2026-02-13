import speech_recognition as sr
import pyttsx3
from googletrans import Translator
def speak(text,language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    if language == "en":
        engine.setProperty('voice',voices[0].id)
    else:
        engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait() 
def speech_to_text(language="en"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now in English...")
        audio = recognizer.listen(source)
try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio, language=language)
    print(f"You said: {text}")
    return text
except sr.UnknownValueError:
    print("Sorry, Could not understand the audio.")
except sr.RequestError as e:
    print(f"API Error: {e}")
    return ""
def translate_text(text, dest_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text
def display_language_options():
    print("Select Language:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
choice = input("Enter your choice (1-8): ")
language_map = {
    "1": "hi",
    "2": "ta",
    "3": "te",
    "4": "bn",
    "5": "mr",
    "6": "gu",
    "7": "ml",
    "8": "pa"
}
return language_dict.get(choice, "es")
def main():
    target_language = display_language_options()
    original_text = speech_to_text(language=target_language)
    if original_text:
        translated_text = translate_text(original_text,
                                         target_language=target_language)
        speak(translated_text,language="en")
        print("Translation Spoken out!")
if __name__ == "__main__":    main()