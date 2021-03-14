#iteratif çözüm (recursive kullanmadan)

def harmonik_toplam_iteratif(n):
    toplam=0

    for i in range(1, n+1):
        toplam=toplam+(1/i)
    return toplam

print(harmonik_toplam_iteratif(4))