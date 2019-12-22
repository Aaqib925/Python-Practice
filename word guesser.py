# This is a program that guess a word by getting the information about the user's word
print("Please think of a word in your mind.")
len_user = int(input("Enter how many letters your word has: "))

print("Please enter the column number of your letter from the list below: ")
print("1\t2\t3\t4\n-------------\nA\tB\tC\tD\nE\tF\tG\tH\nI\tJ\tK\tL\nM\tN\tO\tP\nQ\tR\tS\tT\nU\tV\tW\tX\nY\tZ")

col_list = []
for i in range(1, len_user + 1):
    col = int(input("Enter the column number for {} letter of your word:".format(i)))
    col_list.append(col)
print(col_list)

print("Now please enter the column in which your letters appear from the list below: ")
print("1\t2\t3\t4\t5\t6\t7\n-------------------------")

last_list = []
conj_col1 = ["A", "E", "I", "M", "Q", "U", "Y"]
conj_col2 = ["B", "F", "J", "N", "R", "V", "Z"]
conj_col3 = ["C", "G", "K", "O", "S", "W"]
conj_col4 = ["D", "H", "L", "P", "T", "X"]
for j in col_list:
    if j == 1:
        print("A\tE\tI\tM\tQ\tU\tY")
        last_list.append(conj_col1)
    if j == 2:
        print("B\tF\tJ\tN\tR\tV\tZ")
        last_list.append(conj_col2)
    if j == 3:
        print("C\tG\tK\tO\tS\tW")
        last_list.append(conj_col3)
    if j == 4:
        print("D\tH\tL\tP\tT\tX")
        last_list.append(conj_col4)

tran_col = []
for a in range(1, len_user + 1):
    z = int(input("Enter the column number of the {} letter of word: ".format(a)))
    tran_col.append(z - 1)
print("Your word according to guess is: ", end="")
for b in range(len_user):
    letter = last_list[b][tran_col[b]]
    print(letter, end="")