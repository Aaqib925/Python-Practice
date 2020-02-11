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

root.mainloop()

