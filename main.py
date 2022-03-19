#import tkinter as tk
from tkinter import *
from GuiFuncs import *
from dbHandler import *

def ButtonDisable(button1):
    
    if  button1["state"] == DISABLED:
        button1.configure(state=NORMAL)
    else:
        button1.configure(state=DISABLED)




root = Tk()
team1Selected =tkinter.StringVar(root)
team1Selected.set("Select an Option")

team2Selected =tkinter.StringVar(root)
team2Selected.set("Select an Option")


VarDuck1=IntVar()
VarDuck2=IntVar()

Cube1=IntVar()
Cube2=IntVar()              

CCube2=IntVar()
CCube1=IntVar()

#window setup
TeamList = TeamDropDown()



frame1=Frame(root,borderwidth=3,relief="sunken",height=620,width=440)
frame2=Frame(root,borderwidth=3,relief="sunken",height=620,width=440)
frame1.grid(row=2,column=1,sticky="e")
frame1.grid_propagate(False)
frame2.grid(row=2,column=3,sticky="e")
frame2.grid_propagate(False)

InnerFrame1 = LabelFrame(frame1,width=440,height=220)
InnerFrame1.grid(row = 1, column = 1)
InnerFrame1.grid_propagate(False)


title = Label(master = root,text = 'Scouting application',)
title.grid(row=1,column=2)

allienceSwitcher=Button(master= root,text='Switch team',command= lambda: teamSwitch(allienceSwitcher),bg="red",activebackground="red");
allienceSwitcher.grid(row=1,column=1,padx=(10,50),pady=30);

Duck1 = Checkbutton(master= InnerFrame1,text="Duck Delivered?",variable= VarDuck1,onvalue=1,offvalue=0)
Duck1.grid(row=2, pady=(10,10), padx=10,column= 1)

Duck2 = Checkbutton(master= frame2,text="Duck Delivered?",variable= VarDuck2,onvalue=1,offvalue=0)
Duck2.grid(row=2, pady=(10,10), padx=10,column= 1)

TeamDropDown1 = OptionMenu(frame1,team1Selected,*TeamList)
TeamDropDown1.grid(row=0,column=1,pady=(5,20))

TeamDropDown2 = OptionMenu(frame2,team2Selected,*TeamList)
TeamDropDown2.grid(row=1,column=1,pady=(5,20))

CubeCorrect1 = Checkbutton( InnerFrame1, text = 'Cube Delived To Correct Level?', variable = CCube1, state=DISABLED)
CubeCorrect1.grid(row = 3, column = 1)
CubeCorrect1["state"]=DISABLED

CubeCorrect2 = Checkbutton( frame2, text = 'Cube Delived To Correct Level?', variable = CCube2, state=DISABLED)
CubeCorrect2.grid(row = 3, column = 1)
CubeCorrect2["state"]=DISABLED

CubeDeliver1 = Checkbutton(InnerFrame1, text = 'Was Cube Delivered?', variable = Cube1, command=lambda: ButtonDisable(CubeCorrect1))
CubeDeliver1.grid(row = 2, column = 2)

CubeDeliver2 = Checkbutton(frame2, text = 'Was Cube Delivered?', variable = Cube2, command=lambda: 
ButtonDisable(CubeCorrect2))
CubeDeliver2.grid(row = 2, column = 2)



root.geometry('1200x640')
root.grid_anchor("center")


initDB()

root.mainloop()

