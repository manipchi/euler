oddcomp = []
oddcompset = set()
gold = set()
import math
listfactors = []
primes = []
def factors(number):
    for i in range(2,math.ceil(math.sqrt(number))+1):
        if number%i == 0:
            listfactors.append(i)
            listfactors.append(number/i)
            break
    return(listfactors)
    

for i in range(2,100000,1):
    listfactors.clear()
    if len(factors(i)) == 0:
        primes.append(i)

for i in range(3,2000,2):
    for j in range(3,i+2,2):
        oddcomp.append(i*j)
        oddcompset.add(i*j)
oddcomp = list(dict.fromkeys(oddcomp))
oddcomp.sort()

for i in range(0,10000):
    for j in range(0,10000):
        if primes[j]>oddcomp[i]:
            break
        if math.sqrt((oddcomp[i] - primes[j])/2) == math.floor(math.sqrt((oddcomp[i] - primes[j])/2)):
            gold.add(oddcomp[i])
            break
     
print(sorted(oddcompset-gold))