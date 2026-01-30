from gtts import gTTS
import os

# Ask name
tts = gTTS(text="What is your name?", lang="en")
tts.save("ask.mp3")
os.system("start ask.mp3")  # Windows

name = input("What is your name? : ")

# Greet user
greeting = f"Hello {name}, how are you?"
tts2 = gTTS(text=greeting, lang="en")
tts2.save("greet.mp3")
os.system("start greet.mp3")  # Windows
