import math

def is_prime(n):
    if n <= 3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    stop = int(math.ceil(n**0.5))
    while i <= stop:
        if n%i == 0 or n%(i + 2) == 0:
            return False
        i += 6
    return True


for i in range(1000,10000):
    for j in range(1,4500):
        a = i
        b = i+j
        c = i+j+j
        if c>9999:
            break
        x = [int(r) for r in str(a)]
        y = [int(r) for r in str(b)]
        z = [int(r) for r in str(c)]
        x.sort()
        y.sort()
        z.sort()
        if x==y and y==z and is_prime(a) and is_prime(b) and is_prime(c):
            print(a,b,c)