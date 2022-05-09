# Import the required packages
from tkinter import*
import random
from datetime import datetime
from tkinter import messagebox

# Initialize tkinter
root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Bill Master")

# Declare frame for date and time
timeFrame = Frame(root, bg="#49ADA8", width=1800, height=40, relief=GROOVE)
timeFrame.pack(side=TOP)
  
# Creating a photoimage object of the logo 
# and set the image on a button
logo = PhotoImage(file = r"rest_logo.png")
Button(root, image = logo).pack(side = TOP, pady = 10)


frame1 = Frame(root, width=1000, height=800, relief=GROOVE,
               highlightbackground="#49ADA8", highlightthickness=5)
frame1.pack(side=TOP, expand=YES)

frame2 = Frame(root, width=500, height=800, relief=GROOVE)

# Show the current date and time
now = datetime.now()
currentDateTime = now.strftime("%d/%m/%Y %H:%M:%S")

# Label for application name
label = Label(timeFrame, font=('Arial', 25, 'bold'),
              text="Restaurant Bill Master", fg="#49ADA8", bd=10, anchor='w')
label.grid(row=0, column=0)

# Label for date and time display
label = Label(timeFrame, font=('Arial', 15),
              text=currentDateTime, fg="#286590", anchor='w')
label.grid(row=1, column=0)

# Main application logic
def claculateOrderAmount():
    # Generate random number for Order Number
    order = random.randint(10000, 80000)
    generatedOrderNo = str(order)
    OrderNo.set(generatedOrderNo)

    # Get entries entered by the user
    BerlinerWeisseValue = BerlinerWeisse.get()
    ChimayRedValue = ChimayRed.get()
    BalticPorterValue = BalticPorter.get()
    CreamAleValue = CreamAle.get()
    GermanPilsnerValue = GermanPilsner.get()
    BlondeAleValue = BlondeAle.get()

# Initialize the cost values for the items
    BerlinerWeisseCost = ''
    ChimayRedCost = ''
    BalticPorterCost = ''
    CreamAleCost = ''
    GermanPilsnerCost = ''
    BlondeAleCost = ''
    message = ''

# Check if empty values are submitted or incorrect data type
# If empty value is passed, a message is displayed
# If a value is passed, the program checks if it is number
# If it is not, a message is
# If it is a number, the total cost for the item ordered is calculated
# By multiplied by the total quantity ordered and the price for the item 
    if (len(BerlinerWeisseValue) == 0):
        message = 'Berline Weisse quanity cannot be empty'
        BerlinerWeisseCost = 0.00
    else:
        if(BerlinerWeisseValue.isnumeric()):
            BerlinerWeisseQuantity = float(BerlinerWeisse.get())
            BerlinerWeisseCost = BerlinerWeisseQuantity * 80.00
        else:
             message = 'Berline Weisse quanity must be a number'
             BerlinerWeisseCost = 0.00

    if len(ChimayRedValue) == 0:
        message = 'Chimay Red cannot be empty'
        ChimayRedCost = 0.00
    else:
        if(ChimayRedValue.isnumeric()):
            ChimayRedQuantity = float(ChimayRed.get())
            ChimayRedCost = ChimayRedQuantity * 60.00
        else:
             message = 'Chimay Red quanity must be a number'
             ChimayRedCost = 0.00

    if len(BalticPorterValue) == 0:
        message = 'Baltic Porter quantity cannot be empty'
        BalticPorterCost = 0.00
    else:
        if(BalticPorterValue.isnumeric()):
            BalticPorterQuantity = float(BalticPorter.get())
            BalticPorterCost = BalticPorterQuantity * 75.00
        else:
             message = 'Baltic Porter quanity must be a number'
             BalticPorterCost = 0.00

    if len(CreamAleValue) == 0:
        message = 'Cream Ale quantity cannot be empty'
        CreamAleCost = 0.00
    else:
        if(CreamAleValue.isnumeric()):
            CreamAleQuantity = float(CreamAle.get())
            CreamAleCost = CreamAleQuantity * 45.00
        else:
             message = 'Cream Ale quanity must be a number'
             CreamAleCost = 0.00

    if len(GermanPilsnerValue) == 0:
        message = 'German Pilsner quantity cannot be empty'
        GermanPilsnerCost = 0.00
    else:
        if(GermanPilsnerValue.isnumeric()):
           GermanPilsnerQuantity = float(GermanPilsner.get())
           GermanPilsnerCost = GermanPilsnerQuantity * 89.00
        else:
             message = 'German Pilsner quanity must be a number'
             GermanPilsnerCost = 0.00

    if len(BlondeAleValue) == 0:
        message = 'Blonde Ale quantity cannot be empty'
        BlondeAleCost = 0.00
    else:
        if(BlondeAleValue.isnumeric()):
          BlondeAleQuantity = float(BlondeAle.get())
          BlondeAleCost = BlondeAleQuantity * 68.00
        else:
             message = 'Blonde Ale quanity must be a number'
             BlondeAleCost = 0.00
    message = 'Bill generated successfully'
    # Calculate the total costs for the items
    TotalOrderCost = str('%.2f' % (BerlinerWeisseCost + ChimayRedCost + BalticPorterCost + CreamAleCost + GermanPilsnerCost + BalticPorterCost + BlondeAleCost))
    
    # Calculate tax amount (16% of the total costs of items)
    VATTaxAmount = 0.16 * float(TotalOrderCost)

     # Calculate service fee amount (0.5% of the total costs of items)
    ServiceFeeAmount = 0.005 * float(TotalOrderCost)

    # Calculate total order cost
    TotalCost = float(TotalOrderCost) + \
        float(VATTaxAmount) + float(ServiceFeeAmount)

    # Set the values of the computations
    ServiceFee.set('%.2f' % (ServiceFeeAmount))
    Cost.set(TotalOrderCost)
    VATTax.set('%.2f' % (VATTaxAmount))
    Subtotal.set(TotalOrderCost)
    Total.set('%.2f' % (TotalCost))

    # Show error message
    messagebox.showinfo('message', message)

