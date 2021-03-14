#2- asal sayıları bulan python fonksiyon uygulamasını yapınız.

def asalbul(x):
    i=1
    if(x!=2 and x%2==0 or x==1):
        return 0

    elif(x==2):
        return 1

    else:
        while(i<=x**1/2):
            if(x%i==0):
                return 1
            else:
                return 0

x=int(input("sayı girin: "))

if(asalbul(x) == 0):
    print("asal değildir")
elif(asalbul(x) == 1):
    print("asaldır")
