#!/usr/bin/python
import Tkinter
from Tkinter import *

# -----------------------------------------
# label1=Label(frame, text='Trasact #'+num)
def trasact_menu(parent,frame,num):
	trans_bool=IntVar()
	label1=Checkbutton(frame,text='Trasact #'+num,variable=trans_bool,width=8,onvalue=1,offvalue=0)
	trans_bool.set(1)
	label1.pack(side=LEFT)
	trans_type=StringVar(frame)
	trans_type.set("No action")
	choice1=OptionMenu(frame,trans_type,"No Action", "Buy Stock", "Buy Put  ", "Buy Call ")
	choice1.pack(side=LEFT)
	value1=Entry(frame,width=10)
	value1.pack(side=LEFT)

# -----------------------------------------
top = Tkinter.Tk()

frameval=Frame(top)
frameval.pack()

frame1=Frame(frameval)
frame1.pack(side=TOP)
trasact_menu(frameval,frame1,'1')

frame2=Frame(frameval)
frame2.pack(side=TOP)
trasact_menu(frameval,frame2,'2')

frame3=Frame(frameval)
frame3.pack(side=TOP)
trasact_menu(frameval,frame3,'3')

frame4=Frame(frameval)
frame4.pack(side=TOP)
trasact_menu(frameval,frame4,'4')

top.mainloop()

