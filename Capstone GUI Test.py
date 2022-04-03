# -*- coding: utf-8 -*-
"""
Samuel Meyer

Senior Capstone Project

Wisconsin Lutheran College
"""
global file
file = ""


def importfunction():
    global file
    filer = open("dummycode.py")
    file = filer.read()
    functiondisplay.itemconfig(parsefile, text = file)
    return

import tkinter as tk
parsegui = tk.Tk()
parsegui.title("Function Parsing Capstone Program Thing")

openbutton = tk.Button(parsegui, text = 'open', width = 25, command = importfunction)
openbutton.pack()

functiondisplay = tk.Canvas(parsegui, width=400, height=400)
functiondisplay.pack()
canvas_height=20
canvas_width=400
y = int(canvas_height / 2)
#functiondisplay.create_line(0, y, canvas_width, y )
parsefile = functiondisplay.create_text(200,300, text = file)

upbutton = tk.Button(parsegui, text = '/\\', width = 100, )
upbutton.pack()
downbutton = tk.Button(parsegui, text = '\\/', width = 100, )
downbutton.pack()

parsegui.mainloop()