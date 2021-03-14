#Fonksiyon kullanarak yarıçapı girilen dairenin alanını hesaplayan Python programı

from math import *

def dairalan(r):
    return pi*r*r

r=int(input("yarıçapı giriniz:"))

print(dairalan(r))