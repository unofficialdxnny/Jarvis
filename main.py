import speech_recognition as sr
from gtts import gTTS
import os
import pygame


# Initialize the recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        return audio

def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()


def main():
    while True:
        try:
            audio = listen()
            query = recognizer.recognize_google(audio)
            print("You said: " + query)
            # Add your logic for processing the query here
            response = "I heard you say: " + query
            speak(response)


        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Sorry, I encountered an error: {str(e)}")

if __name__ == "__main__":
    main()

os.remove("response.mp3")
