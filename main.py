import tkinter as tk
from inputHandler import *

root = tk.Tk()

root.geometry('925x640')
title= tk.Label(master = root,text = 'Scouting application')
title.grid(row=1,column=3)
teamSwitcher=tk.Button(text='Switch team',command= lambda: teamSwitch(teamSwitcher),bg="red",activebackground="red");
teamSwitcher.grid(row=1,column=1,padx=(10,50),pady=30);
