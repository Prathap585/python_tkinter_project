#!/usr/bin/env python3

from Tkinter import *
import time

root = Tk()

#setting screen size
width=1000
height=700
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(width=False, height=False)
root .title("Hotel Management System")

#windows partition
Tops = Frame(root, width=1000, height=100, bg='blue', relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=500, height=700, relief=SUNKEN, bg='red')
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

f3 = Frame(root, width=30, height=700, relief=SUNKEN, bg='yellow')
f3.pack(side=LEFT)

f4 = Frame(root, width=65, height=700, relief=SUNKEN, bg='green')
f4.pack(side=LEFT)

#main window
txt_input = StringVar(value='Fuck you bitch...')
Display = Entry(Tops, font=('arial', 80, 'bold'), fg='white', bd=50, bg='blue', justify='right', textvariable=txt_input )
Display.grid(columnspan=4)

#setting date and time
localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(f2,font=('arial', 20, 'bold'),text=localtime,fg='dark blue',bd=10,anchor=W)
lblInfo.grid(row=0,column=0,columnspan=4)

#buliding calculator
#########row1################
btn7=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='7').grid(row=1,column=0)
btn8=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='8').grid(row=1,column=1)
btn9=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='9').grid(row=1,column=2)
btnC=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='C').grid(row=1,column=3)
#########row2###############
btn4=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='4').grid(row=2,column=0)
btn5=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='5').grid(row=2,column=1)
btn6=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='6').grid(row=2,column=2)
btnplus=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='+').grid(row=2,column=3)
#########row3################
btn1=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='1').grid(row=3,column=0)
btn2=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='2').grid(row=3,column=1)
btn3=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='3').grid(row=3,column=2)
btnminus=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='-').grid(row=3,column=3)
#########row4################
btn0=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='0').grid(row=4,column=0)
btndot=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='.').grid(row=4,column=1)
btndivision=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='/').grid(row=4,column=2)
btnmultiply=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='*').grid(row=4,column=3)
#########row5###############
btnequals=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='=').grid(row=5,column=0)
btnopenbracket=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='(').grid(row=5,column=1)
btnclosebracket=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text=')').grid(row=5,column=2)

root.mainloop()