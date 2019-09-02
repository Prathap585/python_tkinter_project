#!/usr/bin/env python3

try:
    # Python2
    from Tkinter import * 
    import ttk
except ImportError:
    # Python3
    import tkinter as tk
    import tkinter.ttk as ttk
import time

msg1 = 'Welcome to python programming.....'
text1 = ''
n = 0

##################scrolling text in textfield###############
def scrollText():
    global text1,n,msg1
    for t in range(len(msg1)):
        for k in range(t):
            text1 += " "
        for g in range(len(msg1)-t):
            text1 += msg1[g]
        text1 = text1.strip()
        f2.update()
        f2.after(200)
        scroll_text.set('')
        scroll_text.set(text1)
        text1 = ''
    scroll_text.set('')
    txtScroll.after(200,scrollText)


##################calculator functions##############
def calcBtn(numbers):
    global operator
    operator=operator + str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    operator=''
    txt_input.set('')
    Display.insert(0,'Start Calculating...')

def equals():
    global operator
    sumup=float(eval(operator))
    txt_input.set(sumup)
    operator=''

###################total btn function##################
def totalControlBtn():
    #cost of meal
    selectedMeal=mealDicator.get()
    selectedMealQty=mealQty.get() 
    if selectedMeal == 'Fried Rice':
        mealCost.set(selectedMealQty*1.8)
    elif selectedMeal == 'Biryani':
        mealCost.set(selectedMealQty*3.7)
    elif selectedMeal == 'Tandoori':
        mealCost.set(selectedMealQty*4.7)
    elif selectedMeal == 'Shawarma':
        mealCost.set(selectedMealQty*5.7)
    else:
        mealCost.set(selectedMealQty*0.0)

    #cost of drink
    selectedDrink=drinkDicator.get()
    selectedDrinkQty=drinkQty.get() 
    if selectedDrink == 'Coke':
        drinkCost.set(selectedDrinkQty*1.8)
    elif selectedDrink == 'Pepsi':
        drinkCost.set(selectedDrinkQty*3.7)
    elif selectedDrink == 'Lemonide':
        drinkCost.set(selectedDrinkQty*4.7)
    elif selectedDrink == 'Water':
        drinkCost.set(selectedDrinkQty*5.7)
    else:
        drinkCost.set(selectedDrinkQty*0.0)

    #cost of delivery
    devCostMeal = float(mealCost.get())
    devCostDrink = float(drinkCost.get())
    deliveryCost = (devCostMeal + devCostDrink) * 0.5

    #room cost
    roomType = v.get()
    null = 0.0
    vipRoom = 10.0
    vipRoomDevCost = deliveryCost/(10*0.5)

    normalRoom = 5.0
    normalRoomDevCost = deliveryCost/(5*2.5)

    if roomType == 1:
        if chkb1.get() == 1:
            serviceFee.set(vipRoomDevCost)
            roomCost.set(10.0)
            devCost.set(deliveryCost)
        else:
            serviceFee.set(null)
            roomCost.set(10.0)
            devCost.set(null)
    elif roomType == 2:
        if chkb1.get() == 1:
            serviceFee.set(normalRoomDevCost)
            roomCost.set(5.0)
            devCost.set(deliveryCost)
        else:
            serviceFee.set(null)
            roomCost.set(5.0)
            devCost.set(null)
        
    elif roomType == 3:
        if chkb1.get() == 1:
            serviceFee.set(null)
            roomCost.set(null)
            devCost.set(null)
        else:
            serviceFee.set(null)
            roomCost.set(null)
            devCost.set(null)
        
    
    totalOrderCost = float(mealCost.get())+float(drinkCost.get())+float(roomCost.get())+float(devCost.get())+float(serviceFee.get())
    totalCost.set(totalOrderCost)
    displayTotal = "Total = $",totalOrderCost

    Display.delete(0,END)
    Display.insert(0,displayTotal)

    if totalCost.get() == '0.0':
        Display.delete(0,END)
        Display.insert(0,'Please, make an order')

