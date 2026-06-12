import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
from openai import OpenAI
from gtts import gTTS         
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your_newsapi_key_here"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)            
    tts.save('temp.mp3')

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def aiProcess(command):
    client = OpenAI(
        api_key="your_openai_key_here"
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in music_library.music:
            link = music_library.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have {song} in the music library")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
        else:
            speak("Sorry, couldn't fetch the news right now.")
    else:
        # Let OpenAI handle everything else
        output = aiProcess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
             
                audio = r.listen(source, timeout=2, phrase_time_limit=5)

            word = r.recognize_google(audio)

           
            if word.lower() == "jarvis":
                speak("Yeah")

                
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                processcommand(command)

        except Exception as e:
            print("Error: {0}".format(e))
