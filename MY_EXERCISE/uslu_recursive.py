#b üssü n i yazdırıyoruz
import time

#recursivle yazdım
def power(b, n):
    if n==0:
        return 1
    else:
        return b*power(b, n-1)

#iteratif yazdım
def power_iteratif(b, n):
    p=1
    for i in range(0, n):
        p=p*b

    return p

start=time.time()

end_start=time.time()
print(end_start-start)

x=power_iteratif(2,10)
y=power(2, 10)

print(x)
print(y)

