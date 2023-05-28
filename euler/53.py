def choose(n,r, memo = {}):
    key = str(n) + ',' + str(r)
    if n == r or r == 0: return 1
    if key in memo: return memo[key]
    memo[key] = choose(n-1,r,memo) + choose(n-1,r-1,memo)
    return memo[key]
print(choose(2,1))
count = 0
for a in range(1,101):
    for b in range(0,a):
        if choose(a,b) > 1000000:
            count +=1
print(count)
        
        
    
    
    
    