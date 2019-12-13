from msvcrt import getch
import sys

sent = "Please predict the answer                  "
print("Enter the petition: ", end="")
sys.stdout.flush()
ans = ""
counter = 0
for i in range(len(sent)):
    x = getch()
    if ord(x.decode()) == 13:
        break
    else:
        counter += 1
        if x.decode() != "/":
            print(x.decode(), end="")
            sys.stdout.flush()

        elif x.decode() == "/":
            print(sent[counter - 1], end="")
            sys.stdout.flush()
            while x.decode() == "/":
                z = getch()
                counter += 1
                print(sent[counter - 1], end="")
                sys.stdout.flush()
                if z.decode() == "/":
                    break
                else:
                    ans = ans + z.decode()

print()
sent = input("Enter your question: ")

print("Your answer is: ", ans)