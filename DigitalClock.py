import tkinter as tk
import datetime as dt
import pyglet

pyglet.font.add_file("DigitalDisplay.ttf")
pyglet.font.load('Digital Display', 180)

MainWin = tk.Tk()

MainWin.title("Digital Clock")
MainWin.configure(bg="#0A4D68")

def Update():
    CurrentTime = dt.datetime.now()

    time_str = f"{CurrentTime.hour}:{CurrentTime.minute}:{CurrentTime.second}"

    TimeLabel.configure(text=time_str)

    TimeLabel.after(1000,Update)

TimeLabel = tk.Label(MainWin,font=("Digital Display",180,"bold"),fg="#ED2B2A",bg="#0A4D68")
TimeLabel.pack()

Update()

MainWin.mainloop()