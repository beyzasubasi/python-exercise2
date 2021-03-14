#bir öğrenciye ait vize ve final notlarının ortalamasını hesaplayan ve ortalamaya göre ekrana "geçti" "kaldı" yazdıran algo

vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
GN = 60

ort = (vize*40)/100 + (final*60)/100

if(ort >= GN):
    print("Geçtiniz!")

else:
    print("Kaldınız!")
