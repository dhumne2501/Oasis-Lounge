import mysql.connector as sqltor


from tkinter import*
import random
import time

root= Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")
root.configure( background='pink')



Tops = Frame(root,bg="pink",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'comic sans ms' ,30, 'bold' ),text="OASIS LOUNGE",fg="red4",bg="pink",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'comic sans ms' ,20, ),text=localtime,fg="red4",bg="pink",anchor=W)
lblinfo.grid(row=2,column=0)
lblinfo = Label(Tops, font=( 'comic sans ms' ,20, ),text="LUXURY BEYOND HEAVEN",fg="red4",bg="pink",anchor=W)
lblinfo.grid(row=1,column=0)

#---------------Calculator------------------
text_Input=StringVar()
operator =""

txtdisplay = Entry(f2,font=('comic sans ms' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="lavender",justify='right', state=DISABLED)
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*120
    costoflargefries = colfries*200
    costofburger = cob*250
    costoffilet = cofi*300
    costofcheeseburger = cochee*500
    costofdrinks = codr*80

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.05)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)
    
   # mycon=sqltor.connect(host='localhost', user='root', passwd='tiger', database='suhani', charset='utf8')
   
   
       
    #def showtotal():
       
    


def qexit():
    root.destroy()

def reset():
    rand.set("0")
    Fries.set("0")
    Largefries.set("0")
    Burger.set("0")
    Filet.set("0")
    Subtotal.set("0")
    Total.set("0")
    Service_Charge.set("0")
    Drinks.set("0")
    Tax.set("0")
    cost.set("0")
    Cheese_burger.set("0")


btn7=Button(f2,padx=16,pady=16,bd=4, fg="black",height=1, font=('comic sans ms', 18 ,'bold'),text="7",bg="lavender", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0,columnspan=1)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="8",bg="lavender", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1,columnspan=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="9",bg="lavender", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="+",bg="lavender", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="4",bg="lavender", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="5",bg="lavender", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="6",bg="lavender", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="-",bg="lavender", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="1",bg="lavender", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="2",bg="lavender", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="3",bg="lavender", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="*",bg="lavender", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="0",bg="lavender", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text="c",bg="lavender", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=1,width = 46,height=1, fg="black", font=('comic sans ms',7 ,'bold'),text="=",bg="lavender",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 18 ,'bold'),text=".",bg="lavender", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('comic sans ms', 20 ,'bold'),text="/",bg="lavender", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)
status = Label(f2,font=('COMIC SANS MS', 15, 'bold'),width = 25, text="OISHIKI & SUHANI",bg="lavender",relief=SUNKEN)
status.grid(row=7,columnspan=4)

#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblreference = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="     Order No.    ",bg="pink",fg="maroon4",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('comic sans ms' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="lavender" ,justify='right', state=DISABLED)
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="  Breakfast Meal ",bg="pink",fg="maroon4",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('comic sans ms' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="lavender" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="    Lunch Meal    ",bg="pink",fg="maroon4",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('comic sans ms' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="lavender" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="   Evening Meal   ",bg="pink",fg="maroon4",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('comic sans ms' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="lavender" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="Swimming Package",bg="pink",fg="maroon4",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('comic sans ms' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="lavender" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="   Golf Package   ",bg="pink",fg="maroon4",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('comic sans ms' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="lavender" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="     Drinks      ",fg="maroon4",bg="pink",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('comic sans ms' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="lavender" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="       Cost      ",fg="maroon4",bg="pink",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('comic sans ms' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="lavender" ,justify='right', state=DISABLED)
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text=" Service Charge",bg="pink",fg="maroon4",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('comic sans ms' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="lavender" ,justify='right', state=DISABLED)
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="       Tax       ",fg="maroon4",bg="pink",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('comic sans ms' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="lavender" ,justify='right', state=DISABLED)
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="     Subtotal    ",bg="pink",fg="maroon4",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('comic sans ms' ,16,'bold'),textvariable=Subtotal , bd=6,insertwidth=4,bg="lavender" ,justify='right', state=DISABLED)
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'comic sans ms' ,16, 'bold' ),text="      Total       ",bg="pink",fg="maroon4",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('comic sans ms' ,16,'bold'),textvariable=Total , bd=6,insertwidth=4,bg="lavender" ,justify='right', state=DISABLED)
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
80
btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('comic sans ms' ,16,'bold'),width=10, text="TOTAL", bg="lavender",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('comic sans ms' ,16,'bold'),width=10, text="RESET", bg="lavender",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('comic sans ms' ,16,'bold'),width=10, text="EXIT", bg="lavender",command=qexit)
btnexit.grid(row=7, column=3)






def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    roo.configure(background="DeepPink4")
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'), text="SERVICE",bg="DeepPink4", fg="Turquoise1", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('comic sans ms', 15,'bold'),bg="DeepPink4", text="_____________", fg="DeepPink4", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'),bg="DeepPink4", text="PRICE", fg="Turquoise1", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'),bg="DeepPink4", text="Breakfast Meal", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'), bg="DeepPink4",text="120", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'), bg="DeepPink4",text="Lunch Meal", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'),bg="DeepPink4", text="200", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'),bg="DeepPink4", text="Evening Meal", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'), bg="DeepPink4",text="250", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'),bg="DeepPink4", text="Swimming Package", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'), bg="DeepPink4",text="300", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'),bg="DeepPink4", text="Golf Package", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'), bg="DeepPink4",text="500", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('comic mans ms', 15, 'bold'), bg="DeepPink4",text="Drinks", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('comic sans ms', 15, 'bold'),bg="DeepPink4", text="80", fg="CadetBlue2", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('comic sans ms' ,16,'bold'),width=10, text="PRICE", bg="lavender",command=price)
btnprice.grid(row=7, column=0,sticky="w")








