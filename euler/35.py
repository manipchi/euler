import math
listfactors = []
primes = []
sex = []
s = []
def factors(number):
    for i in range(2,math.ceil(math.sqrt(number))+1):
        if number%i == 0:
            listfactors.append(i)
            listfactors.append(number/i)
            break
    return(listfactors)
    

for i in range(2,1000000,1):
    listfactors.clear()
    if len(factors(i)) == 0:
        x = [int(a) for a in str(i)]
        if 0 not in x and 2 not in x and 4 not in x and 6 not in x and 8 not in x:
            primes.append(i)
            
            
for k in range(0,len(primes)):
    x = [int(a) for a in str(primes[k])]
    for l in range(0,len(x)+1):
        x.append(x.pop(0))
        strings = [str(a) for a in x]
        a_string = "".join(strings)
        y = int(a_string)
        if y not in primes:
            break
        else:
            continue
        break
    if y in primes:
        sex.append(y)

# x = [int(a) for a in str(999917)]
# for l in range(0,len(x)):
#     x.append(x.pop(0))
#     strings = [str(a) for a in x]
#     a_string = "".join(strings)
#     y = int(a_string)
#     print(y)
#     if y not in primes:
#         break
#     sex.append(y)


sex = set(sex)
        
print(sorted(sex))
print(len(sex))
