import tkinter as tk
from GuiFuncs import *
from dbHandler import *


root = tk.Tk()
team1Selected =tkinter.StringVar(root)
team1Selected.set("Select an Option")

team2Selected =tkinter.StringVar(root)
team2Selected.set("Select an Option")


VarDuck1=tk.IntVar()
VarDuck2=tk.IntVar()

Cube1=tk.IntVar()

#window setup
TeamList = TeamDropDown()

root.geometry('925x640')

frame1=tk.Frame(root,borderwidth=3,relief="sunken",height=620,width=400)
frame2=tk.Frame(root,borderwidth=3,relief="sunken",height=620,width=400)
frame1.grid(row=2,column=1,)
frame1.grid_propagate(False)
frame2.grid(row=2,column=3,sticky="e")
frame2.grid_propagate(False)



title = tk.Label(master = root,text = 'Scouting application')
title.grid(row=1,column=2)

allienceSwitcher=tk.Button(master= root,text='Switch team',command= lambda: teamSwitch(allienceSwitcher),bg="red",activebackground="red");
allienceSwitcher.grid(row=1,column=1,padx=(10,50),pady=30);

Duck1 = tk.Checkbutton(master= frame1,text="Duck Delivered?",variable= VarDuck1,onvalue=1,offvalue=0)
Duck1.grid(row=2, pady=(10,10), padx=10,column= 1)

Duck2 = tk.Checkbutton(master= frame2,text="Duck Delivered?",variable= VarDuck2,onvalue=1,offvalue=0)
Duck2.grid(row=2, pady=(10,10), padx=10,column= 1)

TeamDropDown1 = tk.OptionMenu(frame1,team1Selected,*TeamList)
TeamDropDown1.grid(row=1,column=2,pady=(5,20))

TeamDropDown2 = tk.OptionMenu(frame2,team2Selected,*TeamList)
TeamDropDown2.grid(row=1,column=2,pady=(5,20))

CubeDeliver1 = tk.Checkbutton(frame1, text = 'Was Cube Deliverd?', variable = Cube1)
CubeDeliver1.grid(row = 2, column = 2)

root.geometry('935x640')
root.grid_anchor("center")


initDB()

root.mainloop()

