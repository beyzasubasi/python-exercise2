"""
a)s1 ve s2 isimli 2 adet String verilmektedir.
Bu string’lerin ilk, orta ve son karakterlerinden oluşan yeni bir string döndüren program kodu yazınız.

Girdi:    s1 = "America"
          s2 = "Japan"
Çıktı:    AJrpan
"""

s1 = "America"
s2 = "Japan"

ilk_char = s1[:1] + s2[:1]
orta_char = s1[int(len(s1)/2):int(len(s1)/2)+1] + s2[int(len(s2)/2):int(len(s2)/2)+1]
son_char = s1[len(s1)-1] + s2[len(s2)-1]

toplam = ilk_char + orta_char + son_char
print("String: ",toplam)