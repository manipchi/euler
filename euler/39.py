import math
count = 0
maxi = 0
p = 0
triples = []
for h in range(1,1001):
    triples.clear()
    count = 0
    for m in range(1,200):
        for n in range(1,m):
            a = 2*m*n
            b = (m**2)-(n**2)
            c = math.sqrt((b**2)+(a**2))
            sum = a + b + c
            if h%sum == 0:
                triple = [a*(h/sum),b*(h/sum),c*(h/sum)]
                triple.sort()
                triples.append(triple)
    if triples != [] and len(triples) >= 10:
        print(triples)
        print(h)
