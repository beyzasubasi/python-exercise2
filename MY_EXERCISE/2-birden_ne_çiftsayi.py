"""Kullanıcıdan önce bir n sayısı girmesi istenecek. Sonra 1’den n sayısına kadar olan çift
sayıların toplamı hesaplanıp ekrana yazdırılacak."""

n = int(input("Kaça kadar olan çift sayıları toplamak istersiniz: "))
n=n-1
toplam = 0

while(n>1):
    if(n%2==0):
        toplam = toplam + n
    n = n-1
print("Çift sayıların toplamı: ",toplam)
