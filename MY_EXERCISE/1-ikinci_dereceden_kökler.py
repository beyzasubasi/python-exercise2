#katsayıları kullanıcıdan alınan 2.dereceden bir bilinmeyenli kökleri bulan program
#BEYZA FİRDEVS SUBAŞI       180401047
a = int(input("x karenin katsayısını giriniz: "))
b = int(input("x in katsayısını giriniz: "))
c = int(input("sabit terimi giriniz: "))

delta = b**2-4*a*c

if(delta>0):
    x1 = (-b + delta**(1/2)) / (2*a)
    x2 = (-b - delta**(1/2)) / (2*a)
    print(x1, x2)

elif(delta==0):
    x1 = -b/(2*a)
    print(x1)

else:
    print("Reel Kök Yoktur!")
