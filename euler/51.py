def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if prime[p] == True:
            for i in range(p*p, n, p):
                prime[i] = False
        p += 1
    primes = []
    for i in range(2,n):
        if prime[i]:
            primes.append(i)
    return primes

primes = sieve(1000000)
valid = []
for i in range(0, len(primes)):
    count0 = 0
    count1 = 0
    count2 = 0
    list = [int(a) for a in str(primes[i])]
    for j in range(0, len(list)):
        if list[j] == 0: count0 += 1
        if list[j] == 1: count1 += 1
        if list[j] == 2: count2 += 1
    if count0 == 3 or count1 == 3 or count2 == 3:
        valid.append(primes[i])
            
print(valid)