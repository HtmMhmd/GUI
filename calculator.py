from tkinter import *

# Create the main window and set the title
root = Tk()
root.title("Calculator")

# Create an Entry widget to display the result
show = Entry(root, width=25, borderwidth=5)
show.grid(row=0, column=0, padx=10, pady=20, columnspan=3)

# Function to handle button clicks
def btn_clck(num):
    """Handle button clicks and update the display"""
    smth = show.get()
    show.delete(0, END)
    global n1
    n1 = int(str(smth) + str(num))
    show.insert(0, str(smth) + str(num))

# Function to handle addition
def btn_add():
    """Handle addition and update the global variables"""
    global n2
    n2 = int(show.get())
    show.delete(0, END)
    global x
    x = "0"

# Function to handle subtraction
def btn_sub():
    """Handle subtraction and update the global variables"""
    global n2
    n2 = int(show.get())
    show.delete(0, END)
    global x
    x = "1"

# Function to handle equality
def btn_equal():
    """Handle equality and update the display"""
    show.delete(0, END)
    if x == "0":
        result = n1 + n2
    elif x == "1":
        result = n2 - n1
    print(n2)
    print(n1)
    print(result)
    show.insert(0, result)

# Create buttons and assign their commands
button1 = Button(root, text="1", command=lambda: btn_clck(1), padx=20, pady=10)
button1.grid(row=3, column=0)
button2 = Button(root, text="2", command=lambda: btn_clck(2), padx=20, pady=10)
button2.grid(row=3, column=1)
button3 = Button(root, text="3", command=lambda: btn_clck(3), padx=20, pady=10)
button3.grid(row=3, column=2)

button4 = Button(root, text="4", command=lambda: btn_clck(4), padx=20, pady=10)
button4.grid(row=2, column=0)
button5 = Button(root, text="5", command=lambda: btn_clck(5), padx=20, pady=10)
button5.grid(row=2, column=1)
button6 = Button(root, text="6", command=lambda: btn_clck(6), padx=20, pady=10)
button6.grid(row=2, column=2)

button7 = Button(root, text="7", command=lambda: btn_clck(7), padx=20, pady=10)
button7.grid(row=1, column=0)
button8 = Button(root, text="8", command=lambda: btn_clck(8), padx=20, pady=10)
button8.grid(row=1, column=1)
button9 = Button(root, text="9", command=lambda: btn_clck(9), padx=20, pady=10)
button9.grid(row=1, column=2)

button0 = Button(root, text="0", command=lambda: btn_clck(0), padx=20, pady=10)
button0.grid(row=4, column=0)

button_equal = Button(root, text="=", command=btn_equal, padx=20, pady=10)
button_equal.grid(row=4, column=1, columnspan=2)
button_add = Button(root, text="+", command=btn_add, padx=20, pady=10)
button_add.grid(row=5, column=0)
button_sub = Button(root, text="-", command=btn_sub, padx=20, pady=10)
button_sub.grid(row=5, column=1)
button_clear = Button(root, text="C", command=lambda: show.delete(0, END), padx=20, pady=10)
button_clear.grid(row=5, column=2)

# Start the main event loop
root.mainloop()



