#kullanıcının girdiği 2 sayı için EBOB hesapla (örn: 6 ve 12 için EBOB=6)

# BEYZA FİRDEVS SUBAŞI      180401047

m= int(input("İlk sayıyı giriniz: "))
n = int(input("İkinci sayıyı giriniz: "))
i = 1
ebob = 1


while (i<=m and i<=n ):

    if ( not (m % i) and not (n % i)):
        ebob = i
    i += 1


print("EBOB: ",ebob)