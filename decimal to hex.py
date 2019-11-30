def binary(num):
    """ Function to convert a decimal number into binary """

    binary_number = ""  # in this variable...the binary number will be added after conversion
    if num == 0:
        binary_number = 0
    elif num == 1:
        binary_number = 1
    elif num >= 2:
        while num > 1:
            remainder = num % 2
            binary_number = str(remainder) + binary_number
            num //= 2  # this will reduce the number for the loop

            if num == 1:
                binary_number = str(1) + binary_number
    return binary_number


def bit(binary_num):
    """  Function to form bits of binary number """
    if binary_num == 0:
        return 0000
    elif binary_num == 1:
        return 1
    elif binary_num != 0:
        bits = binary_num
        if len(bits) % 4 == 0:
            return bits
        elif len(bits) != 4:
            for i in range(len(bits) * 4):
                bits = "0" + bits
                if len(bits) % 4 == 0:
                    break
            return bits


def hexa(bits):
    """ Function to convert bits into hexa decimal """
    if bits == 0:
        return 0
    elif bits == 1:
        return 1
    else:
        r1 = 0
        r2 = 4
        length = len(bits)
        hex_list = []

        while length >= 1:
            num2 = bits[r1:r2]
            # print(num2)
            total = 0
            if num2[0] == str(1):
                total += 8
            elif num2[0] == str(0):
                total += 0
            if num2[1] == str(1):
                total += 4
            elif num2[1] == str(0):
                total += 0
            if num2[2] == str(1):
                total += 2
            elif num2[2] == str(0):
                total += 0
            if num2[3] == str(1):
                total += 1
            elif num2[3] == str(0):
                total += 0
            if total >= 16:
                break

            if total == 0 or total > 0 and total != 10 and total != 11 and total != 12 and total != 13 and total != 14 and total != 15:
                hex_list.append(total)
            if total == 10:
                hex_list.append("A")
            if total == 11:
                hex_list.append("B")
            if total == 12:
                hex_list.append("C")
            if total == 13:
                hex_list.append("D")
            if total == 14:
                hex_list.append("E")
            if total == 15:
                hex_list.append("F")
            r1 += 4
            r2 += 4
            length -= 4

        answer = "".join(str(element) for element in hex_list)
        return answer


user_input = int(input("Enter the decimal number to convert in binary: "))

print("Your number {} in binary is equal to:".format(user_input), binary(user_input))
print("Your binary number in form of bits is:", bit(binary(user_input)))
print("Your number {} in hexa decimal is equal to:".format(user_input), hexa(bit(binary(user_input))))
