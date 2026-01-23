import speech_recognition as sr
import pyttsx3
from googletrans import Traslators #Google Translate API

#Initialize text to speech engine
def speak (text,language='en')
    engine=pyttsx3.init()
    engine.setProperty('rate',150) #Speed of Speech

    voices=engine.getProperty('voices')

#Set voices for English or other languages if supported by pyttsx3
if language=="en":
    engine.setProperty('voice',voices[0].id) #Default English Voice

else:
    engine.setProperty('voice',voices[1].id) #Fallback to another voice if available


    engine.say(text)
    engine.runAndWait()

    #Speech to Text Recognize Spoken Language (English)
    def speech_to_text():
        recognizer=sr.Recognizer()
        with sr.Microphone() as source:
            print("Please Speak Now In English...")
            audio=recognizer.listen(source)

            try:

                print("Recognizing speech...")

                text=recognizer.recognize_google(audio,language='en-US') #Use English for speech recognition
                print(f"You said: {text}")

                return text
            except.sr.UnknownValueError:
                print("Sorry, Could not understand the audio")

            except sr.RequestError as e:
                print(f"API Error:{e}")


    #Translate Text Using Google Translate AI
    def translate_text(text,forget_language='es'): #Default Target Language is Spanish(es)
        
        translator=Traslators()
        translation=translator.translate(text,dest=target_Language)
        print(f"Translated Text:{translation.text}")

        return translation.text
