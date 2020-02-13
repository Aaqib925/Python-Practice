from tkinter import *

root = Tk()
root.title("Simple Calculator")

# creating an entry box

entry_box = Entry(root, width=41, borderwidth=5, bg="grey", fg="White")
entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(current) + str(number))

def button_clear():
    entry_box.delete(0, END)


f_num = 0
math = ""

def button_add():
    first_number = entry_box.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry_box.delete(0, END)

def button_sub():
    first_number = entry_box.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    entry_box.delete(0, END)

def button_m():
    first_number = entry_box.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    entry_box.delete(0, END)

def button_div():
    first_number = entry_box.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry_box.delete(0, END)

def button_equal():
    if math == "addition":
        second_num = int(entry_box.get())
        entry_box.delete(0, END)
        entry_box.insert(0, f_num + second_num)
    if math == "subtract":
        second_num = int(entry_box.get())
        entry_box.delete(0, END)
        entry_box.insert(0, f_num - second_num)
    if math == "division":
        second_num = int(entry_box.get())
        entry_box.delete(0, END)
        entry_box.insert(0, f_num / second_num)
    if math == "multiply":
        second_num = int(entry_box.get())
        entry_box.delete(0, END)
        entry_box.insert(0, f_num * second_num)


button1 = Button(root, text="1", padx=35, pady=15, borderwidth=2, bg="grey", fg="White", command=lambda: button_click(1))
button2 = Button(root, text="2", padx=35, pady=15, borderwidth=2, bg="grey", fg="White", command=lambda: button_click(2))
button3 = Button(root, text="3", padx=35, pady=15, borderwidth=2, bg="grey", fg="White", command=lambda: button_click(3))
button4 = Button(root, text="4", padx=35, pady=15, borderwidth=2, bg="grey", fg="White", command=lambda: button_click(4))
button5 = Button(root, text="5", padx=35, pady=15, borderwidth=2, bg="grey", fg="White", command=lambda: button_click(5))
button6 = Button(root, text="6", padx=35, pady=15, borderwidth=2, bg="grey", fg="White", command=lambda: button_click(6))
button7 = Button(root, text="7", padx=35, pady=15, borderwidth=2, bg="grey", fg="White", command=lambda: button_click(7))
button8 = Button(root, text="8", padx=35, pady=15, borderwidth=2, bg="grey", fg="White", command=lambda: button_click(8))
button9 = Button(root, text="9", padx=35, pady=15, borderwidth=2, bg="grey", fg="White", command=lambda: button_click(9))
button0 = Button(root, text="0", padx=35, pady=15, borderwidth=2, bg="grey", fg="White", command=lambda: button_click(0))
buttonequal = Button(root, text="=", padx=34, pady=15, borderwidth=2, command=button_equal)
buttonadd = Button(root, text="+", padx=42, pady=15, borderwidth=2, command=button_add)
buttonsub = Button(root, text="-", padx=44, pady=15, borderwidth=2, command=button_sub)
buttonmulti = Button(root, text="*", padx=43, pady=15, borderwidth=2, command=button_m)
buttonclear = Button(root, text="Clear All", padx=20, borderwidth=2, pady=15, command=button_clear)
buttondiv = Button(root, text="÷", padx=34, pady=15, borderwidth=2, command=button_div)


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonequal.grid(row=4, column=1)

buttonclear.grid(row=1, column=3)
buttonadd.grid(row=2, column=3)
buttonsub.grid(row=3, column=3)
buttonmulti.grid(row=4, column=3)
buttondiv.grid(row=4, column=2)

root.mainloop()
