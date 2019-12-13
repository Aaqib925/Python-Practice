# # This is a program that guess a word by getting the information about the user's word
# print("Please think of a word in your mind.")
# len_user = int(input("Enter how many letters your word has: "))
#
# print("Please enter the column number of your letter from the list below: ")
# print("""
# 1\t2\t3\t4
# -------------
# A\tB\tC\tD
# E\tF\tG\tH
# I\tJ\tK\tL
# M\tN\tO\tP
# Q\tR\tS\tT
# U\tV\tW\tX
# Y\tZ
# """)
#
# col_list = []
# for i in range(1, len_user + 1):
#     col = int(input("Enter the column number for {} letter of your word:".format(i)))
#     col_list.append(col)
# print(col_list)
#
# print("Now please enter the column in which your letters appear from the list below: ")
# num = "1\t2\t3\t4\t5\t6\t7"
# print(num)
# print("---------------------")
#
# last_list = []
# conj_col1 = ["A", "E", "I", "M", "Q", "U", "Y"]
# conj_col2 = ["B", "F", "J", "N", "R", "V", "Z"]
# conj_col3 = ["C", "G", "K", "O", "S", "W"]
# conj_col4 = ["D", "H", "L", "P", "T", "X"]
# for j in col_list:
#     if j == 1:
#         print("A\tE\tI\tM\tQ\tU\tY")
#         last_list.append(conj_col1)
#     if j == 2:
#         print("B\tF\tJ\tN\tR\tV\tZ")
#         last_list.append(conj_col2)
#     if j == 3:
#         print("C\tG\tK\tO\tS\tW")
#         last_list.append(conj_col3)
#     if j == 4:
#         print("D\tH\tL\tP\tT\tX")
#         last_list.append(conj_col4)
#
# final_list = []
# ls = []
# for letter_choice in range(1, len(col_list) + 1):
#     letter_choosen = int(input("Enter the column number of the {} letter from word: ".format(letter_choice)))
#     final_list.append(letter_choosen - 1)
# # print(final_list)
#
# # print(last_list)
# word = []
# for a in range(len(final_list)):
#     var = last_list[a]
#     index = final_list[a]
#     # print(index)
#     # print(var)
#     word.append(var[index])
#
#
# final_word = "".join(word)
# print("Your think your word is:", final_word)
#
# second_column = [1, 2, 4]
# list3 = [["B", "F", "J", "N", "R", "V", "Z"], ["A", "E", "I", "M", "Q", "U", "Y"], ["B", "F", "J", "N", "R", "V", "Z"]]
# for i in range(len(second_column)):
#     x = list3[i][second_column[i] - 1]
#     print(x, end="")
