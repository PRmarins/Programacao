from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo(' ', 'Eu sei...')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0,500) ,y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text = 'Tu é gay?', font = 'Arial 20 bold', bg='White').pack()
btnYes = Button(root, text='Não', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='Sim', font='Arial 20 bold', command=no).place(x=350, y=100)
root.mainloop()