import os
import requests
import pyttsx3
import speech_recognition as sr
import pyautogui
import webbrowser
from googletrans import Translator

# ✅ CONFIGURE HERE
DEEPSEEK_API_KEY = 'sk-5af561abba0a4ff184f50072380801ef'
LANGUAGES = ['en', 'hi', 'zh-cn', 'ru', 'ja', 'es']

# 📢 Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# 🎙 Speech-to-text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except:
        speak("Sorry, I didn't catch that.")
        return ""

# 🌍 Translate user query to English
translator = Translator()
def translate_to_english(text):
    translated = translator.translate(text, dest='en')
    return translated.text

# 🧠 Get DeepSeek response
def deepseek_ask(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Sorry, I couldn't get a response."

# 🧠 Jarvis Logic
def jarvis(query):
    query = translate_to_english(query).lower()

    if "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "type" in query:
        text = query.replace("type", "")
        pyautogui.typewrite(text)
        speak("Typed it for you")
    elif "weather" in query:
        speak("Here is the weather information:")
        weather_response = deepseek_ask("Give me current weather in my location")
        speak(weather_response)
    else:
        speak("Let me think...")
        reply = deepseek_ask(query)
        speak(reply)

# 🔁 Main loop
if __name__ == "__main__":
    speak("Hello! I am Jarvis. How can I help you?")
    while True:
        command = listen()
        if any(x in command.lower() for x in ["exit", "stop", "bye"]):
            speak("Goodbye!")
            break
        elif command.strip() == "":
            continue
        else:
            jarvis(command)