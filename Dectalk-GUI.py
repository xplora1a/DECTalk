
# libraries Import
from tkinter import ttk
import tkinter
import tkinter.scrolledtext
from threading import Thread
import serial
from queue import Queue
import time


# Main Window Properties
window = tkinter.Tk()
window.title("DECTalk")
window.geometry("900x450")


# Functions
def Button_id1_command():   #Story
    pass
def Button_id4_command():   #Speak Comment
    prompt = Entry_id2.get("1.0", tkinter.END)
    if len(prompt) > 0:
        DECtalkQueue.put(prompt)
        ProgressBar = Thread(target=SpeakProgressBar, args=[int(len(prompt)/10)])
        ProgressBar.start()
    pass
def Button_id5_command():   #Save Comment
    print(Entry_id2.get("1.0", tkinter.END))
    pass
def Button_id6_command():   #Clear Comment
    Entry_id2.delete("1.0", tkinter.END)
    pass

def SpeakProgressBar(DelaySeconds):
    Button_id4["state"] = "disabled"
    Button_id1["state"] = "disabled"
    Button_id5["state"] = "disabled"
    Button_id6["state"] = "disabled"
    ProgressBar_id0["value"] = 0
    ProgressBar_id0["maximum"] = DelaySeconds
    for i in range(DelaySeconds):
        ProgressBar_id0["value"] = i
        window.update()
        time.sleep(1)
    ProgressBar_id0["value"] = 0
    Button_id4["state"] = "normal"
    Button_id1["state"] = "normal"
    Button_id5["state"] = "normal"
    Button_id6["state"] = "normal"
    pass

def DECtalkSpeak(DECTalkQueue):
    print("DECtalkSpeak")
    DECTalk = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, bytesize=8, parity="N", stopbits=2, xonxoff=True, rtscts=True)
    while True:
        prompt = DECTalkQueue.get()
        print(prompt)
        DECTalk.write(prompt)
        DECTalk.flush()
        time.sleep(int(len(prompt)/10))
    pass
# Widgets

Label_id7 = tkinter.Label(
    master=window,
    text="Comment on the Exabition",
    font=("Arial", 24),
    height=1,
    width=30,
    )
Label_id7.place(x=160, y=10)
Button_id6 = tkinter.Button(
    master=window,
    text="Clear Comment",
    font=("Arial", 20),
    height=1,
    width=12,
    borderwidth=2,
    bg="#FFFFFF",
    fg="#222222",
    command=Button_id6_command
    )
Button_id6.place(x=580, y=180)
Button_id5 = tkinter.Button(
    master=window,
    text="Save Comment",
    font=("Arial", 20),
    height=1,
    width=12,
    borderwidth=2,
    bg="#FFFFFF",
    fg="#222222",
    command=Button_id5_command
    )
Button_id5.place(x=580, y=110)
Button_id4 = tkinter.Button(
    master=window,
    text="Speak Comment",
    font=("Arial", 20),
    height=1,
    width=12,
    borderwidth=2,
    bg="#FFFFFF",
    fg="#222222",
    command=Button_id4_command
    )
Button_id4.place(x=580, y=50)
Label_id3 = tkinter.Label(
    master=window,
    text="Click this and the DECTalk will tell you a story:",
    font=("Arial", 14),
    height=1,
    width=40,
    bg="#FFFFFF",
    fg="#222222",
    justify="right"
    )

Label_id3.place(x=100, y=295)
Entry_id2 = tkinter.scrolledtext.ScrolledText(
    master=window,
    wrap=tkinter.WORD,
    font=("Arial", 12),
    width=40,
    height=10,
    borderwidth=2,
    bg="#FFFFFF",
    fg="#222222",
    )
Entry_id2.place(x=100, y=50)
Button_id1 = tkinter.Button(
    master=window,
    text="Story",
    font=("Arial", 20),
    height=1,
    width=7,
    borderwidth=2,
    bg="#FFFFFF",
    fg="#222222",
    command=Button_id1_command
    )
Button_id1.place(x=580, y=290)
ProgressBar_id0 = ttk.Progressbar(
    master=window,
    orient="horizontal",
    mode="determinate",
    length=400,
    )
ProgressBar_id0.place(x=100, y=400)

#start the DECTalk thread
DECtalkQueue = Queue()
DECtalkQueue.put("Starting the DECTalk Demo")
DECtalkThread = Thread(target=DECtalkSpeak, args=[DECtalkQueue], daemon=True)
DECtalkThread.start()

#run the main loop
Entry_id2.focus()
window.mainloop()
