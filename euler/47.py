import math
listfactors = []
# def factors(number):
#     for i in range(2,math.ceil(math.sqrt(number))+1):
#         if number%i == 0:
#             listfactors.append(i)
#             listfactors.append(number/i)
#             break
#     return(listfactors)
    

# for i in range(1,100000,1):
#     listfactors.clear()
#     if len(factors(i)) == 0:
#         primes.append(i)

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
        
def primefactors(n):
    listfactors.clear()
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i == 0:
            if is_prime(i) == True:
                listfactors.append(i)
            if is_prime(int(n/i)) == True:
                listfactors.append(int(n/i))
    return(list(dict.fromkeys(listfactors)))


for i in range(1,1000000):
    if len(primefactors(i)) == 4 and len(primefactors(i+1)) == 4 and len(primefactors(i+2)) == 4 and len(primefactors(i+3)) == 4:
        print(i)
        break
    