def hexadecimalToDecimal(hexval):
    dict_hex = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    length = len(hexval)
    base = 1
    dec_val = 0

    #len-1 den -1e kadar 1er 1er azalt
    for i in range(length - 1, -1, -1):
        if hexval[i] >= '0' and hexval[i] <= '9':
            dec_val = dec_val + int(hexval[i]) * base
            base = base * 16

        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            dec_val = dec_val + dict_hex[hexval[i]] * base
            base = base * 16

    return dec_val

#işlemlere tersten başladık 5 A 2 şeklinde (range den dolayı)
hexnum = '2A5'
print(hexadecimalToDecimal(hexnum))