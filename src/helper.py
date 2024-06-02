"""This module will store all the function that is needed for project"""

import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


def voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        audio = recognizer.listen(source)

    try:        
        text = recognizer.recognize_google(audio)
        print("The audio try to conveys: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, failed to interpret you voice")
    except sr.RequestError as error:
        print("Could not request result from google speech recognition service: {0}".format(error))


def llm_model_object(user_text):
    
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_text)
    result = response.text
    
    return result


def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3")