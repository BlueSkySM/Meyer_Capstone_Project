# -*- coding: utf-8 -*-
"""
Samuel Meyer

Senior Capstone Project

Wisconsin Lutheran College
"""
import tkinter as tk
from tkinter import filedialog as fd

global file
file = ""

#imports file and updates canvas
def importfunction():
    global file
    #filer = open("dummycode.py")
    file = fd.askopenfilename()
    with open(file, 'r') as f:
        lines = f.readlines()
    print(lines)
    #file = filer.read()
    dfile = dictfile(lines)
    functiondisplay.itemconfig(parsefile, text = dfile.values())
    return

#turns file into dictionary of each line
def dictfile(lines):
    dfile = {}
    for line_number, line in enumerate(lines):
        dfile[line_number] = line
    print(dfile)
    return dfile

"""
To do list:
1. Break code into lines
2. Make line select GUI element
3. integrate line select functionality 
4. edit importfunction to implement parser 
5. get and implement parser 
6. ??? 
7. Pray to god i graduate 
"""

#declare GUI object

parsegui = tk.Tk()
parsegui.title("Function Parsing Capstone Program Thing")

#import file button
openbutton = tk.Button(parsegui, text = 'open', width = 25, command = importfunction)
openbutton.pack()

#function display canvas
functiondisplay = tk.Canvas(parsegui, width=800, height=400)
functiondisplay.pack()
# canvas_height=20
# canvas_width=400
# y = int(canvas_height / 2)
# #functiondisplay.create_line(0, y, canvas_width, y )
parsefile = functiondisplay.create_text(200,300, text = file)

#ui element for line select goes here 

#select previous line button
upbutton = tk.Button(parsegui, text = '/\\' )
upbutton.pack()
#select next line button
downbutton = tk.Button(parsegui, text = '\\/' )
downbutton.pack()

#ui element for text insertion goes here
commentbox = tk.Entry(parsegui)
commentbox.pack()

#ui element for text insertion commit goes here
commentbutton = tk.Button(parsegui, text = "Add Comment")
commentbutton.pack()

#ui element for selecting next function goes here
nextfunction = tk.Button(parsegui, text = "Next Function >")
nextfunction.pack()

parsegui.mainloop()