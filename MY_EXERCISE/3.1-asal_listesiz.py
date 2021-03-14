""" Kullanıcıdan önce bir n sayısı girmesi istenecek. Sonra 1’den n sayısına KADAR olan asal sayılar ekrana yazdırılacak."""

# BEYZA FİRDEVS SUBAŞI      180401047

p = int(input("hangi sayıya kadar olan asal sayılar hesaplansın: "))
n = 2

if(p==2):
    print("{} den daha küçük asal sayı yoktur!".format(p))

else:
    while(n<p):
        i = 3
        asalmi = 1
        if(n!=2 and n%2==0):
            asalmi = 0
        else:
            while(i<=n**(1/2)):

                if(n!=i and n%i==0):
                    asalmi = 0
                i += 2
        if(asalmi == 1):
            print(n)
        n += 1
