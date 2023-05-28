import math
listfactors = []
primes = []
maxx = 0
maxa = 0
maxb = 0
def factors(number):
    for i in range(2,math.ceil(math.sqrt(number))+1):
        if number%i == 0:
            listfactors.append(i)
            listfactors.append(number/i)
            break
    return(listfactors)
    

for i in range(2,10000,1):
    listfactors.clear()
    if len(factors(i)) == 0:
        primes.append(i)
        
print(primes[166])

def quad(a,b,x):
    return((x**2) +(a*x)+b)

for w in range(-1000,1000):
    for y in range(0,167):
        for i in range(0,1000):
            if quad(w,primes[y],i) not in primes:
                print(w,primes[y],i)
                if i > maxx:
                    maxx = i
                    maxa = w
                    maxb = primes[y]
                break
print(maxx,maxa,maxb)