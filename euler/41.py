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
    

for i in range(1000000,10000000,1):
    listfactors.clear()
    if len(factors(i)) == 0:
        x = [int(a) for a in str(i)]
        if 1 in x and 2 in x and 3 in x and 4 in x and 5 in x and 6 in x and 7 in x:
            primes.append(i)
print(primes)