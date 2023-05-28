import math
def pentagonal(n):
    return(int((n*((3*n)-1))/2))
pentagonals = []

for i in range(1,10000):
    pentagonals.append(pentagonal(i))

# for i in range(0,9999):
#     for j in range(0,i):
#         if (pentagonals[i] + pentagonals[j]) in pentagonals and abs(pentagonals[j] - pentagonals[i]) in pentagonals:
#             print(i,j)
            

print(pentagonals[2166] - pentagonals[1019])