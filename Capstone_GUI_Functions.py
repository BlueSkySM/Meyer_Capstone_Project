# -*- coding: utf-8 -*-
"""
Samuel Meyer

Senior Capstone Project

Wisconsin Lutheran College
"""

import Capstone_GUI_Elements
from tkinter import filedialog as fd, END

global file
file = ""

#imports file and updates canvas
def importfile():
    global file
    #filer = open("dummycode.py")
    file = fd.askopenfilename()
    with open(file, 'r') as f:
        lines = f.readlines()
    print(lines)
    #file = filer.read()
    dfile = dictfile(lines)
    for value in dfile.values():
        Capstone_GUI_Elements.functiondisplay.insert(END, value + "\n")
    #Capstone_GUI_Elements.functiondisplay.itemconfig(Capstone_GUI_Elements.parsefile, text = dfile.values())
    return dfile

#turns file into dictionary of each line
def dictfile(lines):
    dfile = {}
    for line_number, line in enumerate(lines):
        dfile[line_number] = line
    print(dfile)
    return dfile
