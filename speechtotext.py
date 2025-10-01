from tkinter import *
import speech_recognition as sr
from tkinter import messagebox
from tkinter.filedialog import *
root=Tk()
root.title("Speech to Text")
Label(root, text="Voice notepad").place(x=200, y=50)
Start = Button(root, text="").place(x=200, y=300)

root.mainloop()