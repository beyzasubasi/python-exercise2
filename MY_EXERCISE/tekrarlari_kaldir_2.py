def tekrar_kaldir_v2(x):
    #set:tekrarları kaldırır
    return list(set(x))

a = [1,2,3,4,3,2,1]
print(a)
print(tekrar_kaldir_v2(a))