#Klavyeden girilen kelimenin uzunluğunu faktöriyel olarak hesaplayıp sonucu ekrana yazdıran kodu yazınız.



veri=input()
faktoriyel(len(veri))
def faktoriyel(uzunluk):
        if uzunluk==0:
                return 1
        else:
                return uzunluk*faktoriyel(uzunluk-1)