# *                 g)	Aşağıdaki çıktıyı üreten kodu yazınız.
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


sayac=6

for satir in range(1,sayac):
    for sutun in range(1,satir+1):
        print("*", end=' ')

    print(" \n ")

sayac=5

for satir in range(sayac,1,-1):
    for sutun in range(satir,1,-1):
        print("*", end=' ')

    print(" \n ")
