sayac = 0
for n in range(2,100000):
    if(str(2**n)[:3]=="123"):
        sayac += 1
        print(sayac, n)
