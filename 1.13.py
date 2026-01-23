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