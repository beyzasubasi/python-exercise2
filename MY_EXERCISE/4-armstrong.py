"""
Armstrong sayılarını bulan kodu yazınız.
Armstrong(1000) fonksiyonu çağrıldığında 1-1000 arasındaki Armstrong sayıları ekranda listelenecek.
Örnek : 0, 1, 153, 370, 371 and 407 birer Armstrong sayısıdır.
Basamaklarının küplerinin toplamı sayının kendisine eşittir.
"""

def armstrong(ust_limit):
    for i in range(1, ust_limit):
        toplam=0
        sayi=i

        while sayi>0:
            birler=sayi%10
            toplam+=birler**3
            sayi=sayi-birler
            sayi=sayi/10

        if(toplam==i):
            print(i)

armstrong(1000)


