def MonotonikMi(A):
    artan = True
    azalan = True
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            artan = False
        if A[i] < A[i + 1]:
            azalan = False
    return artan or azalan


x = [1, 2, 3, 4]
# x=[1, 4, 3, 2] monotonik olmaz
if (MonotonikMi(x)):
    print("Monotonik")
else:
    print("Monotonik değil")