###########currency converter method################
def currencyConvert():
    currncy = currenyConv.get()
    selectedCountry = indicator.get()
    if selectedCountry == 'China':
        Display.delete(0,END)
        Display.insert(0, ('Yuan',(currncy*6.88)))
    elif selectedCountry == 'France':
        Display.delete(0,END)
        Display.insert(0, ('Euro',(currncy*0.81)))
    elif selectedCountry == 'Ghana':
        Display.delete(0,END)
        Display.insert(0, ('Cedi',(currncy*4.88)))
    elif selectedCountry == 'Mexico':
        Display.delete(0,END)
        Display.insert(0, ('MXN',(currncy*18.90)))
    elif selectedCountry == 'Nigeria':
        Display.delete(0,END)
        Display.insert(0, ('Naira',(currncy*361.01)))
    elif selectedCountry == 'USA':
        Display.delete(0,END)
        Display.insert(0, ('Dollar',(currncy*1.00)))
    else:
        Display.delete(0,END)
        Display.insert(0, 'Error:Select country')


##################reset control button###############
def resetControlBtn():
    Display.delete(0,END)
    Display.insert(0,'System resetting.....')
    Display.after(1000,reset)

def reset():
    clear()
    Display.delete(0,END)
    Display.insert(0,'Reset complete')
    mealDicator.set(value='Delicious Meal')
    drinkDicator.set(value='Drinks')
    indicator.set(value='')
    txtQtyDrink.delete(0,END)
    txtQtyDrink.insert(0,0)
    txtQtyMeal.delete(0,END)
    txtQtyMeal.insert(0,0)
    txtAmount.delete(0,END)
    txtAmount.insert(0,0)

    drinkCost.set(0.0)
    mealCost.set(0.0)
    roomCost.set(0.0)
    devCost.set(0.0)
    serviceFee.set(0.0)
    totalCost.set(0.0)
    chkb1.set(0)
    v.set(3)

##################clear control button###############
def clearControlBtn():
    Display.delete(0,END)
    drinkCost.set('')
    mealCost.set('')
    roomCost.set('')
    devCost.set('')
    serviceFee.set('')
    totalCost.set('')

##################exit control button###############
def destroy():
    root.destroy()

def exitControlBtn():
    Display.delete(0,END)
    Display.insert(0,'Thank you....')
    Display.after(3000, destroy)

root = Tk()

#setting screen size
width=1100
height=700
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(width=False, height=False)
root .title("Hotel Management System")

#windows partition
Tops = Frame(root, width=1100, height=100, bg='blue', relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=600, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=500, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

f3 = Frame(root, width=20, height=700, relief=SUNKEN)
f3.pack(side=LEFT)

f4 = Frame(root, width=250, height=700, relief=SUNKEN)
f4.pack(side=LEFT)

#main window
txt_input = StringVar(value='Fuck you bitch...')
Display = Entry(Tops, font=('arial', 80, 'bold'), fg='white', bd=50, bg='blue', justify='right', textvariable=txt_input )
Display.grid(columnspan=2)

#setting date and time
localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(f2,font=('arial', 20, 'bold'),text=localtime,fg='dark blue',bd=10,anchor=W)
lblInfo.grid(row=0,column=1,columnspan=4)

#buliding calculator
operator=''
#########row1################
btn7=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='7',command=lambda:calcBtn(7)).grid(row=2,column=1)
btn8=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='8',command=lambda:calcBtn(8)).grid(row=2,column=2)
btn9=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='9',command=lambda:calcBtn(9)).grid(row=2,column=3)
btnC=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='C',bg='green',command=clear).grid(row=2,column=4)
#########row2###############
btn4=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='4',command=lambda:calcBtn(4)).grid(row=3,column=1)
btn5=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='5',command=lambda:calcBtn(5)).grid(row=3,column=2)
btn6=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='6',command=lambda:calcBtn(6)).grid(row=3,column=3)
btnplus=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='+',bg='green',command=lambda:calcBtn('+')).grid(row=3,column=4)
#########row3################
btn1=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='1',command=lambda:calcBtn(1)).grid(row=4,column=1)
btn2=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='2',command=lambda:calcBtn(2)).grid(row=4,column=2)
btn3=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='3',command=lambda:calcBtn(3)).grid(row=4,column=3)
btnminus=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='-',bg='green',command=lambda:calcBtn('-')).grid(row=4,column=4)
#########row4################
btn0=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='0',command=lambda:calcBtn(0)).grid(row=5,column=1)
btndot=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='.',bg='orange',command=lambda:calcBtn('.')).grid(row=5,column=2)
btndivision=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='/',bg='orange',command=lambda:calcBtn('/')).grid(row=5,column=3)
btnmultiply=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='*',bg='green',command=lambda:calcBtn('*')).grid(row=5,column=4)
#########row5###############
btnequals=Button(f2,padx=48,pady=2,bd=8,font=('arial',20,'bold'),text='=',bg='green',command=equals).grid(row=6,column=1,columnspan=2)
btnopenbracket=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='(',bg='orange',command=lambda:calcBtn('(')).grid(row=6,column=3)
btnclosebracket=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text=')',bg='green',command=lambda:calcBtn(')')).grid(row=6,column=4)

