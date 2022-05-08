# -*- coding: utf-8 -*-
"""
Samuel Meyer

Senior Capstone Project

Wisconsin Lutheran College
"""

import Capstone_GUI_Elements
from tkinter import filedialog as fd, END
from collections import deque

global file
global sfile
file = ""
sfile = ""

def importfile():
    #imports file and updates text field with lines
    #adds non-function lines to output loop
    #when it reaches a function creates dictionary
    #repeats till end of file
    global file
    global sfile
    #test hardcode
    #filer = open("dummycode.py")
    file = fd.askopenfilename()
    with open(file, 'r') as f:
        lines = f.readlines()
    #test print
    #print(lines)

    
    dfile = dequefile(lines)
    
    while dfile:
        #pop leftmost (top of program file)
        #check for function definition
        #if yes create deque out of function
        #otherwise add to end of saved file
        line = dfile.popleft()
        #test print
        print(line)
        
        if line.startswith("def"):
            fsubdeque = deque(line)
            while not "return" in line:
                line = dfile.popleft()
                fsubdeque.append(line)
            
            print(fsubdeque)
            dictfunction(fsubdeque)
        else:
            #Capstone_GUI_Elements.functiondisplay.insert(END, line)
            sfile += line
    
    #save file
    
    return


def dequefile(lines):
    #turns file into deque so it can be popped off as it iterates
    dfile = deque(lines)
    #test print
    print(dfile)
    return dfile

def dictfunction(subdeque):
    #creates a dictionary of function contents from subdeque
    #allows manipulating until next function button is pressed
    Capstone_GUI_Elements.functiondisplay.insert(END, subdeque)
    return


def savefile(dfile):
    
    return