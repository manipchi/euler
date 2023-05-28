x = []
for j in range(1,1000000):
    x.clear()
    for i in range (1,9):
        if len(x) < 9:
            z = i*j
            l = [int(a) for a in str(z)]
            x = x+l
    if 1 in x and 2 in x and 3 in x and 4 in x and 5 in x and 6 in x and 7 in x and 8 in x and 9 in x and len(x) == 9:
        print(x)
    
