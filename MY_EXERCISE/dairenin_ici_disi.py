import math
x = int(input("X değeri:"))
y = int(input("Y değeri:"))
distance=math.sqrt(x**2+y**2);
if (distance<=10):
    print("%d ve %d koordinatları dairenin içerisinde"%(x, y))
else:
    print("%d ve %d koordinatları dairenin dışında"%(x, y))