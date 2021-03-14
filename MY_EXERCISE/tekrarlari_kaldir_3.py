def tekrar_kaldir_v1(x):
  y = []
  for eleman in x:
      bulundu=False
      for i in range(len(y)):
          if(eleman==y[i]):
              bulundu=True

      if(bulundu==False):
          y.append(eleman)
  return y

a = [1,2,3,4,3,2,1]
print(a)
print(tekrar_kaldir_v1(a))