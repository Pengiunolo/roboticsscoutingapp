from re import I
import sqlite3
import tkinter

isTeamRed = True;

def teamSwitch(self):
    global isTeamRed;
    if(isTeamRed):
        isTeamRed=False
        self.configure(bg="blue",activebackground="blue")
    else:
        isTeamRed=True
        self.configure(bg="red",activebackground="red")

def dynamicFrameresizer(root,f1,f2):
    a = root.winfo_width()/2 - 125
    f1.configure(width=a)
    f2.configure(width=a)