"""
c)String’i terse çeviren program kodu yazınız.

Girdi:
str1 = "PYnative"
Çıktı:
evitanYP
"""
#pythonda bir şeyi ters çevirme:    'hello world'[::-1]     'dlrow olleh'

#ikinci yol
#for x in range(len(isim)-1, 0, -1):
#print(isim[x])​

#üçüncü yol
#uzunluk = len(isim) -1
#while uzunluk>=0:
#print(isim[uzunluk])
#uzunluk -=1​


isim = input ("İsminiz :")
#Birinci Yol
print("İsminizin tersten yazılışı :", isim[::-1])
