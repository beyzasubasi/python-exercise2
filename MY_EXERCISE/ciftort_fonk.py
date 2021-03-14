# Kullanıcının girdiği 2 sayı arasındaki çift sayıların ortalamasını bulan Python programı

def ciftik(sayi1, sayi2):
    toplam = 0
    count = 0

    for i in range(sayi1, sayi2):

        if(i%2==0):
            toplam+=i
            count+=1

    ort=toplam/count

    return ort

sayi1=int(input("kaçtan: "))
sayi2=int(input("kaça: "))

print(ciftik(sayi1, sayi2))