# f)	Verilen bir sayıyı basamaklarına göre terse çevirecek program kodunu yazınız.
#       Verilen sayı:                  Beklenen çıktı:
#       76542                          24567


sayi = int(input("Sayıyı Gir : "))
ters = 0
while (sayi > 0):
    gecici = sayi % 10
    ters = (ters * 10) + gecici
    sayi = sayi // 10

print("\n Sayının Ters Çevrilmiş Hali = %d" % ters)
