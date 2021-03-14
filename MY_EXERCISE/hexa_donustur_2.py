def hexadecimalToDecimal(hexval):
    length = len(hexval)
    base = 1
    dec_val = 0

    for i in range(length - 1, -1, -1):

        # If character lies in '0'-'9',
        # converting it to integral 0-9
        # by subtracting 48 from ASCII value
        if hexval[i] >= '0' and hexval[i] <= '9':
            tmp = ord(hexval[i])
            dec_val = dec_val + (tmp - 48) * base
            base = base * 16

        # If character lies in 'A'-'F',converting
        # it to integral 10-15 by subtracting 55
        # from ASCII value
        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            tmp = ord(hexval[i])
            dec_val = dec_val + (tmp - 55) * base
            base = base * 16

    return dec_val


hexnum = '2A5'
print(hexadecimalToDecimal(hexnum))