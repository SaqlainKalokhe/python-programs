from ast import operator
from cgitb import reset
from hmac import compare_digest
from tkinter import *
from tkinter import filedialog
import time
from turtle import clear
import random
from numpy import save
from tkinter import messagebox


root=Tk()
root.geometry('1390x690+0+0')
root.resizable(0,0)
root.title('Restaurant Management System')

root.config(bg='firebrick4')


# frames
TopFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
TopFrame.pack(side=TOP)
labelTitle=Label(TopFrame,text='Restaurant Management System',font=('fantasy',30,'bold'),fg='white',bd=10,bg='red4',width=45)
labelTitle.grid(row=0,column=0)
# menu_frame
MenuFrame=Frame(root,bd=10,relief=RIDGE,bg='red4')
MenuFrame.pack(side=LEFT)

# cost_frame
CostFrame=Frame(MenuFrame,bd=4,relief=RIDGE,bg='red4',pady=10)
CostFrame.pack(side=BOTTOM)

# Food_frame
FoodFrame=LabelFrame(MenuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
FoodFrame.pack(side=LEFT)

# Drink_frame
drinksFrame=LabelFrame(MenuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

# Desert_frame
desertFrame=LabelFrame(MenuFrame,text='Desert',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
desertFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

# functions 
def totalcost():
    global priceofFood,priceofDrinks,priceofCakes
    global subtotalofItem
    
    item1 = int(e_roti.get())
    item2 = int(e_daal.get())
    item3 = int(e_fish.get())
    item4 = int(e_sabji.get())
    item5 = int(e_kebab.get())
    item6 = int(e_chawal.get())
    item7 = int(e_mutton.get())
    item8 = int(e_paneer.get())
    item9 = int(e_chicken.get())
    
    item10 = int(e_lassi.get())
    item11 = int(e_coffee.get())
    item12 = int(e_faluda.get())
    item13 = int(e_shikanji.get())
    item14 = int(e_jaljeera.get())
    item15 = int(e_roohafza.get())
    item16 = int(e_masalatea.get())
    item17 = int(e_badammilk.get())
    item18 = int(e_coldrinks.get())

    item19 = int(e_oreo.get())
    item20 = int(e_baklawa.get())
    item21 = int(e_kitkatcake.get())
    item22 = int(e_vanillacake.get())
    item23 = int(e_bananacake.get())
    item24 = int(e_browniecake.get())
    item25 = int(e_fruit.get())
    item26 = int(e_hotchocolate.get())
    item27 = int(e_blackforest.get())

    priceofFood=(item1*10)+(item2*60)+(item3*10)+(item4*50)+ (item5*40) + (item6 * 30) + (item7 * 120) + (item8 * 100) + (item9 * 120)

    priceofDrinks=(item10*50)+(item11*40)+ (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) + (item16 * 20) + (item17 * 50) + (item18 * 80)

    priceofCakes=(item19*400)+(item20*500)+ (item21 * 500) + (item22 * 550) + (item23 * 450) + (item24 * 800) + (item25 * 620) + (item26 * 700) + (item27 * 550)

    costoffoodvar.set(str(priceofFood)+ ' Rs')
    costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
    costofcakesvar.set(str(priceofCakes)+ ' Rs')


    subtotalofItem=priceofFood+priceofCakes+priceofDrinks
    subtotalvar.set(str(subtotalofItem)+ ' Rs')
    
    servicetaxvar.set('50 Rs')
    
    totalcost = subtotalofItem + 50
    totalcostvar.set(str(totalcost)+ ' Rs')
    

# def totalcost():
    
    
    
def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    elif var1.get() == 0:
        textroti.config(state=DISABLED)
        e_roti.set('0')
        

def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()

    elif var2.get() == 0:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()

    elif var3.get() == 0: 
        textfish.config(state=DISABLED)
        e_fish.set('0')
        

def sabji():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.delete(0,END)
        textsabji.focus()
    elif var4.get() == 0:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')
        


def kebab():
    if var5.get() == 1:
        textkebab.config(state=NORMAL)
        textkebab.delete(0,END)
        textkebab.focus()
    elif var5.get() == 0:
        textkebab.config(state=DISABLED)
        e_kebab.set('0')
        


def chawal():
    if var6.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.delete(0,END)
        textchawal.focus()
    elif var6.get() == 0:
        textchawal.config(state=DISABLED)
        e_chawal('0')
        
        


def mutton():
    if var7.get() == 1:
        textmutton.config(state=NORMAL)
        textmutton.delete(0,END)
        textmutton.focus()
    elif var7.get() == 0:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')
        


def paneer():
    if var8.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    elif var8.get() == 0:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')
        


def chicken():
    if var9.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.delete('0')
        textchicken.focus()
    elif var9.get() == 0:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')
        
        


def lassi():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    elif var10.get() == 0:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')
       


def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')
        


def faluda():
    if var12.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    elif var12.get() == 0:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')
        


def shikanji():
    if var13.get() == 1:
        textshikanji.config(state=NORMAL)
        textshikanji.delete(0,END)
        textshikanji.focus()
    elif var13.get() == 0:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')
        


def jaljeera():
    if var14.get() == 1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0,END)
        textjaljeera.focus()
    elif var14.get() == 0:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')
        


def roohafza():
    if var15.get() == 1:
        textroohafza.config(state=NORMAL)
        textroohafza.delete(0,END)
        textroohafza.focus()
    elif var15.get() == 0:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')
        


def masalatea():
    if var16.get() == 1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.delete(0,END)
        textmasalatea.focus()
    elif var16.get() == 0:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')
        


def badammilk():
    if var17.get() == 1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.delete(0,END)
        textbadammilk.focus()
    elif var17.get() == 0:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')
        


def colddrinks():
    if var18.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.delete(0,END)
        textcolddrinks.focus()
    elif var18.get() == 0:
        textcolddrinks.config(state=DISABLED)
        e_coldrinks('0')
        


def oreocake():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    elif var19.get() == 0:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')


def baklawacake():
    if var20.get() == 1:
        textbaklawa.config(state=NORMAL)
        textbaklawa.delete(0,END)
        textbaklawa.focus()
    elif var20.get() == 0:
        textbaklawa.config(state=DISABLED)
        e_baklawa.set('0')
       


def kitkatcake():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    elif var21.get() == 0:
        textkitkat.config(state=DISABLED)
        e_kitkatcake.set('0')
        


def vanillacake():
    if var22.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    elif var22.get() == 0:
        textvanilla.config(state=DISABLED)
        e_vanillacake.set('0')


def bananacake():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0,END)
        textbanana.focus()
    elif var23.get() == 0:
        textbanana.config(state=DISABLED)
        e_bananacake.set('0')


def browniecake():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
        e_browniecake.set('0')
       


def fruit():
    if var25.get() == 1:
        textfruit.config(state=NORMAL)
        textfruit.delete(0,END)
        textfruit.focus()
    elif var25.get() == 0:
        textfruit.config(state=DISABLED)
        e_fruit.set('0')
        


def hotchocolate():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    elif var26.get() == 0:
        textchocolate.config(state=DISABLED)
        e_hotchocolate.set('0')
        


def blackforest():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0,END)
        textblackforest.focus()
    elif var27.get() == 0:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')
        
        
