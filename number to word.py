dic1 = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
dic2 = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
        17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
dic3 = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty",
        90: "Ninety", 100: "Hundred"}

num = int(input("Enter any number: "))
num_copy = num
length = len(str(num))
# print(length)
last = str(num)[-1]
last_two = str(num)[length - 2: length]

# print(last)
# print(last_two)

# print(last_third)
word = ""

if length == 1:
    val1 = dic1.get(num)
    word = word + val1
    print(word)
if length >= 2:
    if last == str(0) and length >= 2 and num not in dic2:
        units = dic3.get(num)
        word = word + str(units)
        if length == 2:
            print(word)
    if length >= 2 and int(last_two) in dic2:
        tens = dic2.get(num)
        word = word + str(tens)
        if length == 2 and num in dic2:
            print(word)
    elif length >= 2 and int(last_two) not in dic2 and last != str(0):
        val2 = num % 10
        val_2 = dic1.get(val2)
        # print(val_2)
        word = word + str(" ") + str(val_2)
        num //= 10
        # print(num)

        num = str(num)[-1] + str(0)
        # print(num)

        val__2 = dic3.get(int(num))
        # print(val__2)
        word = str(val__2) + word + str(" ")
        # print(word)
        if length == 2:
            print(word)
    if length >= 3:
        last_third = str(num_copy)[-3]
        # print(last_third)
        if last_two == "00":
            hundred = dic1.get(int(last_third))
            word = str(hundred) + " Hundreds"
            if length == 3:
                print(word)
        elif last_two != "00" and length >= 3:
            hundred2 = dic1.get(int(last_third))
            word = str(hundred2) + " Hundreds and " + word
            print(word)
    if length == 4:
        first = str(num_copy)[0]
        last_three = str(num_copy)[1: length]
        if last_three == "000":
            thousand = dic1.get(int(first))
            word = thousand + " Thousands"
            print(word)
        else:
            thousand2 = dic1.get(int(first))
            word = str(thousand2) + " Thousands " + word
            print(word)


