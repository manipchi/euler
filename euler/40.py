list = []
x = []
product = 1
for i in range(1,1000000):
    x = [int(a) for a in str(i)]
    for j in range(0,len(x)):
        list.append(x[j])
for m in range(0,7):
    product = product * list[(10**m)-1]
print(product)