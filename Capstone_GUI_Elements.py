# -*- coding: utf-8 -*-
"""
Samuel Meyer

Senior Capstone Project

Wisconsin Lutheran College
"""

import tkinter as tk
from tkinter import *
from Capstone_GUI_Functions import importfile, file, index, upPress, downPress, addComment, nextPress, savefile
#from Capstone_GUI_Functions import file

#declare GUI object

parsegui = tk.Tk()
parsegui.title("Function Parsing Capstone Program Thing")

#function display canvas
functiondisplay = tk.Text(parsegui, width=80, height=40)
functiondisplay.pack()
#parsefile = functiondisplay.create_text(200,300, text = file)

#import file button

openbutton = tk.Button(parsegui, text = 'open', width = 25, command = importfile)

openbutton.pack()


#ui element for line select goes here 
indexlabel = tk.Label(parsegui, text = "Current Line: " + str(index))
indexlabel.pack()

#select previous line button
upbutton = tk.Button(parsegui, text = '/\\', command= upPress )
upbutton.pack()
#select next line button
downbutton = tk.Button(parsegui, text = '\\/', command= downPress )
downbutton.pack()

#ui element for text insertion goes here
commentbox = tk.Entry(parsegui)
commentbox.pack()

#ui element for text insertion commit goes here
commentbutton = tk.Button(parsegui, text = "Add Comment", command = addComment)
commentbutton.pack()

#ui element for selecting next function goes here
nextfunction = tk.Button(parsegui, text = "Next Function >", command = nextPress)
nextfunction.pack()

savebutton = tk.Button(parsegui, text = "Save file", command = savefile)
savebutton.pack()