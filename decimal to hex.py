def binary(num):
    """ Function to convert a decimal number into binary """

    binary_number = ""  # in this variable...the binary number will be added after conversion
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num >= 2:
        while num > 1:
            remainder = num % 2
            binary_number = str(remainder) + binary_number
            num //= 2  # this will reduce the number for the loop

            if num == 1:
                binary_number = str(1) + binary_number
    return binary_number


def bit(binary_num):
    """ This function will convert the binary number into four bits """
    len_bin_number = len(binary_num)
    modulus = len_bin_number % 4  # this will check if the number is already in bit or not
    bits = ""
    if modulus != 0:
        for b in range(modulus * 4):
            bits = b * str(0) + str(binary_num)  # this will add zeros till the bit is closest bit is made
            if len(bits) <= modulus * 4 and len(bits) % 4 == 0:
                break
    else:
        bits = binary_num  # if the number does not need any zero addition this will return the number

    return bits


def hexa(bits):
    """ Function to convert bits into hexa decimal """
    len_bits = len(bits)
