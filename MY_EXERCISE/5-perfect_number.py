"""
Mükemmel sayıları (perfect number) bulan kodu yazınız.
Örnek: 6, 28, 496 birer mükemmel sayıdır. 6 sayısı 1, 2, and 3’ün toplamıdır.
"""
"""
def perfect_number(sayi):
    i=0
    a=0
    toplam=0
    while a<sayi:
        a+= 1
        i+=1
        if(sayi%i==0):
            toplam+=i

    if(sayi==toplam):
        print(sayi,"mükemmel bir sayıdır.")
    else:
        print(sayi,"mükemmel bir sayı değildir.")

perfect_number(int(input("sayı giriniz:")))
"""

def perfect(sayi):
    toplam=0
    for i in range (1, sayi):
        if(sayi%i==0):
            toplam=toplam+i
    if(toplam==sayi):
        print(sayi,"mükemmel bir sayıdır.")
    else:
        print(sayi, "mükemmel bir sayı değildir.")

perfect(8)