rand.set("0")
Fries.set("0")
Largefries.set("0")
Burger.set("0")
Filet.set("0")
Subtotal.set("0")
Total.set("0")
Service_Charge.set("0")
Drinks.set("0")
Tax.set("0")
cost.set("0")
Cheese_burger.set("0")




def feed():
    ro = Tk()
    ro.geometry("1600x700+0+0")
    ro.title("FEEDBACK")
    ro.configure(background="azure")
    
    
    #name = StringVar()
    #fdbck = StringVar()
    
    lblinf = Label(ro, font=('comic sans ms', 15, 'bold'), text="      SINCE WE THRIVE TOWARDS PROVIDING BETTER SERVICES, YOUR KIND FEEDBACK WILL BE APPRECIATED",  bg="azure", fg="hot pink", bd=5)
    lblinf.grid(row=0, column=0)
    
    
    
    mycon=sqltor.connect(host='localhost', user='root', passwd='tiger', database='suhani', charset='utf8')
   
    
    def database():
        #name1=name.get()
        #fdbck1=fdbck.get()
        
        cursor=mycon.cursor()
        cursor.execute('create table if not exists feedback(NAME TEXT, FEEDBACK TEXT)')
        st="insert into feedback(NAME, FEEDBACK) values('{}','{}')".format('name','fdbck')
        cursor.execute(st)
        mycon.commit()
        
        
    
        
    
   
    namelbl = Label(ro, font=( 'comic sans ms' ,16),text="Enter name",bg="azure",fg="hot pink",bd=5,anchor='w')
    namelbl.grid(row=1,column=0)
    entername = Entry(ro,font=('comic sans ms',16),bd=6,insertwidth=5,bg="lavender")#textvariable=name)
    entername.grid(row=2,column=0)
        
    
   
    feedbacklbl = Label(ro, font=( 'comic sans ms' ,16 ),text="Enter feedback",bg="azure",fg="hot pink",bd=5,anchor='w')
    feedbacklbl.grid(row=3,column=0)
    enterfeedback = Entry(ro,font=('comic sans ms',16),bd=6,insertwidth=5,bg="lavender") #textvariable=fdbck)
    enterfeedback.grid(row=4,column=0)
    
    
    
    
        
        
        
  
    
  
    
    submitbtn=Button(ro,padx=16,pady=16,bd=4, fg="hot pink", font=('comic sans ms', 15 ,'bold'),text="SUBMIT",bg="azure",command=database)
    submitbtn.grid(row=5,column=0)
    
 
    
    
    
    

    
    ro.mainloop()
    
btnfd=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('comic sans ms' ,16,'bold'),width=10, text="FEEDBACK", bg="lavender",
             command=feed)
btnfd.grid(row=8, column=0)




root.mainloop()