########choose meal#########
mealQty=IntVar()
mealDicator=StringVar(value='Delicious Meal')

lblMeal=Label(f1,font=('arial',16,'bold'),text='Choose Meal',bd=10,anchor=W)
lblMeal.grid(row=0,column=0)

txtMeal=ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=mealDicator)
txtMeal['values']=('Fried Rice', 'Biryani', 'Tandoori', 'Shawarma')
txtMeal.grid(row=0,column=1)

lblQtMeal=Label(f1,font=('arial',16,'bold'),text='Qty. of Meal',bd=10,anchor=W)
lblQtMeal.grid(row=1,column=0)
txtQtyMeal=Entry(f1,font=('arial',16,'bold'),textvariable=mealQty,bd=10,insertwidth=2,bg='white',justify='right')
txtQtyMeal.grid(row=1,column=1)

########choose drink#########
drinkQty=IntVar()
drinkDicator=StringVar(value='Drinks')

lblDrink=Label(f1,font=('arial',16,'bold'),text='Choose Drinks',bd=10,anchor=W)
lblDrink.grid(row=2,column=0)

txtDrink=ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=drinkDicator)
txtDrink['values']=('Coke', 'Pepsi', 'Lemonide', 'Water')
txtDrink.grid(row=2,column=1)

lblQtDrink=Label(f1,font=('arial',16,'bold'),text='Qty. of Drink',bd=10,anchor=W)
lblQtDrink.grid(row=3,column=0)

txtQtyDrink=Entry(f1,font=('arial',16,'bold'),textvariable=drinkQty,bd=10,insertwidth=2,bg='white',justify='right')
txtQtyDrink.grid(row=3,column=1)

###########Order delivery###############
chkb1=IntVar()
lblHomeDev=Label(f1,font=('arial',16,'bold'),text='Order delivery',bd=10,anchor=W)
lblHomeDev.grid(row=4,column=0)
check1=Checkbutton(f1,text='Yes',variable=chkb1,font=('arial',16,'bold'))
check1.grid(row=4,column=1)

##########Book your room###########
v=IntVar()
v.set(3)
lblRoom=Label(f1,font=('arial',16,'bold'),text='Book a room',bd=10,anchor=W)
lblRoom.grid(row=5,column=0)

myRadios = Radiobutton(f1,text='VIP',font=('arial',16,'bold'),variable=v,value=1)
myRadios.grid(row=5,column=1,sticky=W)
myRadios = Radiobutton(f1,text='Normal',font=('arial',16,'bold'),variable=v,value=2)
myRadios.grid(row=5,column=1)
myRadios = Radiobutton(f1,text='No',font=('arial',16,'bold'),variable=v,value=3)
myRadios.grid(row=5,column=1,sticky=E)