#save button's function
def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    
    bill_data=textReceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Note','Your Bill Is Succesfully Saved')
        
# receipt 
def receipt():
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_roti.get()!='0':
            textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')

        if e_daal.get()!='0':
            textReceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*60}\n\n')

        if e_fish.get()!='0':
            textReceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*100}\n\n')

        if e_chawal.get() != '0':
            textReceipt.insert(END, f'Chawal:\t\t\t{int(e_chawal.get()) * 30}\n\n')

        if e_sabji.get() != '0':
            textReceipt.insert(END, f'Sabji:\t\t\t{int(e_sabji.get()) * 50}\n\n')

        if e_paneer.get() != '0':
            textReceipt.insert(END, f'Paneer:\t\t\t{int(e_paneer.get()) * 100}\n\n')

        if e_kebab.get() != '0':
            textReceipt.insert(END, f'Kebab:\t\t\t{int(e_kebab.get()) * 40}\n\n')

        if e_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 120}\n\n')

        if e_mutton.get() != '0':
            textReceipt.insert(END, f'Mutton:\t\t\t{int(e_mutton.get()) * 120}\n\n')

        if e_lassi.get() != '0':
            textReceipt.insert(END, f'Lassi:\t\t\t{int(e_lassi.get()) * 50}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffee.get()) * 40}\n\n')

        if e_faluda.get() != '0':
            textReceipt.insert(END, f'Faluda:\t\t\t{int(e_faluda.get()) * 80}\n\n')

        if e_shikanji.get() != '0':
            textReceipt.insert(END, f'Shikanji:\t\t\t{int(e_shikanji.get()) * 30}\n\n')

        if e_jaljeera.get() != '0':
            textReceipt.insert(END, f'Jaljeera:\t\t\t{int(e_jaljeera.get()) * 40}\n\n')

        if e_roohafza.get() != '0':
            textReceipt.insert(END, f'Roohafza:\t\t\t{int(e_roohafza.get()) * 60}\n\n')

        if e_masalatea.get() != '0':
            textReceipt.insert(END, f'Masala Chai:\t\t\t{int(e_masalatea.get()) * 20}\n\n')

        if e_badammilk.get() != '0':
            textReceipt.insert(END, f'Badam Milk:\t\t\t{int(e_badammilk.get()) * 50}\n\n')

        if e_coldrinks.get() != '0':
            textReceipt.insert(END, f'Cold Drinks:\t\t\t{int(e_coldrinks.get()) * 80}\n\n')

        if e_oreo.get() != '0':
            textReceipt.insert(END, f'Oreo:\t\t\t{int(e_oreo.get()) * 400}\n\n')

        if e_baklawa.get() != '0':
            textReceipt.insert(END, f'Apple:\t\t\t{int(e_baklawa.get()) * 300}\n\n')

        if e_kitkatcake.get() != '0':
            textReceipt.insert(END, f'Kitkat:\t\t\t{int(e_kitkatcake.get()) * 500}\n\n')

        if e_bananacake.get() != '0':
            textReceipt.insert(END, f'Banana:\t\t\t{int(e_bananacake.get()) * 450}\n\n')

        if e_browniecake.get() != '0':
            textReceipt.insert(END, f'Brownie:\t\t\t{int(e_browniecake.get()) * 800}\n\n')

        if e_fruit.get() != '0':
            textReceipt.insert(END, f'Pineapple:\t\t\t{int(e_fruit.get()) * 620}\n\n')

        if e_hotchocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate:\t\t\t{int(e_hotchocolate.get()) * 700}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 550}\n\n')

        if e_vanillacake.get() != '0':
            textReceipt.insert(END, f'Vanilla:\t\t\t{int(e_vanillacake.get()) * 550}\n\n')

        textReceipt.insert(END,'***************************************************************\n')
        if costoffoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofcakesvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

        
        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItem}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItem+50}Rs\n\n')
        textReceipt.insert(END,'***************************************************************\n')
        
        
