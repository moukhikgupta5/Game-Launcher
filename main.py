from tkinter import *
import random
from tkinter import messagebox
import jumbledmodule
import tictactoemodule


#-----main----

# create a GUI window
root=Tk()

#to give title to the gui window
root.title('Game Launcher')

#to set geomtry
root.geometry('315x300')

#to set bg colour
root.configure(background='#0ABDE3')

#1st label to show welcome message
l1 = Label(root , text='Welcome to the Game Launcher' , fg='#192A56',bg='#0ABDE3',font=("Helvetica", 16))
l1.grid(row=0,column=0)

#empty label to skip a row
l2 = Label(root , text='' , fg='#192A56',bg='#0ABDE3',font=("Helvetica", 16))
l2.grid(row=2,column=0)

#button for jumbled game
b1 = Button(root,text= ' Play Jumbled   ',command=jumbledmodule.playjumbled,bd=10,bg='#67E6DC',fg='#192A56')
b1.grid(row=3,column=0)

#empty label to skip a row
l10 = Label(root , text='' , fg='#192A56',bg='#0ABDE3',font=("Helvetica", 16))
l10.grid(row=4,column=0)

#button to play tic tac toe
b2=Button(root,text='Play Tic Tac Toe',command=tictactoemodule.playtictactoe,bd=10,bg='#67E6DC',fg='#192A56')
b2.grid(row=5,column=0)

#empty label to skip a row
l3 = Label(root , text='' , fg='#192A56',bg='#0ABDE3',font=("Helvetica", 16))
l3.grid(row=6,column=0)

#label giving credits
l4 = Label(root , text='Created by :-' , fg='#192A56',bg='#0ABDE3',font=("Helvetica", 14))
l4.grid(row=7,column=0)

#label for names
l5 = Label(root , text='Moukhik Gupta' , fg='#192A56',bg='#0ABDE3',font=("Helvetica", 13))
l5.grid(row=8,column=0)

# start the GUI
root.mainloop()
