#girilen sayının faktöriyeli ( n den 1e )

n = int(input("Faktöriyelini almak istediğiniz sayı: "))
carpim = 1

while(n>1):
    carpim = carpim * n
    n = n-1

print(carpim)