# reset button

def reset():
    textReceipt.delete(1.0,END)
    e_daal.set('0')
    e_roti.set('0')
    e_sabji.set('0')
    e_fish.set('0')
    e_kebab.set('0')
    e_chawal.set('0')
    e_mutton.set('0')
    e_paneer.set('0')
    e_chicken.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_roohafza.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_masalatea.set('0')
    e_badammilk.set('0')
    e_coldrinks.set('0')

    e_oreo.set('0')
    e_baklawa.set('0')
    e_kitkatcake.set('0')
    e_vanillacake.set('0')
    e_bananacake.set('0')
    e_browniecake.set('0')
    e_fruit.set('0')
    e_hotchocolate.set('0')
    e_blackforest.set('0')

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textkebab.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textchawal.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)

    textoreo.config(state=DISABLED)
    textbaklawa.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textfruit.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')



    
#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

# textvariable

e_roti=StringVar()
e_daal=StringVar()
e_sabji = StringVar()
e_chawal = StringVar()
e_fish = StringVar()
e_mutton = StringVar()
e_kebab = StringVar()
e_chicken = StringVar()
e_paneer = StringVar()

e_lassi=StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_shikanji = StringVar()
e_roohafza = StringVar()
e_jaljeera = StringVar()
e_masalatea = StringVar()
e_badammilk = StringVar()
e_coldrinks = StringVar()

e_oreo=StringVar()
e_baklawa = StringVar()
e_kitkatcake = StringVar()
e_vanillacake = StringVar()
e_bananacake = StringVar()
e_browniecake = StringVar()
e_fruit = StringVar()
e_hotchocolate = StringVar()
e_blackforest = StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_roti.set('0')
e_daal.set('0')
e_sabji.set('0')
e_fish.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_roohafza.set('0')
e_shikanji.set('0')
e_jaljeera.set('0')
e_masalatea.set('0')
e_badammilk.set('0')
e_coldrinks.set('0')

e_oreo.set('0')
e_baklawa.set('0')
e_kitkatcake.set('0')
e_vanillacake.set('0')
e_bananacake.set('0')
e_browniecake.set('0')
e_fruit.set('0')
e_hotchocolate.set('0')
e_blackforest.set('0')



##FOOD

roti=Checkbutton(FoodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(FoodFrame,text='Daal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(FoodFrame,text='Fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=fish)
fish.grid(row=2,column=0,sticky=W)

sabji=Checkbutton(FoodFrame,text='Sabji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=sabji)
sabji.grid(row=3,column=0,sticky=W)

kebab=Checkbutton(FoodFrame,text='kebab',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=kebab)
kebab.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(FoodFrame,text='Chawal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=chawal)
chawal.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(FoodFrame,text='Mutton',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=mutton)
mutton.grid(row=6,column=0,sticky=W)

paneer=Checkbutton(FoodFrame,text='Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=paneer)
paneer.grid(row=7,column=0,sticky=W)

chicken=Checkbutton(FoodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=chicken)
chicken.grid(row=8,column=0,sticky=W)

#Entry Fields for Food Items

textroti=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textfish=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textsabji = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sabji)
textsabji.grid(row=3, column=1)

textkebab = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kebab)
textkebab.grid(row=4, column=1)

textchawal = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chawal)
textchawal.grid(row=5, column=1)

textmutton = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mutton)
textmutton.grid(row=6, column=1)

