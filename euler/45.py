tri = set()
pent = set()
hexa = set()

def triangular(n):
    return int((n*(n+1))/2)
def pentagonal(n):
    return int((n*((3*n)-1))/2)
def hexagonal(n):
    return int(n*((2*n)-1))

for i in range(1,100000):
    tri.add(triangular(i))
    pent.add(pentagonal(i))
    hexa.add(hexagonal(i))
# for i in range(1,9999):
#     for j in range(1,9999):
#         if pentagonal(j) > triangular(i):
#             break
#         for k in range(1,9999):
#             if triangular(i) == pentagonal(j) == hexagonal(k):
#                 print(triangular(i))
#             elif hexagonal(k) > triangular(i) or hexagonal(k) > pentagonal(j):
#                 break

print(tri.intersection(pent, hexa))