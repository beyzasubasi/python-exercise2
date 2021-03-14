metin_girdi = input("Sayı giriniz:")
girdiler = metin_girdi.split()
len_girdi = len(girdiler)
max = int(girdiler[0])
min = int(girdiler[0])
total = 0
for i in range(len_girdi):
    girdiler[i] = int(girdiler[i])
    if (girdiler[i]>max):
        max = girdiler[i]
    if (girdiler[i]<min):
        min = girdiler[i]
    total = total + girdiler[i]
avg = total/len_girdi
print("En küçük=%d, En büyük=%d, Ortalama=%d"% (min,max,avg))