textpaneer = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_paneer)
textpaneer.grid(row=7, column=1)

textchicken = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=8, column=1)

#Drinks

lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=faluda)
faluda.grid(row=2,column=0,sticky=W)

shikanji=Checkbutton(drinksFrame,text='Shikanji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=shikanji)
shikanji.grid(row=3,column=0,sticky=W)

jaljeera=Checkbutton(drinksFrame,text='Jaljeera',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=jaljeera)
jaljeera.grid(row=4,column=0,sticky=W)

roohafza=Checkbutton(drinksFrame,text='Roohafza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=roohafza)
roohafza.grid(row=5,column=0,sticky=W)

masalatea=Checkbutton(drinksFrame,text='Masala Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=masalatea)
masalatea.grid(row=6,column=0,sticky=W)

badammilk=Checkbutton(drinksFrame,text='Badam Milk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=badammilk)
badammilk.grid(row=7,column=0,sticky=W)

colddrinks=Checkbutton(drinksFrame,text='Cold Drinks',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=colddrinks)
colddrinks.grid(row=8,column=0,sticky=W)
#entry fields for drink items

textlassi = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=1)

textfaluda = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_faluda)
textfaluda.grid(row=2, column=1)

textshikanji = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_shikanji)
textshikanji.grid(row=3, column=1)

textjaljeera = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_jaljeera)
textjaljeera.grid(row=4, column=1)

textroohafza = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_roohafza)
textroohafza.grid(row=5, column=1)

textmasalatea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_masalatea)
textmasalatea.grid(row=6, column=1)

textbadammilk = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_badammilk)
textbadammilk.grid(row=7, column=1)

textcolddrinks = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coldrinks)
textcolddrinks.grid(row=8, column=1)

# Desert

oreocake=Checkbutton(desertFrame,text='Oreo Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=oreocake)
oreocake.grid(row=0,column=0,sticky=W)

baklawa=Checkbutton(desertFrame,text='Baklawa',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=baklawacake)
baklawa.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(desertFrame,text='Kitkat Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=kitkatcake)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(desertFrame,text='Vanilla Ice-cream',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=vanillacake)
vanillacake.grid(row=3,column=0,sticky=W)

bananacake=Checkbutton(desertFrame,text='Banana Milk Shake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=bananacake)
bananacake.grid(row=4,column=0,sticky=W)

browniecake=Checkbutton(desertFrame,text='Browniecake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=browniecake)
browniecake.grid(row=5,column=0,sticky=W)

fruit=Checkbutton(desertFrame,text='Fruit plate ',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=fruit)
fruit.grid(row=6,column=0,sticky=W)

hotchocolate=Checkbutton(desertFrame,text='Hot Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=hotchocolate)
hotchocolate.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(desertFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)

#entry fields for desert

textoreo = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=1)

textbaklawa = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_baklawa)
textbaklawa.grid(row=1, column=1)

textkitkat = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkatcake)
textkitkat.grid(row=2, column=1)

textvanilla = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanillacake)
textvanilla.grid(row=3, column=1)

textbanana = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_bananacake)
textbanana.grid(row=4, column=1)

textbrownie = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_browniecake)
textbrownie.grid(row=5, column=1)

textfruit = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_fruit)
textfruit.grid(row=6, column=1)

textchocolate = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_hotchocolate)
textchocolate.grid(row=7, column=1)

textblackforest = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)

#costlabels & entry fields

labelCostofFood=Label(CostFrame,text='Cost of Food',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1)

labelCostofDrinks=Label(CostFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1)

labelCostofCakes=Label(CostFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1)

labelSubTotal=Label(CostFrame,text='Sub Total',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3)

labelServiceTax=Label(CostFrame,text='Service Tax',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3)

labelTotalCost=Label(CostFrame,text='Total Cost',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=6,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=6,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=6,command=save)
buttonSave.grid(row=0,column=2)

# buttonsql=Button(buttonFrame,text='Database',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5)
# buttonsql.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=6,command=reset)
buttonReset.grid(row=0,column=4)
#textarea for receipt

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

# calculator
operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))  
    calculatorField.delete(0,END) 
    calculatorField.insert(0,result)
    operator='' 
  
    
    
calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='yellow',bg='pink',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='yellow',bg='firebrick4',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='yellow',bg='firebrick4',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='yellow',bg='firebrick4',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()