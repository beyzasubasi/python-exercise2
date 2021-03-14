#kullanıcıdan 2 adet 3 basmaklı sayı al, 2si de polindromsa topla, biri polindromsa çıkar, eğer ikiside pol değilse çarp
#BEYZA FİRDEVS SUBAŞI       180401047

x = int(input("3 basamaklı bir sayı giriniz: "))
z = int(input("3 basamaklı bir sayı giriniz: "))

y1 = int(x/100)
x = int(x-(y1*100))
o1 = int(x/10)
x = int(x-(o1*10))
b1 =int(x)

y = int(z/100)
z = int (z-(y*100))
o = int (z/10)
z = int (z-(o*10))
b =int (z)


if(y1==b1 and y==b):
    print("Polindrom sayılardır ve iki sayının toplamı: ",(100*y1+10*o1+b1) + (100*y+10*o+b))

elif(y1==b1 or y==b):

    if(y>y1):
        y1,y=y,y1
        o1,o=o,o1
        b1,b=b,b1


    print("Bir adet polindrom sayı vardır ve iki sayının farkı: ",(100*y1+10*o1+b1) - (100*y+10*o+b))

else:
    print("Polindrom sayılar değildir ve iki sayının çarpımı: ",(100*y1+10*o1+b1) * (100*y+10*o+b))
