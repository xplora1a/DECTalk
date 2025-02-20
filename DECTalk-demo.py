#! /usr/bin/python3

import os
from datetime import datetime
import serial
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class dialogue():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("DECTalk demo")
        self.create_widgets()

    def create_widgets(self):
        self.story = ttk.Button(self.win, text="Story")
        self.story.grid(column=1,row=0,padx=5,pady=5)
        self.comment = scrolledtext.ScrolledText(self.win, width=50,height=10, wrap=tk.WORD)
        self.comment.grid(row=2,column=0, columnspan=3,padx=5,pady=5)
        self.add_comment = ttk.Button(self.win, text="Add Comment")
        self.add_comment.grid(column=0,row=3,padx=5,pady=5)
        self.play_comment = ttk.Button(self.win, text="Play Comment")
        self.play_comment.grid(column=1,row=3,padx=5,pady=5)
        self.clear_comment = ttk.Button(self.win, text="Clear Comment")
        self.clear_comment.grid(column=2, row=3,padx=5,pady=5)


window = dialogue()
window.win.mainloop()
