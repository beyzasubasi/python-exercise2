#kullanıcının girdiği 2 sayı için EKOK hesapla (örn: 6 ve 12 için EKOK=12)

x = int(input("İlk sayıyı giriniz: "))
y = int(input("İkinci sayıyı giriniz: "))

if(x>y):

    x,y = y,x

elif(x<y):

    sayac = y
    k = sayac % x
    l = sayac % y

    while 1:
        if (k == 0 and l == 0):
            break

        sayac = sayac + 1
        k = sayac % x
        l = sayac % y

print("EKOK: ",sayac)
