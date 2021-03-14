#recursiveli fibonacci
def fib(number):
    if(number==0):
        return 0
    elif(number==1):
        return 1
    return fib(number-1)+fib(number-2)

print(fib(5))

#iteratif fibonacci
def fibbi(sayi):
    prepresayi=0
    presayi=0
    currentsayi=0

    for i in range(sayi-1):
        prepresayi=presayi
        presayi=currentsayi
        currentsayi=prepresayi+presayi
    return currentsayi
print(fibbi(5))