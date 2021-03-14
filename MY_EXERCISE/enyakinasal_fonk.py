# Verilen herhangi bir listede asal olmayan sayıları en yakın asal sayıya dönüştüren ve listeyi güncelleyen kodu yazınız.
# eşit uzaklık gibi durumlarda büyük olan sayı tercih edilecektir.
# 4 sayısı hem 3 e hem de 5 e dönüştürülebilir, bu durumda 5 tercih edilecektir.

def asalmi(sayi):
    for i in range(2, sayi - 1, 1):
        if sayi % i == 0:
            return False
    return True


def yuvarla(liste):
    for i in range(len(liste)):
        el = liste[i]
        if el <= 2:
            el = 2
        else:
            while asalmi(el) == False:
                el = el + 1
        liste[i] = el
    return liste

print(yuvarla([8,9]))