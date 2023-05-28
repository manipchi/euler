for i in range(100000,int(1000000/6)):
    digits = [int(a) for a in str(i)]
    digits.sort()
    count = 0
    for j in range(2,7):
        digitsm = [int(a) for a in str(i*j)]
        digitsm.sort()
        if digitsm == digits:
            count += 1
        else:
            break
    if count == 5:
        print(i)
        
        
    
        
        
        
    
            