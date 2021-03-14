""" Kullanıcıdan önce bir n sayısı girmesi istenecek. Sonra 1’den n sayısına kadar olan asal
sayılar ekrana yazdırılacak."""

#kullanıcıdan okunan sayıdan daha küçük bütün asal sayıları bir liste olarak döndüren algo

p = int(input("Kaça kadar asal sayı yazdırmak istediğinizi bir n değeri şeklinde giriniz: "))
n = 2
asal = []
while(n<p):
    i = 3
    asalmi = 1
    if(n!=2 and n%2==0):
        asalmi = 0
    else:
        while(i<=n**(1/2)):
            if(n%i==0):
                asalmi = 0
            i += 2
    if(asalmi == 1):
        asal.append(n)
    n += 1
print(asal)
