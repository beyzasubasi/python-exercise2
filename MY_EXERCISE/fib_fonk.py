#Verilen sayıya kadar Fibonacci sayı dizisini yazdıran fibonacci isimli bir fonksiyon yazalım.

def fibonacci(sayi):
    a,b=0,1
    while b<=sayi:
        print (a)
        a,b=b,a+b

fibonacci(10)