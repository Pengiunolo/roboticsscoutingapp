import imp


import tkinter

isTeamRed = True;

def teamSwitch(self):
    global isTeamRed;
    if(isTeamRed):
        isTeamRed=False
        self.configure(bg="blue")
    else:
        isTeamRed=True
        self.configure(bg="red")
