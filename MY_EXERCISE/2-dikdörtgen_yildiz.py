"""
Ciz isimli bir fonksiyon yazın.
Ciz(4, 8) çağrımına karşın aşağıdaki çıktıyı üretsin
 *  *  *  *  *  *  *  *
 *  *  *  *  *  *  *  *
 *  *  *  *  *  *  *  *
 *  *  *  *  *  *  *  *

"""
def ciz(satir,sutun):
    for i in range(satir):
        for j in range(sutun):
            print("*", end=" ")
        print("")

sat=int(input("SATIR SAYISI: "))
sut=int(input("SUTUN SAYISI: "))

ciz(sat,sut)
