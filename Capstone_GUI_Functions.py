# -*- coding: utf-8 -*-
"""
Samuel Meyer

Senior Capstone Project

Wisconsin Lutheran College
"""

import Capstone_GUI_Elements
from tkinter import filedialog as fd, END
from collections import deque
from time import sleep

global file
global sfile
global index
global nextPressed
nextPressed = False
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
            flist = []
            while True:
                #test print
                print(line)
                
                flist.append(line)
                
                if "return" in line:
                    break
                line = dfile.popleft()
            #print(fsubdeque)
            dictfunction(flist)
        else:
            #Capstone_GUI_Elements.functiondisplay.insert(END, line)
            sfile += line
    
    #save file
    
    return


def nextButtonPress():
    #signifies that the Next Function button has been pressed 
    global nextPressed
    nextPressed = True
    return

def dequefile(lines):
    #turns file into deque so it can be popped off as it iterates
    dfile = deque(lines)
    #test print
    #print(dfile)
    return dfile

def dictfunction(flines):
    #pushes the contents of the function to the GUI
    #allows manipulating until next function button is pressed
    global nextPressed
    dfunc = dequefile(flines)
    while nextPressed == False:
    
        
        updateCanvas(dfunc)
        sleep(5)

    if nextPressed == True:
        #clear canvas and changes value to ready next function
        Capstone_GUI_Elements.functiondisplay.delete("1.0", "end")
        nextPressed = False
        return

def updateCanvas(dlines):
    Capstone_GUI_Elements.functiondisplay.delete("1.0", "end")
    for line in dlines:
        #line = dfunc.popleft()
        Capstone_GUI_Elements.functiondisplay.insert(END, line)
    

def savefile(dfile):
    #creates new file from saved results using filedialog 
    return