##############cost display screens######################
mealCost=StringVar()
lblMeal1=Label(f1,font=('arial',16,'bold'),text='Cost of Meal($)',bd=16,anchor=W)
lblMeal1.grid(row=0,column=2)
txtMeal1=Entry(f1,font=('arial',16,'bold'),textvariable=mealCost,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
txtMeal1.grid(row=0,column=3)

drinkCost=StringVar()
lblDrink1=Label(f1,font=('arial',16,'bold'),text='Cost of Drink($)',bd=16,anchor=W)
lblDrink1.grid(row=1,column=2)
txtDrink1=Entry(f1,font=('arial',16,'bold'),textvariable=drinkCost,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
txtDrink1.grid(row=1,column=3)

devCost=StringVar()
lblDev=Label(f1,font=('arial',16,'bold'),text='Cost of Delivery($)',bd=16,anchor=W)
lblDev.grid(row=2,column=2)
txtDev=Entry(f1,font=('arial',16,'bold'),textvariable=devCost,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
txtDev.grid(row=2,column=3)

roomCost=StringVar()
lblRoom=Label(f1,font=('arial',16,'bold'),text='Cost of Room($)',bd=16,anchor=W)
lblRoom.grid(row=3,column=2)
txtRoom=Entry(f1,font=('arial',16,'bold'),textvariable=roomCost,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
txtRoom.grid(row=3,column=3)

serviceFee=StringVar()
lblServiceFee=Label(f1,font=('arial',16,'bold'),text='Service Fee($)',bd=16,anchor=W)
lblServiceFee.grid(row=4,column=2)
txtServiceFee=Entry(f1,font=('arial',16,'bold'),textvariable=serviceFee,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
txtServiceFee.grid(row=4,column=3)

totalCost=StringVar()
lblTotal=Label(f1,font=('arial',16,'bold'),text='Total($)',bd=16,anchor=W)
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=totalCost,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
txtTotal.grid(row=5,column=3)

############currency converter#####################
currenyConv=IntVar()
indicator=StringVar(value='Choose a Country')
cunConvLbl='------------------------------------------Currency Converter---------------------------------------------'

lblCunCon=Label(f1,font=('arial',16,'bold italic'),text=cunConvLbl,bd=20,anchor=W)
lblCunCon.grid(row=6,column=0,columnspan=4)

lblCountry=Label(f1,font=('arial',16,'bold'),text='Nationality',bd=20,anchor=W)
lblCountry.grid(row=7,column=0)

txtCountry=ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=indicator)
txtCountry['values']=('China', 'France', 'Ghana', 'Mexico', 'Nigeria', 'USA')
txtCountry.grid(row=7,column=1)

lblAmount=Label(f1,font=('arial',16,'bold'),text='Amount($)',bd=20,anchor=W)
lblAmount.grid(row=7,column=2)
txtAmount=Entry(f1,font=('arial',16,'bold'),textvariable=currenyConv,bd=10,insertwidth=4,bg='white',justify='right')
txtAmount.grid(row=7,column=3)

####################control buttons###################
btnConvert=Button(f1,padx=8,pady=4,bd=16,fg='white',font=('arial',20,'bold'),width=10,text='Convert',bg='orange',command=currencyConvert).grid(row=8,column=2)

btnTotal=Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',20,'bold'),width=10,text='Total',bg='orange',command=totalControlBtn).grid(row=1,column=0)
btnClear=Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',20,'bold'),width=10,text='Clear',bg='orange',command=clearControlBtn).grid(row=2,column=0)
btnReset=Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',20,'bold'),width=10,text='Reset',bg='orange',command=resetControlBtn).grid(row=3,column=0)
btnExit=Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',20,'bold'),width=10,text='Exit',bg='orange',command=exitControlBtn).grid(row=4,column=0)

#####################adding logo#######################
photo=PhotoImage(file='')
myphoto=Label(f1,image=photo)
myphoto.grid(row=8,column=0)

#################scrollable text#######################
scroll_text=StringVar()
txtScroll=Entry(f2, textvariable=scroll_text, font=('arial',15,'bold'), fg='white', bd=10, bg='blue', width=28)
txtScroll.grid(row=1,column=1,columnspan=4)
scrollText()

root.mainloop()