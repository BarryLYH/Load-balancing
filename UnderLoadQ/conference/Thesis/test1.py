from tkinter import *
import tkinter.font as tkFont

root = Tk()
ft = tkFont.Font(family = 'Fixdsys')

Label(root, text = 'd',font=ft).grid()
k = root.mainloop()
print(k)