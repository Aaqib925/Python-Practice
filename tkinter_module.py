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

root = Tk()
# this is the upper frame
topframe = Frame(root)

topframe.pack()

# for the lower frame we will create one and pass the parameter in pack function
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

# for creating buttons for each frame
# fg means foreground, which is not compulsory
button1 = Button(topframe, text="Button1", fg="Blue")
button2 = Button(topframe, text="Button2", fg="red")
button3 = Button(bottomframe, text="Button3", fg="green")
button4 = Button(bottomframe, text="Button4", fg="brown")
button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()

