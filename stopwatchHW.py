from tkinter import *
import time
from tkinter import messagebox

root = Tk()
root.title("Clockk")
root.geometry("400x320")
hours = StringVar()
minutes = StringVar()
seconds = StringVar()
hours.set("00")
minutes.set("00")
seconds.set("00")
def submit():
    try:
        temp = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    except:
        print("Please input the suitable value.")
    while temp > -1:
        minute,second = divmod(temp, 60)
        hour = 00
        if minute > 60:
            hour, minute=divmod(minute, 60)
        # hours.set("{00:2d}".format(hour))
        hours.set(f"{hour:02d}")
        #minutes.set("{00:2d}".format(minute))
        minutes.set(f"{minute:02d}")
        #seconds.set("{00:2d}".format(second))
        seconds.set(f"{second:02d}")
        
        root.update()
        time.sleep(1)
        if temp == 00:
            messagebox.showinfo("Countdown", "Alarm!!")
        temp = temp-1

hourentry = Entry(root, w=3, font=20, textvariable=hours)
hourentry.place(x=80, y=160)
minutesentry = Entry(root, w=3, font=20, textvariable=minutes)
minutesentry.place(x=130, y=160)
secondsentry = Entry(root, w=3, font=20, textvariable=seconds)
secondsentry.place(x=180, y=160)
root.config(background="navy")

setcountdown = Button(root, text="Start", bd="5", command=submit).place(x=130, y=199)
root.mainloop()