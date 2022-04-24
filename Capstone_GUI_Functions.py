# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 13:27:44 2022

@author: samme
"""
from tkinter import filedialog as fd

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
    #functiondisplay.itemconfig(parsefile, text = dfile.values())
    return dfile

#turns file into dictionary of each line
def dictfile(lines):
    dfile = {}
    for line_number, line in enumerate(lines):
        dfile[line_number] = line
    print(dfile)
    return dfile
