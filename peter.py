# from msvcrt import getch
# import sys
# from getch import getch
#
# sent = "Please predict the answer                  "
# print("Enter the petition: ", end="")
# sys.stdout.flush()
# ans = ""
# counter = 0
# for i in range(len(sent)):
#     x = getch()
#     if ord(x.decode()) == 13:
#         break
#     else:
#         counter += 1
#         if x.decode() != "/":
#             print(x.decode(), end="")
#             sys.stdout.flush()
#
#         elif x.decode() == "/":
#             print(sent[counter - 1], end="")
#             sys.stdout.flush()
#             while x.decode() == "/":
#                 z = getch()
#                 counter += 1
#                 print(sent[counter - 1], end="")
#                 sys.stdout.flush()
#                 if z.decode() == "/":
#                     break
#                 else:
#                     ans = ans + z.decode()
#
# print()
# sent = input("Enter your question: ")
#
# print("Your answer is: ", ans)
# from getch import getch
#
# sent = "Please predict the answer"
#
# print("Enter the petition: ")
#
# ans = ""
# counter = 0
# for i in range(len(sent)):
#     x = getch()
#     hu = x.decode()
#     if ord(hu) == 13:
#         break
#     else:
#         counter += 1
#         if hu != "/":
#             print(hu)
#
#         elif hu == "/":
#             print(sent[counter - 1])
#
#             while hu == "/":
#                 z = getch()
#                 counter += 1
#                 print(sent[counter - 1])
#
#                 if z.decode() == "/":
#                     break
#                 else:
#                     ans = ans + z.decode()
#
# print(ans)

from msvcrt import getch
import sys
import time

string = "Please predict the answer                  "
print("Enter the petition: ", end="")
sys.stdout.flush()
answer = ""
counter = 0
for i in range(len(string)):
    char = getch()
    if ord(char.decode()) == 13:    # Enter ASCII code to break the petition
        break
    elif ord(char.decode()) == 8:
        counter -= 1
        print("\b \b", end="")
        sys.stdout.flush()
    else:
        counter += 1
        if char.decode() != "/":
            print(char.decode(), end="")   # Printing what user is typing
            sys.stdout.flush()

        elif char.decode() == "/":
            print(string[counter - 1], end="")
            sys.stdout.flush()

            while char.decode() == "/":
                z = getch()
                counter += 1
                print(string[counter - 1], end="")    # replacing the letters
                sys.stdout.flush()
                if z.decode() == "/":
                    break
                else:
                    answer += z.decode()

print()
print()
default_string = input("Enter your question: ")
print()
y = "Thinking..."
for i in y:
    time.sleep(0.1)
    print(i, end="")
    sys.stdout.flush()

print()
if len(answer) == 0:
    print("I only answer my developer...Sorry")
if answer == "no":
    print("Sorry, I am learning, can't answer this.")
elif len(answer) != 0:
    print("The answer according to prediction is: ", answer)



