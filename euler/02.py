fibMemo = {}
sum = 0
def fib(n):
    if n == 1 or n == 2: return 1
    if n not in fibMemo:
        fibMemo[n] = fib(n-1) + fib(n-2)
    return fibMemo[n]

x = 1
while fib(x) < 4000000:
    if fib(x)%2 == 0:
        sum += fib(x)
    x +=1
print(sum)