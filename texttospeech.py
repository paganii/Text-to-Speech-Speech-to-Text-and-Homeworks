from tkinter import *
from gtts import gTTS
import os

# root=Tk()
# root.title="Text to Speech"
# root.geometry("690x500")
# root.config(background="lightblue")

text = input("Type something...")
audio = gTTS(text, lang = "en")
audio.save("Output.mp3")
os.system("Output.mp3")

# root.mainloop()