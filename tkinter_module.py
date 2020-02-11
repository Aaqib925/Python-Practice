from tkinter import *

# root = Tk()
# # label is anything to be written or widget
# mylabel = Label(root, text="Hello Aaqib \nHow are you doing")
# # now placing the label on the window
#
# # pack function is going to place the label where it gets place by itself
# mylabel.pack()
#
# # to hold the screen we use the mainloop fucntion
# root.mainloop()

# root = Tk()
# # this is the upper frame
# topframe = Frame(root)
#
# topframe.pack()
#
# # for the lower frame we will create one and pass the parameter in pack function
# bottomframe = Frame(root)
# bottomframe.pack(side=BOTTOM)
#
# # for creating buttons for each frame
# # fg means foreground, which is not compulsory
# button1 = Button(topframe, text="Button1", fg="Blue")
# button2 = Button(topframe, text="Button2", fg="red")
# button3 = Button(bottomframe, text="Button3", fg="green")
# button4 = Button(bottomframe, text="Button4", fg="brown")
#
# # by default they are made on the top of other
#
# button1.pack(side=LEFT)
# button2.pack(side=RIGHT)
# button3.pack(side=LEFT)
# button4.pack(side=RIGHT)
#
# root.mainloop()

# for the widgets

root = Tk()

# bg means background and fg means foreground which means color of font
# we will use fill paramter to make the labels grow inside the main window
# fill = X means left and right and fill = Y means up and down

# first label

label1 = Label(root, text="One", bg="Pink", fg="Blue")
label1.pack(side=TOP, fill=X)

label2 = Label(root, text="Two", bg="Black", fg="white")
label2.pack(side=LEFT, fill=Y)

label3 = Label(root, text="Three", bg="White", fg="Blue")
label3.pack(side=RIGHT, fill=X)

root.mainloop()