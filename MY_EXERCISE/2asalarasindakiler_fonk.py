#2- Gönderilen 2 sayı arasındaki tüm asal sayıları bulan python fonksiyon uygulamasını yapınız.

def asal_sayilar(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)


sayi1 = int(input('sayı 1:'))
sayi2 = int(input('sayı 2:'))

asal_sayilar(sayi1, sayi2)