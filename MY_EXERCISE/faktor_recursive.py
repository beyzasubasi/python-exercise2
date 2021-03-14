#recursiveli fak
def faktoriyel(n):
    if n==1:
        return 1
    else:
        return n*faktoriyel(n-1)
print(faktoriyel(5))

#iterasyonlu fak
def iteratif_faktoriyel(n):
    sonuc=1
    for i in range(2,n+1):
        sonuc*=i
    return sonuc
print(iteratif_faktoriyel(5))