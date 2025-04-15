#! /usr/bin/python3

# libraries Import
from tkinter import ttk
import tkinter
import tkinter.scrolledtext
from threading import Thread
import serial
from queue import Queue
import time
import random

story2= [
#    "[:phoneme arpabet speak on]",
    "[:np] A Redding Shaggy Bear Tale for Seven DECtalk Software Voices.",
    "By Dennis Klatt.",
    "[:np] Once upon a time, there were three bears. They lived in the great forest and tried to adjust to modern times.",
    "[:nh] I'm papa bear. I love my family, but I love [\"]honey best.",
    "[:nb] I'm mama bear. Being a mama bear is a drag.",
    "[:nk] I'm baby bear and I have trouble relating to all of the demands of older bears.",
    "[:np] One day, the three bears left their condominium to search for honey.",
    "While they were gone, a beautiful young lady snuck into the bedroom through an open window.",
    "[:nw] My name is Wendy. My purpose in entering this building should be clear. I am planning to steal the family jewels.",
    "[:np] Hot on her trail was the famous police detective, Frank.",
    "[:nf] Have you seen a lady carrying a laundry bag over her shoulder?",
    "[:np] A woman, kneeling with her left ear firmly placed against a large rock, responded.",
    "[:nu] [']No. No [/]one passed this [/ \\]way.",
    "I've been listening for [']earthquakes all morning, but have only spotted three bears searching for honey.",
    "[:np] The end."
]

prompts = [
    "We'd love to hear your thoughts on the digital technology exhibition.",
    "Welcome! Please share your insights.",
    "We'd appreciate your comments on our digital showcase.",
    "Hi there! How are you enjoying the exhibition?",
    "Let us know which displays caught your attention and why.",
    "Please tell us what you think of our exhibition.",
    "We'd love to know what you liked best from our digital experience!",
    "Thank you for visiting! Share your impressions with us.",
    "We're all ears! Tell us what sparked your curiosity.",
    "Got a moment? Help us with your valuable feedback.",
    "Please take a second to let us know what you think.",
    "Spot something you love? Tell us about it!",
    "Hi! Please share your thoughts.",
    "Do you remember working with equipment like this? Share your memories with us.",
    "Are you enjoying the show? Let us know!",
    "We're glad you're here! A short comment from you helps us.",
    "Hope the exhibits inspired you! Share your thoughts.",
    "Let us know what you really think!"
]
global lastAvtivity

# Main Window Properties
window = tkinter.Tk()
window.title("DECTalk")
window.geometry("900x450")


# Functions
def speakdelay(prompt):
    delay = max(int(len(prompt)*0.15), 2)
    return delay

def Button_id1_command():   #Story
    global lastAvtivity
    lastAvtivity = time.time()
    for line in story2:
        DECtalkQueue.put(line+"\n")
    ProgressBar = Thread(target=SpeakProgressBar, args=[70])
    ProgressBar.start()
    pass
def Button_id4_command():   #Speak Comment
    global lastAvtivity
    lastAvtivity = time.time()
    prompt = Entry_id2.get("1.0", tkinter.END)
    if len(prompt) > 0:
        DECtalkQueue.put(prompt)
        ProgressBar = Thread(target=SpeakProgressBar, args=[speakdelay(prompt)])
        ProgressBar.start()
    pass
def Button_id5_command():   #Save Comment
    global lastAvtivity
    lastAvtivity = time.time()
    comment = Entry_id2.get("1.0", tkinter.END)
    with open("Comment.txt", mode="a") as file:
        file.write("\n"+time.strftime("%Y-%m-%d %H:%M:%S")+"\n")
        file.writelines(comment)
        file.close
    Button_id5["state"] = "disabled"
    pass
def Button_id6_command():   #Clear Comment
    global lastAvtivity
    lastAvtivity = time.time()
    Entry_id2.delete("1.0", tkinter.END)
    Button_id5["state"] = "normal"
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
    ProgressBar_id0["value"] = DelaySeconds
    window.update()
    time.sleep(1)
    ProgressBar_id0["value"] = 0
    Button_id4["state"] = "normal"
    Button_id1["state"] = "normal"
    Button_id5["state"] = "normal"
    Button_id6["state"] = "normal"
    window.update()
    pass

def DECtalkSpeak(DECTalkQueue):
    global lastAvtivity
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
        lastAvtivity = time.time()
        time.sleep(int(len(prompt)*0.07))
    pass

# if there has been no activity for 10 minutes, it will randomly select a 
# prompt from the list and speak it. This is a seperate thread.
def RandomPrompt():
    global lastAvtivity
    while True:
        if time.time() - lastAvtivity > 600:
            prompt = random.choice(prompts)
            DECtalkQueue.put(prompt)
            ProgressBar = Thread(target=SpeakProgressBar, args=[speakdelay(prompt)])
            ProgressBar.start()
            time.sleep(speakdelay(prompt))
            lastAvtivity = time.time()
        time.sleep(30)
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

# start the DECTalk thread
DECtalkQueue = Queue()
DECtalkQueue.put("Starting the DECTalk Digital Comment system.\n")
DECtalkThread = Thread(target=DECtalkSpeak, args=[DECtalkQueue], daemon=True)
DECtalkThread.start()

# start the RandomPrompt thread
lastAvtivity = time.time()
RandomPromptThread = Thread(target=RandomPrompt, daemon=True)
RandomPromptThread.start()

# run the main loop
Entry_id2.focus()
window.attributes("-fullscreen", True)
window.mainloop()
