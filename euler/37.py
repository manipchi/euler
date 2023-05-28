import math
listfactors = []
primes = []
sex = set()
truncations = set()
def factors(number):
    for i in range(2,math.ceil(math.sqrt(number))+1):
        if number%i == 0:
            listfactors.append(i)
            listfactors.append(number/i)
            break
    return(listfactors)
    

for i in range(1,1000000,1):
    listfactors.clear()
    if len(factors(i)) == 0:
        x = [int(a) for a in str(i)]
        if 0 not in x and 2 not in x and 4 not in x and 6 not in x and 8 not in x:
            primes.append(i)
            
for k in range(0,len(primes)):
    truncations.clear()
    d = primes[k]
    x = [int(a) for a in str(primes[k])]
    z = [int(a) for a in str(primes[k])]
    while len(x) > 1:
        x.pop(len(x)-1)
        strings = [str(integer) for integer in x]
        a_string = "". join(strings)
        y = int(a_string)
        truncations.add(y)
    while len(z) > 1:
        z.pop(0)
        strings = [str(integer) for integer in z]
        a_string = "". join(strings)
        y = int(a_string)
        truncations.add(y) 
    primeset = set(primes)
    if truncations.issubset(primeset):
        sex.add(d)
    else:
        continue


sex = list(sex)
sex.sort()
print(sex)
answer = 23+37+53+73+313+317+373+797+3137+3797+739397
print(answer)