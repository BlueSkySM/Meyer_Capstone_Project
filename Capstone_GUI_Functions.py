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
global dfile
global dfunc
nextPressed = False
file = ""
sfile = ""
dfile = deque
dfunc = deque
index = 0

#file manipulation code

def importfile():
    #imports file and creates list of lines
    #turns lines into deque so they can be parsed by popping the stack
    global file
    global dfile

    #test hardcode
    #filer = open("dummycode.py")
    file = fd.askopenfilename()
    with open(file, 'r') as f:
        lines = f.readlines()
    #test print
    #print(lines)

    
    dfile = dequefile(lines)
    parsefunc()
    return


def parsefunc():
    global dfile
    global sfile
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
                
                flist.append(line)
                
                if "return" in line:
                    break
                line = dfile.popleft()
                #test print
                print(line)
            dictfunction(flist)
            return
        else:
            #Capstone_GUI_Elements.functiondisplay.insert(END, line)
            sfile += line
            #test print
            #print(sfile)
    
    Capstone_GUI_Elements.functiondisplay.delete("1.0", "end")
    Capstone_GUI_Elements.functiondisplay.insert(END, "End of File")
    savefile()
    #save file
    
    return

def dequefile(lines):
    #turns any given list into a deque
    dfile = deque(lines)
    #test print
    #print(dfile)
    return dfile

def dictfunction(flines):
    global dfunc
    #creates deque from list for easier popping into saved file later
    #pushes the contents of the function to the GUI
    dfunc = dequefile(flines)
    updateCanvas(dfunc)
    return




# element manipulation code

def upPress():
    # up line select element
    # if you try to go less than line 0, it does nothing 
    global index
    if index == 0:
        return
    else:
        index -= 1
    # update index on canvas
    updateIndex()
    return

def downPress(): 
    # down line select element
    # if you try to go greater than the max of the function deque, it does nothing 
    global index
    global dfunc
    #test print
    #print(len(dfunc))
    if index + 1 >= len(dfunc):
        return
    else:
        index += 1
    # update index on canvas
    updateIndex()
    return

def nextPress():
    global dfunc
    global index
    global sfile
    index = 0
    updateIndex()
    while dfunc:
        line = dfunc.popleft()
        sfile += line
    
    #print(sfile)
    parsefunc()
    return

def updateIndex():
    Capstone_GUI_Elements.indexlabel['text'] = "Current Line: " + str(index+1)
    return



def addComment():
    # temporarily converts deque to a list 
    # adds text from tkinter entry box as string to line
    # clears entry to allow another entry to be made
    # updates canvas
    
    global index
    global dfunc
    addedcomment = Capstone_GUI_Elements.commentbox.get()
    listdfunc = list(dfunc)
    listdfunc[index] = listdfunc[index].replace("\n", "") + " # " + str(addedcomment) + "\n"
    dfunc = deque(listdfunc)
    Capstone_GUI_Elements.commentbox.delete(0, "end")
    updateCanvas(dfunc)
    return


def updateCanvas(dlines):
    Capstone_GUI_Elements.functiondisplay.delete("1.0", "end")
    for line in dlines:
        #line = dfunc.popleft()
        Capstone_GUI_Elements.functiondisplay.insert(END, line)
    return
    

def savefile():
    #creates new file from saved results using filedialog
    global sfile
    file = fd.asksaveasfile(defaultextension=".py", filetypes=[("Python File",".py")])
    if not file:
        Capstone_GUI_Elements.parsegui.destroy()
        return
    file.write(sfile)
    file.close()
    Capstone_GUI_Elements.parsegui.destroy()
    return