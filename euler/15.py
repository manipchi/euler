def numberOfPaths(x,y, memo = {}):
    key = str(x) + ',' + str(y)
    if x == 0 and y == 0: return 1
    if x < 0 or y < 0: return 0
    if key in memo: return memo[key]
    memo[key] = numberOfPaths(x-1,y) + numberOfPaths(x, y-1)
    return memo[key]

print(numberOfPaths(200,200))