from tkinter import*
import random
from datetime import datetime

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Bill Master")

timeFrame = Frame(root, bg="#49ADA8", width=1800, height=40, relief=GROOVE)
timeFrame.pack(side=TOP)

frame1 = Frame(root, width=1000, height=800, relief=GROOVE)
frame1.pack(side=LEFT,  ipadx=500,
    ipady=10)

frame2 = Frame(root, width=500, height=800, relief=GROOVE)
frame2.pack(side=RIGHT)

# Show the current date and time
now = datetime.now()
currentDateTime = now.strftime("%d/%m/%Y %H:%M:%S")

label = Label(timeFrame, font=('Arial', 25, 'bold'),
              text="Restaurant Bill Master", fg="#49ADA8", bd=10, anchor='w')
label.grid(row=0, column=0)

label = Label(timeFrame, font=('Arial', 15),
              text=currentDateTime, fg="#286590", anchor='w')
label.grid(row=1, column=0)


def Ref():
    x = random.randint(12980, 50876)
  
def exitApp():
    root.destroy()

def reset():
   
    Cost.set("")


rand = StringVar()
BerlinerWeisse = StringVar()
ChimayRed = StringVar()
BalticPorter = StringVar()
CreamAle = StringVar()
GermanPilsner = StringVar()
Subtotal = StringVar()
Total = StringVar()
ServiceFee = StringVar()
BlondeAle = StringVar()
VATTax = StringVar()
Cost = StringVar()


lblreference = Label(frame1, font=('aria', 15, 'bold'),
                     text="Order No.", fg="#286590", bd=10, anchor='w')
lblreference.grid(row=0, column=0)
txtreference = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=rand,
                     bd=6, insertwidth=4, bg="#286590", justify='right')
txtreference.grid(row=0, column=1)

berlinerlbl = Label(frame1, font=('Arial', 15, 'bold'),
                    text="Berliner Weisse", fg="#286590", bd=10, anchor='w')
berlinerlbl.grid(row=1, column=0)
berlinertxt = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=BerlinerWeisse,
                 bd=6, insertwidth=4, bg="#286590", justify='right')
berlinertxt.grid(row=1, column=1)

chimaylbl = Label(frame1, font=('aria', 15, 'bold'),
                      text="Chimay Red", fg="#286590", bd=10, anchor='w')
chimaylbl.grid(row=2, column=0)
chimaytxt = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=ChimayRed,
                      bd=6, insertwidth=4, bg="#286590", justify='right')
chimaytxt.grid(row=2, column=1)


balticlbl = Label(frame1, font=('aria', 15, 'bold'),
                  text="Baltic Porter", fg="#286590", bd=10, anchor='w')
balticlbl.grid(row=3, column=0)
txtburger = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=BalticPorter,
                  bd=6, insertwidth=4, bg="#286590", justify='right')
txtburger.grid(row=3, column=1)

creamlbl = Label(frame1, font=('aria', 15, 'bold'),
                 text="Cream Ale", fg="#286590", bd=10, anchor='w')
creamlbl.grid(row=4, column=0)
creamtxt = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=CreamAle,
                 bd=6, insertwidth=4, bg="#286590", justify='right')
creamtxt.grid(row=4, column=1)

germanlbl = Label(frame1, font=(
    'aria', 15, 'bold'), text="German Pilsner", fg="#286590", bd=10, anchor='w')
germanlbl.grid(row=5, column=0)
germantxt = Entry(frame1, font=('ariel', 17, 'bold'),
                         textvariable=GermanPilsner, bd=6, insertwidth=4, bg="#286590", justify='right')
germantxt.grid(row=5, column=1)

blondelbl = Label(frame1, font=('aria', 15, 'bold'),
                  text="Blonde Ale", fg="#286590", bd=10, anchor='w')
blondelbl.grid(row=0, column=2)
blondtxt = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=BlondeAle,
                  bd=6, insertwidth=4, bg="#286590", justify='right')
blondtxt.grid(row=0, column=3)

lblcost = Label(frame1, font=('aria', 15, 'bold'),
                text="Cost", fg="#286590", bd=10, anchor='w')
lblcost.grid(row=1, column=2)
txtcost = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=Cost,
                bd=6, insertwidth=4, bg="#286590", justify='right')
txtcost.grid(row=1, column=3)

servicelbl = Label(frame1, font=(
    'aria', 15, 'bold'), text="Service Fee", fg="#286590", bd=10, anchor='w')
servicelbl.grid(row=2, column=2)
servicetxt = Entry(frame1, font=('ariel', 17, 'bold'),
                          textvariable=ServiceFee, bd=6, insertwidth=4, bg="#286590", justify='right')
servicetxt.grid(row=2, column=3)

lblTax = Label(frame1, font=('aria', 15, 'bold'),
               text="VAT Tax", fg="#286590", bd=10, anchor='w')
lblTax.grid(row=3, column=2)
txtTax = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=VATTax,
               bd=6, insertwidth=4, bg="#286590", justify='right')
txtTax.grid(row=3, column=3)

lblSubtotal = Label(frame1, font=('aria', 15, 'bold'),
                    text="Subtotal", fg="#286590", bd=10, anchor='w')
lblSubtotal.grid(row=4, column=2)
txtSubtotal = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=Subtotal,
                    bd=6, insertwidth=4, bg="#286590", justify='right')
txtSubtotal.grid(row=4, column=3)

lblTotal = Label(frame1, font=('aria', 15, 'bold'),
                 text="Total", fg="#286590", bd=10, anchor='w')
lblTotal.grid(row=5, column=2)
txtTotal = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=Total,
                 bd=6, insertwidth=4, bg="#286590", justify='right')
txtTotal.grid(row=5, column=3)


lblTotal = Label(frame1, text="---------------------", fg="white")
lblTotal.grid(row=6, columnspan=3)

btnTotal = Button(frame1, padx=16, pady=8, bd=10, fg="black", font=(
    'ariel', 17, 'bold'), width=10, text="Total Bill", bg="#286590", command=Ref)
btnTotal.grid(row=7, column=1)

btnreset = Button(frame1, padx=16, pady=8, bd=10, fg="black", font=(
    'ariel', 17, 'bold'), width=10, text="Reset Bill", bg="#286590", command=reset)
btnreset.grid(row=7, column=2)

btnexit = Button(frame1, padx=16, pady=8, bd=10, fg="black", font=(
    'ariel', 17, 'bold'), width=10, text="Exit", bg="#286590", command=exitApp)
btnexit.grid(row=7, column=3)


def priceListing():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price Listing")
    
    roo.mainloop()


pricelistingbtn = Button(frame1, padx=16, pady=8, bd=10, fg="black", font=(
    'ariel', 16, 'bold'), width=10, text="Price Listing", bg="#286590", command=priceListing)
pricelistingbtn.grid(row=7, column=0)

root.mainloop()
