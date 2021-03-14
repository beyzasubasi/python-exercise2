"""
Ciz isimli bir fonksiyon yazın.
Ciz(6) çağrımına karşın aşağıdaki çıktıyı üretsin.
 *
 *  *
 *  *  *
 *  *  *  *
 *  *  *  *  *
 *  *  *  *  *  *
"""

def ciz(sayac):
    for satir in range(sayac):
        for sutun in range(satir+1):
            print("*", end=" ")
        print("")

sat=int(input("satır sayısı: "))
ciz(sat)



