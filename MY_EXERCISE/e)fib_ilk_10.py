# e)Fibonacci serisini ilk 10 terime kadar yazdıracak program kodunu yazınız.
# Fibonacci serisi:
# 0  1  1  2  3  5  8  13  21  34

fn1, fn2 =0, 1
fn3=45
print(fn1, end=' ')
print(fn2, end=' ')


for i in range(0,8):
    fn3=fn1+fn2
    print(fn3, end=' ')

    fn1=fn2
    fn2=fn3