#!/usr/bin/env python3
import os
try:
    # Python2
    from Tkinter import * 
    import ttk
except ImportError:
    # Python3
    import tkinter as tk
    import tkinter.ttk as ttk
import time

class Main:
    def __init__(self, parent):
        #windows partition
        self.parent = parent
        self.Tops = Frame(parent, width=1100, height=100, bg='blue', relief=SUNKEN)
        self.Tops.pack(side=TOP)

        self.f1 = Frame(parent, width=600, height=700, relief=SUNKEN)
        self.f1.pack(side=LEFT)

        self.f2 = Frame(parent, width=500, height=700, relief=SUNKEN)
        self.f2.pack(side=RIGHT)

        self.f3 = Frame(parent, width=20, height=700, relief=SUNKEN)
        self.f3.pack(side=LEFT)

        self.f4 = Frame(parent, width=250, height=700, relief=SUNKEN)
        self.f4.pack(side=LEFT)

        #main window
        self.txt_input = StringVar(value='HOtem Management System')
        self.Display = Entry(self.Tops, font=('arial', 80, 'bold'), fg='white', bd=50, bg='blue', justify='right', textvariable=self.txt_input )
        self.Display.grid(columnspan=2)

        #setting date and time
        localtime = time.asctime(time.localtime(time.time()))
        lblInfo = Label(self.f2,font=('arial', 20, 'bold'),text=localtime,fg='dark blue',bd=10,anchor=W)
        lblInfo.grid(row=0,column=1,columnspan=4)

        #buliding calculator
        self.operator=''
        #########row1################
        btn7=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='7',command=lambda:self.calcBtn(7)).grid(row=2,column=1)
        btn8=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='8',command=lambda:self.calcBtn(8)).grid(row=2,column=2)
        btn9=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='9',command=lambda:self.calcBtn(9)).grid(row=2,column=3)
        btnC=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='C',bg='green',command=self.clear).grid(row=2,column=4)
        #########row2###############
        btn4=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='4',command=lambda:self.calcBtn(4)).grid(row=3,column=1)
        btn5=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='5',command=lambda:self.calcBtn(5)).grid(row=3,column=2)
        btn6=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='6',command=lambda:self.calcBtn(6)).grid(row=3,column=3)
        btnplus=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='+',bg='green',command=lambda:self.calcBtn('+')).grid(row=3,column=4)
        #########row3################
        btn1=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='1',command=lambda:self.calcBtn(1)).grid(row=4,column=1)
        btn2=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='2',command=lambda:self.calcBtn(2)).grid(row=4,column=2)
        btn3=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='3',command=lambda:self.calcBtn(3)).grid(row=4,column=3)
        btnminus=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='-',bg='green',command=lambda:self.calcBtn('-')).grid(row=4,column=4)
        #########row4################
        btn0=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='0',command=lambda:self.calcBtn(0)).grid(row=5,column=1)
        btndot=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='.',bg='orange',command=lambda:self.calcBtn('.')).grid(row=5,column=2)
        btndivision=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='/',bg='orange',command=lambda:self.calcBtn('/')).grid(row=5,column=3)
        btnmultiply=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='*',bg='green',command=lambda:self.calcBtn('*')).grid(row=5,column=4)
        #########row5###############
        btnequals=Button(self.f2,padx=48,pady=2,bd=8,font=('arial',20,'bold'),text='=',bg='green',command=self.equals).grid(row=6,column=1,columnspan=2)
        btnopenbracket=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='(',bg='orange',command=lambda:self.calcBtn('(')).grid(row=6,column=3)
        btnclosebracket=Button(self.f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text=')',bg='green',command=lambda:self.calcBtn(')')).grid(row=6,column=4)

        ########choose meal#########
        self.mealQty=IntVar()
        self.mealDicator=StringVar(value='Delicious Meal')

        lblMeal=Label(self.f1,font=('arial',16,'bold'),text='Choose Meal',bd=10,anchor=W)
        lblMeal.grid(row=0,column=0)

        txtMeal=ttk.Combobox(self.f1,font=('arial',16,'bold'),textvariable=self.mealDicator)
        txtMeal['values']=('Fried Rice', 'Biryani', 'Tandoori', 'Shawarma')
        txtMeal.grid(row=0,column=1)

        lblQtMeal=Label(self.f1,font=('arial',16,'bold'),text='Qty. of Meal',bd=10,anchor=W)
        lblQtMeal.grid(row=1,column=0)
        self.txtQtyMeal=Entry(self.f1,font=('arial',16,'bold'),textvariable=self.mealQty,bd=10,insertwidth=2,bg='white',justify='right')
        self.txtQtyMeal.grid(row=1,column=1)

        ########choose drink#########
        self.drinkQty=IntVar()
        self.drinkDicator=StringVar(value='Drinks')

        lblDrink=Label(self.f1,font=('arial',16,'bold'),text='Choose Drinks',bd=10,anchor=W)
        lblDrink.grid(row=2,column=0)

        txtDrink=ttk.Combobox(self.f1,font=('arial',16,'bold'),textvariable=self.drinkDicator)
        txtDrink['values']=('Coke', 'Pepsi', 'Lemonide', 'Water')
        txtDrink.grid(row=2,column=1)

        lblQtDrink=Label(self.f1,font=('arial',16,'bold'),text='Qty. of Drink',bd=10,anchor=W)
        lblQtDrink.grid(row=3,column=0)

        self.txtQtyDrink=Entry(self.f1,font=('arial',16,'bold'),textvariable=self.drinkQty,bd=10,insertwidth=2,bg='white',justify='right')
        self.txtQtyDrink.grid(row=3,column=1)

        ###########Order delivery###############
        self.chkb1=IntVar()
        lblHomeDev=Label(self.f1,font=('arial',16,'bold'),text='Order delivery',bd=10,anchor=W)
        lblHomeDev.grid(row=4,column=0)
        check1=Checkbutton(self.f1,text='Yes',variable=self.chkb1,font=('arial',16,'bold'))
        check1.grid(row=4,column=1)

        ##########Book your room###########
        self.v=IntVar()
        self.v.set(3)
        lblRoom=Label(self.f1,font=('arial',16,'bold'),text='Book a room',bd=10,anchor=W)
        lblRoom.grid(row=5,column=0)

        myRadios = Radiobutton(self.f1,text='VIP',font=('arial',16,'bold'),variable=self.v,value=1)
        myRadios.grid(row=5,column=1,sticky=W)
        myRadios = Radiobutton(self.f1,text='Normal',font=('arial',16,'bold'),variable=self.v,value=2)
        myRadios.grid(row=5,column=1)
        myRadios = Radiobutton(self.f1,text='No',font=('arial',16,'bold'),variable=self.v,value=3)
        myRadios.grid(row=5,column=1,sticky=E)

        ##############cost display screens######################
        self.mealCost=StringVar()
        lblMeal1=Label(self.f1,font=('arial',16,'bold'),text='Cost of Meal($)',bd=16,anchor=W)
        lblMeal1.grid(row=0,column=2)
        txtMeal1=Entry(self.f1,font=('arial',16,'bold'),textvariable=self.mealCost,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
        txtMeal1.grid(row=0,column=3)

        self.drinkCost=StringVar()
        lblDrink1=Label(self.f1,font=('arial',16,'bold'),text='Cost of Drink($)',bd=16,anchor=W)
        lblDrink1.grid(row=1,column=2)
        txtDrink1=Entry(self.f1,font=('arial',16,'bold'),textvariable=self.drinkCost,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
        txtDrink1.grid(row=1,column=3)

        self.devCost=StringVar()
        lblDev=Label(self.f1,font=('arial',16,'bold'),text='Cost of Delivery($)',bd=16,anchor=W)
        lblDev.grid(row=2,column=2)
        txtDev=Entry(self.f1,font=('arial',16,'bold'),textvariable=self.devCost,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
        txtDev.grid(row=2,column=3)

        self.roomCost=StringVar()
        lblRoom=Label(self.f1,font=('arial',16,'bold'),text='Cost of Room($)',bd=16,anchor=W)
        lblRoom.grid(row=3,column=2)
        txtRoom=Entry(self.f1,font=('arial',16,'bold'),textvariable=self.roomCost,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
        txtRoom.grid(row=3,column=3)

        self.serviceFee=StringVar()
        lblServiceFee=Label(self.f1,font=('arial',16,'bold'),text='Service Fee($)',bd=16,anchor=W)
        lblServiceFee.grid(row=4,column=2)
        txtServiceFee=Entry(self.f1,font=('arial',16,'bold'),textvariable=self.serviceFee,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
        txtServiceFee.grid(row=4,column=3)

        self.totalCost=StringVar()
        lblTotal=Label(self.f1,font=('arial',16,'bold'),text='Total($)',bd=16,anchor=W)
        lblTotal.grid(row=5,column=2)
        txtTotal=Entry(self.f1,font=('arial',16,'bold'),textvariable=self.totalCost,fg='white',bd=10,insertwidth=2,bg='blue',justify='right')
        txtTotal.grid(row=5,column=3)

        ############currency converter#####################
        self.currenyConv=IntVar()
        self.indicator=StringVar(value='Choose a Country')
        cunConvLbl='------------------------------------------Currency Converter---------------------------------------------'

        lblCunCon=Label(self.f1,font=('arial',16,'bold italic'),text=cunConvLbl,bd=20,anchor=W)
        lblCunCon.grid(row=6,column=0,columnspan=4)

        lblCountry=Label(self.f1,font=('arial',16,'bold'),text='Nationality',bd=20,anchor=W)
        lblCountry.grid(row=7,column=0)

        txtCountry=ttk.Combobox(self.f1,font=('arial',16,'bold'),textvariable=self.indicator)
        txtCountry['values']=('China', 'France', 'Ghana', 'Mexico', 'Nigeria', 'USA')
        txtCountry.grid(row=7,column=1)

        lblAmount=Label(self.f1,font=('arial',16,'bold'),text='Amount($)',bd=20,anchor=W)
        lblAmount.grid(row=7,column=2)
        self.txtAmount=Entry(self.f1,font=('arial',16,'bold'),textvariable=self.currenyConv,bd=10,insertwidth=4,bg='white',justify='right')
        self.txtAmount.grid(row=7,column=3)

        ####################control buttons###################
        btnConvert=Button(self.f1,padx=8,pady=4,bd=16,fg='white',font=('arial',20,'bold'),width=10,text='Convert',bg='orange',command=self.currencyConvert).grid(row=8,column=2)

        btnTotal=Button(self.f4,padx=10,pady=8,bd=16,fg='white',font=('arial',20,'bold'),width=10,text='Total',bg='orange',command=self.totalControlBtn).grid(row=1,column=0)
        btnClear=Button(self.f4,padx=10,pady=8,bd=16,fg='white',font=('arial',20,'bold'),width=10,text='Clear',bg='orange',command=self.clearControlBtn).grid(row=2,column=0)
        btnReset=Button(self.f4,padx=10,pady=8,bd=16,fg='white',font=('arial',20,'bold'),width=10,text='Reset',bg='orange',command=self.resetControlBtn).grid(row=3,column=0)
        btnExit=Button(self.f4,padx=10,pady=8,bd=16,fg='white',font=('arial',20,'bold'),width=10,text='Exit',bg='orange',command=self.exitControlBtn).grid(row=4,column=0)

        #####################adding logo#######################
        photo=PhotoImage(file='')
        myphoto=Label(self.f1,image=photo)
        myphoto.grid(row=8,column=0)

        #################scrollable text#######################
        self.scroll_text=StringVar()
        self.txtScroll=Entry(self.f2, textvariable=self.scroll_text, font=('arial',15,'bold'), fg='white', bd=10, bg='blue', width=28)
        self.txtScroll.grid(row=1,column=1,columnspan=4)
        self.scrollText()

    ##################scrolling text in textfield###############
    def scrollText(self):
        global text1,n,msg1
        msg1 = 'Hotel management system'
        msg2 = 'developed by python tkinter'
        text1 = ''
        n = 0

        for t in range(len(msg1)):
            for k in range(t):
                text1 += " "
            for g in range(len(msg1)-t):
                text1 += msg1[g]
            text1 = text1.strip()
            self.f2.update()
            self.f2.after(200)
            text1 = text1.strip()
            self.scroll_text.set('')
            self.scroll_text.set(text1)
            text1 = ''
        self.scroll_text.set('')
        self.txtScroll.after(200,self.scrollText)


    ##################calculator functions##############
    def calcBtn(self,numbers):
        # global self.operator
        self.operator=self.operator + str(numbers)
        self.txt_input.set(self.operator)

    def clear(self):
        # global operator
        self.operator=''
        self.txt_input.set('')
        self.Display.insert(0,'Start Calculating...')

    def equals(self):
        # global operator
        sumup=float(eval(self.operator))
        self.txt_input.set(sumup)
        self.operator=''

    ###################total btn function##################
    def totalControlBtn(self):
        #cost of meal
        selectedMeal=self.mealDicator.get()
        selectedMealQty=self.mealQty.get() 
        if selectedMeal == 'Fried Rice':
            self.mealCost.set(selectedMealQty*1.8)
        elif selectedMeal == 'Biryani':
            self.mealCost.set(selectedMealQty*3.7)
        elif selectedMeal == 'Tandoori':
            self.mealCost.set(selectedMealQty*4.7)
        elif selectedMeal == 'Shawarma':
            self.mealCost.set(selectedMealQty*5.7)
        else:
            self.mealCost.set(selectedMealQty*0.0)

        #cost of drink
        selectedDrink=self.drinkDicator.get()
        selectedDrinkQty=self.drinkQty.get() 
        if selectedDrink == 'Coke':
            self.drinkCost.set(selectedDrinkQty*1.8)
        elif selectedDrink == 'Pepsi':
            self.drinkCost.set(selectedDrinkQty*3.7)
        elif selectedDrink == 'Lemonide':
            self.drinkCost.set(selectedDrinkQty*4.7)
        elif selectedDrink == 'Water':
            self.drinkCost.set(selectedDrinkQty*5.7)
        else:
            self.drinkCost.set(selectedDrinkQty*0.0)

        #cost of delivery
        devCostMeal = float(self.mealCost.get())
        devCostDrink = float(self.drinkCost.get())
        deliveryCost = (devCostMeal + devCostDrink) * 0.5

        #room cost
        roomType = self.v.get()
        null = 0.0
        vipRoom = 10.0
        vipRoomDevCost = deliveryCost/(10*0.5)

        normalRoom = 5.0
        normalRoomDevCost = deliveryCost/(5*2.5)

        if roomType == 1:
            if self.chkb1.get() == 1:
                self.serviceFee.set(vipRoomDevCost)
                self.roomCost.set(10.0)
                self.devCost.set(deliveryCost)
            else:
                self.serviceFee.set(null)
                self.roomCost.set(10.0)
                self.devCost.set(null)
        elif roomType == 2:
            if self.chkb1.get() == 1:
                self.serviceFee.set(normalRoomDevCost)
                self.roomCost.set(5.0)
                self.devCost.set(deliveryCost)
            else:
                self.serviceFee.set(null)
                self.roomCost.set(5.0)
                self.devCost.set(null)
            
        elif roomType == 3:
            if self.chkb1.get() == 1:
                self.serviceFee.set(null)
                self.roomCost.set(null)
                self.devCost.set(null)
            else:
                self.serviceFee.set(null)
                self.roomCost.set(null)
                self.devCost.set(null)
            
        
        totalOrderCost = float(self.mealCost.get())+float(self.drinkCost.get())+float(self.roomCost.get())+float(self.devCost.get())+float(self.serviceFee.get())
        self.totalCost.set(totalOrderCost)
        displayTotal = "Total = $",totalOrderCost

        self.Display.delete(0,END)
        self.Display.insert(0,displayTotal)

        if self.totalCost.get() == '0.0':
            self.Display.delete(0,END)
            self.Display.insert(0,'Please, make an order')

    ###########currency converter method################
    def currencyConvert(self):
        currncy = self.currenyConv.get()
        selectedCountry = self.indicator.get()
        if selectedCountry == 'China':
            self.Display.delete(0,END)
            self.Display.insert(0, ('Yuan',(currncy*6.88)))
        elif selectedCountry == 'France':
            self.Display.delete(0,END)
            self.Display.insert(0, ('Euro',(currncy*0.81)))
        elif selectedCountry == 'Ghana':
            self.Display.delete(0,END)
            self.Display.insert(0, ('Cedi',(currncy*4.88)))
        elif selectedCountry == 'Mexico':
            self.Display.delete(0,END)
            self.Display.insert(0, ('MXN',(currncy*18.90)))
        elif selectedCountry == 'Nigeria':
            self.Display.delete(0,END)
            self.Display.insert(0, ('Naira',(currncy*361.01)))
        elif selectedCountry == 'USA':
            self.Display.delete(0,END)
            self.Display.insert(0, ('Dollar',(currncy*1.00)))
        else:
            self.Display.delete(0,END)
            self.Display.insert(0, 'Error:Select country')


    ##################reset control button###############
    def resetControlBtn(self):
        self.Display.delete(0,END)
        self.Display.insert(0,'System resetting.....')
        self.Display.after(1000,self.reset)

    def reset(self):
        self.clear()
        self.Display.delete(0,END)
        self.Display.insert(0,'Reset complete')
        self.mealDicator.set(value='Delicious Meal')
        self.drinkDicator.set(value='Drinks')
        self.indicator.set(value='')
        self.txtQtyDrink.delete(0,END)
        self.txtQtyDrink.insert(0,0)
        self.txtQtyMeal.delete(0,END)
        self.txtQtyMeal.insert(0,0)
        self.txtAmount.delete(0,END)
        self.txtAmount.insert(0,0)

        self.drinkCost.set(0.0)
        self.mealCost.set(0.0)
        self.roomCost.set(0.0)
        self.devCost.set(0.0)
        self.serviceFee.set(0.0)
        self.totalCost.set(0.0)
        self.chkb1.set(0)
        self.v.set(3)

    ##################clear control button###############
    def clearControlBtn(self):
        self.Display.delete(0,END)
        self.drinkCost.set('')
        self.mealCost.set('')
        self.roomCost.set('')
        self.devCost.set('')
        self.serviceFee.set('')
        self.totalCost.set('')

    ##################exit control button###############
    def destroy(self):
        self.parent.destroy()

    def exitControlBtn(self):
        self.Display.delete(0,END)
        self.Display.insert(0,'Thank you....')
        self.Display.after(3000, self.destroy)

        
root = Tk()
app=Main(root)
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

root.mainloop()