# 5 4 3 2 1      satırlar arası birer boşluk kalacak şekilde yazdır
# 4 3 2 1
# 3 2 1
# 2 1
# 1

sayac=5

for satir in range(sayac,0,-1):
    for sutun in range(satir,0,-1):
        print(sutun, end=' ')
    print(" \n ")