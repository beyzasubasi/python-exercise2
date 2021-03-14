#Kendisine gönderilen bir sayının tam bölenlerini bulan python uygulamasını yapınız.

def bolenlerim(x):

    bolen=[]

    for i in range(1,x):

        if(x%i==0):
            bolen.append(i)

    return bolen

print(bolenlerim(10))