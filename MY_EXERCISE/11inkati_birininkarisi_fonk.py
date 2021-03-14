# Eğer bir sayı 11 in katıysa veya bir sayının karesiyse bu sayıya ob sayı denir.
# Verilen iki sayı arasındaki sayılardan ob sayı olanları tespit edip bunları
# bir listeye ekleyerek sonunda listeyi döndüren fonksiyonu yazınız.

from math import *

def ob(sayi1, sayi2):
    list=[]

    for i in range(sayi1, sayi2):
        if(i%11==0 or sqrt(i)==int(sqrt(i))):
            list.append(i)

    return list

print(ob(9,23))