# h) Kullanıcının bilgisayarın tuttuğu bir sayıyı tahmin etmeye çalıştığı bir program yazınız.
# Kullanıcının tahmin için 3 defa hakkı olacaktır.
# Program, kullanıcının tahmininin doğru değerden büyük ya da küçük olduğunu gösteren mesajlar verecektir.


import random

sayi = random.randint(1,100)
tahmin, deneme = 0, 0
print("3 Deneme hakkınız bulunmaktadır..")

while(tahmin!=sayi):
    tahmin=int(input("Tahmininiz: "))
    deneme+=1

    if(deneme<=2):
        if(tahmin<sayi):
            print("Daha büyük bir sayı giriniz..")

        elif(tahmin>sayi):
            print("Daha küçük bir sayı giriniz: ")

        else:
            print("DOĞRU TAHMİN!")

    else:
        print("Deneme hakkınız bitti!")
        print("TUTULAN SAYI: ",sayi)
        break




