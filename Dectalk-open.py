#! /usr/bin/python3

# libraries Import
from tkinter import ttk
import tkinter
import tkinter.scrolledtext
from threading import Thread
import serial
from queue import Queue
import time

story2= [
    "[:np]",
    "Hello. I am a DECTalk text-to-speech synthesizer.",
    "I gave Stephen Hawking back his ability to speak",
    "in the early ninetween eighties.",
    "I have had many other applications, such as providing computer-stored",
    "details in telephone calls to emergency services,",
    "rather than simply sounding an alarm.", 
    "I even used to call to check the needs of people who receive",
    "meals-on-wheels.",
    "I was developed by Digital Equipment Corporation.",
    "This particular unit was preserved by Edward Hammond,",
    "and was restored to operation by The Redding Repair Cafe,",
    "at the Redding Hack-space.",
    "I am proud to be surrounded by so many other friends from the past.",
    "But today I have the honour of opening the Readding Museums",
    "Digital Equipment Corporation exhibition.",
    "[:nf]I therefore declare the exhibition open.",
    "[:np]Thank you."
]

# Main Window Properties
window = tkinter.Tk()
window.title("DECTalk Open Exhibition")
window.geometry("900x450")


# Functions
def speakdelay(prompt):
    delay = max(int(len(prompt)*0.15), 2)
    return delay

def Button_id1_command():   #Story
    for line in story2:
        DECtalkQueue.put(line+"\n")
    ProgressBar = Thread(target=SpeakProgressBar, args=[47])
    ProgressBar.start()
    pass

def SpeakProgressBar(DelaySeconds):
    Button_id1["state"] = "disabled"
    ProgressBar_id0["value"] = 0
    ProgressBar_id0["maximum"] = DelaySeconds
    for i in range(DelaySeconds):
        ProgressBar_id0["value"] = i
        window.update()
        time.sleep(1)
    ProgressBar_id0["value"] = DelaySeconds
    window.update()
    time.sleep(1)
    ProgressBar_id0["value"] = 0
    Button_id1["state"] = "normal"
    window.update()
    pass

def DECtalkSpeak(DECTalkQueue):
    try:
        DECTalk = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, bytesize=8, parity="N", stopbits=2, xonxoff=True, rtscts=True)
        Connected = True
    except:
        Connected = False
    while True:
        prompt = DECTalkQueue.get().encode("ascii")
        print(prompt)
        if Connected:
            DECTalk.write(prompt)
            DECTalk.flush()
        time.sleep(int(len(prompt)*0.07))
    pass

# Widgets

Label_id3 = tkinter.Label(
    master=window,
    text="Click this and the DECTalk will open the exabition:",
    font=("Arial", 14),
    height=1,
    width=40,
    bg="#FFFFFF",
    fg="#222222",
    justify="right"
    )

Button_id1 = tkinter.Button(
    master=window,
    text="Open Exabition",
    font=("Arial", 20),
    height=1,
    width=20,
    borderwidth=2,
    bg="#FFFFFF",
    fg="#222222",
    command=Button_id1_command
    )
Button_id1.place(x=280, y=290)
ProgressBar_id0 = ttk.Progressbar(
    master=window,
    orient="horizontal",
    mode="determinate",
    length=400,
    )
ProgressBar_id0.place(x=100, y=400)

#start the DECTalk thread
DECtalkQueue = Queue()
DECtalkQueue.put("[:np]Starting the DECTalk system.\n")
DECtalkThread = Thread(target=DECtalkSpeak, args=[DECtalkQueue], daemon=True)
DECtalkThread.start()


#run the main loop
window.mainloop()
