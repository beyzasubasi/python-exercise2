a = [200, 3, 511, 72, 11, 13, 17, 19, 23, 249, 31, 37, 41, 43, 47]

for j in range(len(a)-1):
    for i in range(len(a)-1):
        if(a[i]>a[i+1]):
            a[i], a[i+1] = a[i+1], a[i]
print(a)

