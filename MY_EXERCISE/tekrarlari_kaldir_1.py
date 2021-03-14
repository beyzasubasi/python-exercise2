def tekrar_kaldir_v1(x):
  y = []
  for i in x:
    if i not in y:      #eleman y de yoksa
      y.append(i)
  return y

a = [1,2,3,4,3,2,1]
print(a)
print(tekrar_kaldir_v1(a))  