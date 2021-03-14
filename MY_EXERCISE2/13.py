n = int(input("bir sayı girin: "))
bt = 0
while(n!=0):
    bt += n - (n//10)*10
    n = n//10
print(bt)
