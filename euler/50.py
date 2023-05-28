import math
primes= []
sum = 0
max = 0
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

for i in range(2,1000000):
    if is_prime(i):
        primes.append(i)

for i in range(0,len(primes)):
    sum = 0
    for j in range(0,len(primes)-i):
        if sum<1000000:
            sum += primes[i+j]
            if is_prime(sum) == True and j>max:
                max = j
                print(j+1, sum)
