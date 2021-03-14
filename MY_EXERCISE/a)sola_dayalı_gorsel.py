# 1             satırlar arası birer boşluk kalacak şekilde yazdır
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

#deger=[]               liste olarak üretir
#for i in range(1,6):

#    deger.append(i)
#    print(deger, "\n \n")


sayac=6

for satir in range(1,sayac):
    for sutun in range(1,satir+1):
        print(sutun, end=' ')
    print(" \n ")