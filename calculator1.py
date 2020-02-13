from tkinter import *

root = Tk()
root.title("Simple Calculator")

# creating an entry box

entry_box = Entry(root, width=35, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click():
    return


button1 = Button(root, text="1", command=button_click)
button2 = Button(root, text="2", command=button_click)
button3 = Button(root, text="3", command=button_click)
button4 = Button(root, text="4", command=button_click)
button5 = Button(root, text="5", command=button_click)
button6 = Button(root, text="6", command=button_click)
button7 = Button(root, text="7", command=button_click)
button8 = Button(root, text="8", command=button_click)
button9 = Button(root, text="9", command=button_click)
button0 = Button(root, text="0", command=button_click)

root.mainloop()
