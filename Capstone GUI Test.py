# -*- coding: utf-8 -*-
"""
Samuel Meyer

Senior Capstone Project

Wisconsin Lutheran College
"""
global file
file = ""

#imports file and updates canvas
def importfunction():
    global file
    filer = open("dummycode.py")
    file = filer.read()
    dfile = dictfile(file)
    functiondisplay.itemconfig(parsefile, text = dfile.values())
    return

#turns file into dictionary of each line
def dictfile(file):
    dfile = {}
    for line_number, line in enumerate(file):
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
import tkinter as tk
parsegui = tk.Tk()
parsegui.title("Function Parsing Capstone Program Thing")

#import file button
openbutton = tk.Button(parsegui, text = 'open', width = 25, command = importfunction)
openbutton.pack()

#function display canvas
functiondisplay = tk.Canvas(parsegui, width=400, height=400)
functiondisplay.pack()
canvas_height=20
canvas_width=400
y = int(canvas_height / 2)
#functiondisplay.create_line(0, y, canvas_width, y )
parsefile = functiondisplay.create_text(200,300, text = file)

#select previous line button
upbutton = tk.Button(parsegui, text = '/\\', width = 100, )
upbutton.pack()
#select next line button
downbutton = tk.Button(parsegui, text = '\\/', width = 100, )
downbutton.pack()



parsegui.mainloop()