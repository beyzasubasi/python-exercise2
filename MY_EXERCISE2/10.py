fn1, fn2 = 1, 1
fn3 = 42
while(fn3<10000):
    fn3 = fn1 + fn2
    fn1 = fn2
    fn2 = fn3
print(fn1)
