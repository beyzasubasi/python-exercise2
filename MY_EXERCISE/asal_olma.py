# girilen sayı asal mıdır değil midir

"""p = int(input("Bir sayı giriniz: "))
asal = 0

for n in range(2, p//2+1):  #sayının kareköküne kadar gitsem yeterli
    if(p//n*n == p):
        asal = 1

if(asal==0):
    print("asal sayıdır")
else:
    print("asal sayı değildir")"""

a = int(input("Sayıyı giriniz: "))
b = 2

if(a<b):
    print("Sayı asal değildir!")

elif(a==b):
    print("Sayı asaldır!")

elif(a>b):       #else: şeklinde de bitirilebilir
    b = b + 1     #yerinin mantığını anlamadım

    if(a%b==0):
        print("Sayı asal değildir!")

    else:
        print("Sayı asaldır..")











