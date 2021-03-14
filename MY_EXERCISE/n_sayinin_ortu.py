# girilen n adet sayının ortlamasını bulan algo

n = int(input("Kaç sayının ortalamasını bulmak istiyorsunuz: "))
sayac = 0
toplam = 0


while(sayac<n):
    sayac+=1
    k = int(input("Sayınızı giriniz: "))

    toplam = toplam + k


ort = toplam/n
print("Girdiğiniz sayıların ortalaması: ", ort)
