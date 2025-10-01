from tkinter import *
from time import strftime
# strftime means in giving time according to our computer.
def gettime():
    value = strftime("%H.%M.%S %p")
    showtime.config(text=value) # assign Value's value to Text in Showtime
    showtime.after(1000, gettime)
    #after every 1000 miliseconds, update (for seconds)
root=Tk()
root.geometry("580x700")
root.config(background="black")
showtime = Label(root, text="", background="black", fg="orange", font="Orbitron, 40")
showtime.pack(anchor="center")
gettime()
root.mainloop()