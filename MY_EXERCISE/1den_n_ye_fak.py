#girilen sayının faktöriyeli (1den 5e)

n = int(input("Faktöriyelini almak istediğiniz sayı: "))
i = 1
carpim = 1

while(i<=n):
    carpim = carpim*i
    i += 1

print(carpim)