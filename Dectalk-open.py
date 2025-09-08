#! /usr/bin/python3

# libraries Import
from tkinter import ttk
import tkinter
import tkinter.scrolledtext
from threading import Thread
import serial
from queue import Queue
import time

story3= [
    "[:np]",
    "[oy<300,13>_<300>ax<600,13>_<300>eh<600,13>_<1600>]",
    "I am a DECTalk text-to-speech synthesizer.[_<1600>]",
    "[jh<300,10>_<300>ow<600,10>_<300>aw<600,10>_<1600>]",
    "I am a DECTalk text-to-speech synthesizer.[_<1600>]",
    
    "In nineteen sixty-four, a tech town was born.",
    "In a place called Redding.[_<600>]",
    "It was a town that would become famous for its",
    "contribution to the world of computing.[_<600>]",
    "I am a DECTalk text-to-speech synthesizer.[_<600>]",
    "I gave Steefen Hawking back his ability to speak.[_<600>]",
    "I was developed by Digital Equipment in the nineteen eighties.",
    "I was preserved by Edward Hammond,[_<600>]",
    "and was restored to operation by The Redding Repair Cafe,[_<300>]",
    "at the Redding Hack-space.[_<600>]",
    "I am proud to be surrounded by so many other friends from the past.",
    "[_<1600>]",
    "[oy<300,13>_<300>oy<600,13>_<300>oy<600,13>_<1600>]",
    "I am a DECTalk text-to-speech synthesizer.[_<1600>]",
    "[jh<300,10>_<300>jh<600,10>_<300>jh<600,10>_<1600>]",
    "I am a DECTalk text-to-speech synthesizer.[_<1600>]",
    "I am a DECTalk text-to-speech synthesizer.[_<1600>]",
    "I am a DECTalk.[_<1600>]",
    "I am a DECTalk.[_<1600>]",
    "I am a DECTalk.[_<1600>]",
    "I am a DECTalk text-to-speech synthesizer.[_<1600>]",
    "DECTalk.[_<1600>]",
    "DECTalk.[_<1600>]",
    "DECTalk.[_<1600>]",
    "DECTalk text-to-speech synthesizer.[_<1600>]"
]

story2=[
    "[:np]",
    "humanityi survival depends not on inventions but on wisdom.",
    "In the not so distant future, humanity walks a razors edge.",
    "Artificial intelligence, once our greatest tool,",
    "has become a force shaping every choice, every breath, every heartbeat of civilization.",
    "Cities shimmer with impossible technology, disease is a relic of history,",
    "and the stars themselves seem within reach.",
    "But beneath this brilliance lies a shadow: power concentrated in unseen hands,",
    "a world where privacy has vanished, and algorithms know us better than we know",
    "ourselves. This is not a tale of utopia or ruin, but of a fragile species standing at",
    "the crossroads of its own destiny.",
    "The question is not whether AI will change humanity.",
    "[_<1600>]but whether humanity will endure its own creation",
    "[_<1600>]",
    "We built the future. But can we survive it?"
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
