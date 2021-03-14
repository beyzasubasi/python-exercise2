def isprime(n):
    i = 3
    if(n<2):
        return(0)
    if(n!=2 and n%2==0):
        return(0)
    while(i<=n**(1/2)):
        if(n%i==0):
            return(0)
        i += 2
    return(1)

def ikiyebol(a):
    b = a[:len(a)//2]
    c = a[len(a)//2:]
    return(b,c)

def divisors(n):
    carpanlar = [1]
    q = int(n**(1/2)//1)+1
    for p in range(2, q):
        if(n%p==0):
            carpanlar.append(p)
            carpanlar.append(int(n/p))
    if((q-1)**2==n):
        return(carpanlar[:-1])
    return(carpanlar)

def allprimes(n):
    primes = list(range(2,n+1,1))
    for x in range(0,int(n/2)+1):
        if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i]=0
    primes.sort()
    return(primes[primes.count(0):])
