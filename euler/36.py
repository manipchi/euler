palindromes = []
winning = []
sum = 0
for i in range (1,1000000):
    x = [int(a) for a in str(i)]
    y = [int(a) for a in str(i)]
    x.reverse()
    if i%2 == 1 and x == y:
        palindromes.append(i)
print(palindromes)
for i in range(0, (len(palindromes)-1)):
    b = bin(palindromes[i]).replace("0b", "")
    z = [int(k) for k in b]
    w = [int(k) for k in b]
    print(z)
    w.reverse()
    if z == w:
        winning.append(palindromes[i])
        sum = sum + palindromes[i]
print(palindromes)
print(winning)
print(sum)
