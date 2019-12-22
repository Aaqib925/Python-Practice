from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox


# ================1stWindow=============================================
class MyClass1:
    def __init__(self):
        win1 = Tk()
        self.win1 = win1
        win1.geometry('600x300')
        win1.configure(background='black')
        f1 = Frame(win1, width=1000, height=700, relief='raise')
        f1.configure(background='grey')
        f1.pack()
        f1Label = Label(f1, font=('arial', 30, 'bold'), text='WORD GUESSING GAME')
        f1Label.grid(row=0, column=0)

        f2 = Frame(win1, width=800, height=700, relief='raise')
        f2.configure(background='black')
        f2.pack()
        name = Label(f2, text='Enter Your Name', font=('arial', '9', 'bold'))  # Taking name
        name.grid(row=3, column=3)

        entry1 = Entry(f2)  # user name
        entry1.grid(row=3, column=4)
        name = StringVar()
        # self.n=name.get() #saving user name
        self.n = entry1

        f3 = Frame(win1, width=1000, height=700, relief='raise')
        f3.configure(background='grey')
        f3.pack()
        f3labe1 = Label(f3, text='START YOUR GAME BY CLICKING THE BUTTON', font=('arial', '10', 'bold'))
        f3labe1.grid(row=3, column=2)

        button1 = Button(f3, pady=8, bd=8, text='START', font=('arial', 8, 'bold'), width=20,
                         command=self.GameStart).grid(row=7, column=2)

    def GameStart(self):
        print(self.n.get())
        self.win1.destroy()
        win2 = Tk()
        self.win2 = win2
        self.win2 = win2
        win2.geometry('600x300')
        win2.configure(background='black')
        f3 = Frame(win2, width=1000, height=700, relief='raise')
        f3.configure(background='grey')
        f3.pack()
        f3Label = Label(f3, font=('arial', 10, 'bold'),
                        text='PLease Think a Word in\n your mind and enter the length of word below')
        f3Label.grid(row=1, column=0)

        entry1 = Entry(f3)  # taking length
        entry1.grid(row=3, column=0)
        # self.len=IntVar()
        # self.len_user=entry1.get()
        # print(self.len_user)
        self.entry1 = entry1

        def func():
            len_user = int(self.entry1.get())
            print(len_user)
            f4 = Frame(win2, width=1000, height=700, relief='raise')
            f4.configure(background='pink')
            f4.pack()
            f3Label = Label(f4, font=('arial', 10, 'bold'),
                            text="Please enter the column number of your letter from the list below: ")
            f3Label.grid(row=3, column=0)
            # imageview
            img = "C:\\Users\\zainu\\OneDrive\\Desktop\\Areeba_Project\\pic1.png"
            canvas = Canvas(win2, width=200, height=100)
            canvas.pack()
            mi = PhotoImage(file=img)
            canvas.create_image(5, 0, anchor=NW, image=mi)  # ,anchor=NW)

            f5 = Frame(win2, width=1000, height=700, relief='raise')
            f5.configure(background='pink')
            f5.pack()

            i = 1
            col_list1 = []

            f5Label = Label(f5, font=('arial', 10, 'bold'),
                            text="Enter the column number for {} letter of your word:".format(i))
            f5Label.grid(row=i, column=0)  # i-1
            entry1 = Entry(f5)  # taking column num
            entry1.grid(row=i, column=2)

            def take_input():
                nonlocal i, col_list1, entry1, len_user
                col_list1.append(entry1.get())
                print(col_list1)
                i += 1
                if i <= len_user:
                    f5Label = Label(f5, font=('arial', 10, 'bold'),
                                    text="Enter the column number for {} letter of your word:".format(i))
                    f5Label.grid(row=i, column=0)  # i-1
                    entry1 = Entry(f5)  # taking column num
                    entry1.grid(row=i, column=2)

                if i <= len_user:
                    button1 = Button(f5, text='Submit2', font=('arial', 8, 'bold'), width=20, command=take_input).grid(
                        row=i + 1, column=2)

                else:
                    button1 = Button(f5, text='Done', font=('arial', 8, 'bold'), width=20,
                                     command=self.Gamestart2).grid(row=i, column=2)

                if i > len_user:
                    self.col_list = []
                    # removing duplicate for user
                    for y in col_list1:
                        if y in self.col_list:
                            continue
                        else:
                            self.col_list.append(y)
                    self.col_list1 = col_list1

            button1 = Button(f5, text='Submit', font=('arial', 8, 'bold'), width=20, command=take_input).grid(row=i + 1,
                                                                                                              column=2)

        ##            for i in range(1, len_user+1):
        ##                f5Label=Label(f5,font=('arial',10,'bold'),text="Enter the column number for {} letter of your word:".format(i))
        ##                f5Label.grid(row=i,column=0)#i-1
        ##                entry1=Entry(f5) #taking column num
        ##                entry1.grid(row=i, column=2)
        ##                col_list1.append(entry1.get())
        ##                button1=Button(f5,text='Submit',font=('arial',8,'bold'),width=20,command=self.Gamestart2).grid(row=i+1,column=2)

        # button1=Button(f5,text='Submit',font=('arial',8,'bold'),width=20,command=self.Gamestart2).grid(row=i+1,column=2)

        button1 = Button(f3, pady=8, bd=8, text='Submit', font=('arial', 8, 'bold'), width=20, command=func).grid(row=7,
                                                                                                                  column=0)

    def Gamestart2(self):
        print(self.col_list)
        col_list = self.col_list
        col_list1 = self.col_list1

        self.win2.destroy()
        win3 = Tk()
        self.win3 = win3

        num = "1\t2\t3\t4\t5\t6\t7\n-----------------------------------------------------------------------------------------"

        print("")
        # list which will work in backend
        last_list = []
        conj_col1 = ["A", "E", "I", "M", "Q", "U", "Y"]
        conj_col2 = ["B", "F", "J", "N", "R", "V", "Z"]
        conj_col3 = ["C", "G", "K", "O", "S", "W"]
        conj_col4 = ["D", "H", "L", "P", "T", "X"]

        win3.geometry('600x300')
        win3.configure(background='black')
        f4 = Frame(win3, width=1000, height=700, relief='raise')
        f4.configure(background='grey')
        f4.pack()
        f5Label = Label(f4, font=('arial', 10, 'bold'), text=num)
        f5Label.grid(row=2, column=0)

        for j in col_list1:
            if int(j) == 1:
                last_list.append(conj_col1)
            if int(j) == 2:
                last_list.append(conj_col2)
            if int(j) == 3:
                last_list.append(conj_col3)
            if int(j) == 4:
                last_list.append(conj_col4)

        user_list = []
        i = 3
        for k in col_list:

            if int(k) == 1:
                f5Label = Label(f4, font=('arial', 10, 'bold'), text="A\tE\tI\tM\tQ\tU\tY")
                f5Label.grid(row=i, column=0)
                print("A\tE\tI\tM\tQ\tU\tY")
                user_list.append(conj_col1)
            if int(k) == 2:
                f5Label = Label(f4, font=('arial', 10, 'bold'), text="B\tF\tJ\tN\tR\tV\tZ")
                f5Label.grid(row=i, column=0)
                print("B\tF\tJ\tN\tR\tV\tZ")
                user_list.append(conj_col2)
            if int(k) == 3:
                f5Label = Label(f4, font=('arial', 10, 'bold'), text="C\tG\tK\tO\tS\tW\t ")
                f5Label.grid(row=i, column=0)
                print("C\tG\tK\tO\tS\tW")
                user_list.append(conj_col3)
            if int(k) == 4:
                f5Label = Label(f4, font=('arial', 10, 'bold'), text="D\tH\tL\tP\tT\tX\t ")
                f5Label.grid(row=i, column=0)
                print("D\tH\tL\tP\tT\tX")
                user_list.append(conj_col4)
            i += 1

        f4 = Frame(win3, width=1000, height=700, relief='raise')
        f4.configure(background='pink')
        f4.pack()
        f3Label = Label(f4, font=('arial', 10, 'bold'),
                        text="Please enter the column number of your letter from the Above: ")
        f3Label.grid(row=i, column=0)
        # imageview

        f5 = Frame(win3, width=1000, height=1000, relief='raise')
        f5.configure(background='pink')
        f5.pack()

        i = 1

        f5Label = Label(f5, font=('arial', 10, 'bold'),
                        text="Enter the column number for {} letter of your word:".format(i))
        f5Label.grid(row=i, column=0)  # i-1
        entry1 = Entry(f5)  # taking column num
        entry1.grid(row=i, column=2)

        final_list = []
        ls = []
        ##        for letter_choice in range(1, len(col_list1) + 1):
        ##            letter_choosen = int(input("Enter the column number of the {} letter from word: ".format(letter_choice)))
        ##            final_list.append(letter_choosen - 1)

        word = []

        ##        for a in range(len(final_list)):
        ##            var = last_list[a]
        ##            index = final_list[a]
        ##            print(index)
        ##            print(var)
        ##            word.append(var[index])
        ##        print(word)
        ##
        ##
        ##        final_word = "".join(word)
        ##        print("Your word is:", final_word)

        def take_input():
            nonlocal i, entry1, final_list, ls
            a = int(entry1.get()) - 1
            final_list.append(a)
            print(final_list)
            i += 1

            def answer():  # Used to display the Answer
                nonlocal final_list, last_list, word
                for a in range(len(final_list)):
                    var = last_list[a]
                    index = final_list[a]
                    print(index)
                    print(var)
                    word.append(var[index])
                    final_word = "".join(word)
                    final_word = "Your Word is :" + final_word
                    # print("Your word is:", final_word)
                    f5Label = Label(f5, font=('arial', 10, 'bold'), text=final_word)
                    f5Label.grid(row=i + 1, column=0)

            if i <= len(col_list1):
                f5Label = Label(f5, font=('arial', 10, 'bold'),
                                text="Enter the column number for {} letter of your word:".format(i))
                f5Label.grid(row=i, column=0)  # i-1
                entry1 = Entry(f5)  # taking column num
                entry1.grid(row=i, column=2)

            if i <= len(col_list1):
                button1 = Button(f5, text='Submit2', font=('arial', 8, 'bold'), width=20, command=take_input).grid(
                    row=i + 1, column=2)

            else:
                button1 = Button(f5, text='Done', font=('arial', 8, 'bold'), width=20, command=answer).grid(row=i,
                                                                                                            column=2)

        button1 = Button(f5, text='Submit', font=('arial', 8, 'bold'), width=20, command=take_input).grid(row=i + 1,
                                                                                                          column=2)


obj = MyClass1()
