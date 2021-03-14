"""1) Kullanıcıdan önce bir n sayısı girmesi istenecek. Sonra bu n sayısı kadar sınav notu
girmesi sağlanacak. En düşük sınav notu ekrana yazdırılacak."""

# BEYZA FİRDEVS SUBAŞI      180401047

n = int(input("Kaç tane sınav notu girmek istersiniz: "))
sayac = 0
edsn = 100

if(n<=0):
    print("Sınav notu sayınızı girmediniz!")

else:
    while(n>sayac):
        k = int(input("Sınav notunuzu giriniz: "))
        sayac +=1

        if(k<edsn):
            edsn=k

    print("En düşük notunuz: ",edsn)

