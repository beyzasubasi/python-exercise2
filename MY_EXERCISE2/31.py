bolenler = [2]*(10**7+1)
sayac = 0

for i in range(2, len(bolenler)//2):
    for j in range(2*i, len(bolenler), i):
        bolenler[j] += 1

for i in range(2,len(bolenler)-1):
    if(bolenler[i]==bolenler[i+1]):
        sayac += 1

print(sayac)
