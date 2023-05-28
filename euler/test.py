# import math
# import time
# primes= []
# sum = 0
# max = 0
# def is_prime(n):
#     if n <= 3:
#         return True
#     if n%2==0 or n%3==0:
#         return False
#     i = 5
#     stop = int(math.ceil(n**0.5))
#     while i <= stop:
#         if n%i == 0 or n%(i + 2) == 0:
#             return False
#         i += 6
#     return True

# t0 = time.time()

# for i in range(2,1000000):
#     if is_prime(i):
#         primes.append(i)
        
# t1 = time.time()
# print(t1-t0)


l = ['1', '1', '0', '0', '1', '9']
print(l.index('1'))