# Exit the application
def exitApp():
    root.destroy()

# Reset the entries
# Clears all the entries
def resetBill():
    OrderNo.set("")
    BerlinerWeisse.set("")
    ChimayRed.set("")
    BalticPorter.set("")
    CreamAle.set("")
    GermanPilsner.set("")
    Subtotal.set("")
    Total.set("")
    ServiceFee.set("")
    BlondeAle.set("")
    VATTax.set("")
    Cost.set("")

# Initialize the variables for the entries
OrderNo = StringVar() # Holds the Order Number 
BerlinerWeisse = StringVar()  # Holds the quantity of BerlinerWeisse
ChimayRed = StringVar()  # Holds the quantity of Chimay Red
BalticPorter = StringVar()  # Holds the quantity of Baltic Porter
CreamAle = StringVar()  # Holds the quantity of Cream Ale
GermanPilsner = StringVar()  # Holds the quantity of German Pilsner
BlondeAle = StringVar()  # Holds the quantity of Blonde Ale
Subtotal = StringVar()  # Holds the quantity of Sub total
Total = StringVar()  # Holds the quantity of Total
ServiceFee = StringVar()  # Holds the quantity of Service Fee
VATTax = StringVar()  # Holds the quantity of VAT Tax
Cost = StringVar()  # Holds the quantity of Cost

# Show the labels and entry widgets
lblreference = Label(frame1, font=('aria', 15, 'bold'),
                     text="Order No.", fg="#286590", bd=10, anchor='w')
lblreference.grid(row=0, column=0)
txtreference = Entry(frame1, font=('ariel', 17, 'bold'), state=DISABLED, textvariable=OrderNo,
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
txtcost = Entry(frame1, font=('ariel', 17, 'bold'), state=DISABLED, textvariable=Cost,
                bd=6, insertwidth=4, bg="#286590", justify='right')
txtcost.grid(row=1, column=3)

servicelbl = Label(frame1, font=(
    'aria', 15, 'bold'), text="Service Fee", fg="#286590", bd=10, anchor='w')
servicelbl.grid(row=2, column=2)
servicetxt = Entry(frame1, font=('ariel', 17, 'bold'), state=DISABLED,
                   textvariable=ServiceFee, bd=6, insertwidth=4, bg="#286590", justify='right')
servicetxt.grid(row=2, column=3)

lblTax = Label(frame1, font=('aria', 15, 'bold'),
               text="VAT Tax", fg="#286590", bd=10, anchor='w')
lblTax.grid(row=3, column=2)
txtTax = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=VATTax, state=DISABLED,
               bd=6, insertwidth=4, bg="#286590", justify='right')
txtTax.grid(row=3, column=3)

lblSubtotal = Label(frame1, font=('aria', 15, 'bold'),
                    text="Subtotal", fg="#286590", bd=10, anchor='w')
lblSubtotal.grid(row=4, column=2)
txtSubtotal = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=Subtotal, state=DISABLED,
                    bd=6, insertwidth=4, bg="#286590", justify='right')
txtSubtotal.grid(row=4, column=3)

lblTotal = Label(frame1, font=('aria', 15, 'bold'),
                 text="Total", fg="#286590", bd=10, anchor='w')
lblTotal.grid(row=5, column=2)
txtTotal = Entry(frame1, font=('ariel', 17, 'bold'), textvariable=Total, state=DISABLED,
                 bd=6, insertwidth=4, bg="#286590", justify='right')
txtTotal.grid(row=5, column=3)


lblTotal = Label(frame1, text="---------------------", fg="white")
lblTotal.grid(row=6, columnspan=3)

img = PhotoImage(file='money1.png')
btnTotal = Button(frame1, padx=16, pady=8, bd=20, fg="black", font=(
    'ariel', 17, 'bold'), width=150, height=33, image=img, text="Total Bill", bg="#286590", command=claculateOrderAmount)
btnTotal.grid(row=7, column=1)

btnreset = Button(frame1, padx=16, pady=8, bd=10, fg="black", font=(
    'ariel', 17, 'bold'), width=10, text="Reset Bill", bg="#286590", command=resetBill)
btnreset.grid(row=7, column=2)

btnexit = Button(frame1, padx=16, pady=8, bd=10, fg="black", font=(
    'ariel', 17, 'bold'), width=10, text="Exit App", bg="#286590", command=exitApp)
btnexit.grid(row=7, column=3)

# Function to show the prices for each item
def priceListing():
    roo = Tk()
    roo.geometry("800x320+0+0")
    roo.title("Price Listing")
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="Beer", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'),
                    text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="Price ($)", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="Berliner Weisse", fg="#286590", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="$80.00", fg="#286590", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="Chimay Red", fg="#286590", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="$60.00", fg="#286590", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="Baltic Porter", fg="#286590", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="$75.00", fg="#286590", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="Cream Ale", fg="#286590", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="$45.00", fg="#286590", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="German Pilsner", fg="#286590", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="$89.00", fg="#286590", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="Blonde Ale", fg="#286590", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('Arial', 17, 'bold'),
                    text="$68.00", fg="#286590", anchor=W)
    lblinfo.grid(row=6, column=3)
    roo.mainloop()

# Show the price listing button
pricelistingbtn = Button(frame1, padx=16, pady=8, bd=10, fg="black", font=(
    'ariel', 16, 'bold'), width=10, text="Price Listing", bg="#286590", command=priceListing)
pricelistingbtn.grid(row=7, column=0)

root.mainloop()
