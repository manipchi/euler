import math

mult13 = []
mult17 = []
last4 = []
last5 = []
last6 = []
last8 = []
answers = []
for i in range(0,1000):
    if len(str(13*i)) == 3:
        mult13.append(13*i)
    elif len(str(13*i)) > 3:
        break

for i in range(0,100):
    if len(str(17*i)) == 3:
        mult17.append(17*i)
    elif len(str(17*i)) > 3:
        break

for i in range(0,len(mult13)):
    for j in range(0,len(mult17)):
        if str(mult13[i])[-2:] == str(mult17[j])[0:2] and len((str(mult13[i]) + str(mult17[j])[-1:])) == len(set(str(mult13[i]) + str(mult17[j])[-1:])):
            last4.append(str(mult13[i]) + str(mult17[j])[-1:])

for i in range(0,len(last4)):
    z = (int(last4[i][1]) - int(last4[i][0]))
    if z < 0:
        a = -z
        last4[i] = str(a) + last4[i]
    elif z>0:
        a = 11-z
        last4[i] = str(a) + last4[i]
        
for i in range(0,len(last4)):
    if len(last4[i]) == len(set(last4[i])) and int(last4[i][0]) == 5 or int(last4[i][0] == 0):
        last5.append(last4[i])


for k in range(0,len(last5)):
    for i in range(0,10):
        if int(str(i) + last5[k][0:2])%7 == 0 and len(str(i) + last5[k]) == len(set(str(i) + last5[k])):
            last6.append(str(i)+last5[k])

for k in range(0,len(last6)):
    for i in range(10,100):
        if int(str(i)[1])%2 == 0 and (int(str(i)[0]) + int(str(i)[1]) + int(last6[k][0]))%3 == 0 and len(str(i) + last6[k]) == len(set(str(i) + last6[k])):
            last8.append(str(i) + last6[k])
            
for k in range(0,len(last6)):
    for i in range(1,10):
        if int(str(i)[0])%2 == 0 and (int(str(i)[0]) + int(last6[k][0]))%3 == 0 and len('0' + str(i) + last6[k]) == len(set('0' + str(i) + last6[k])):
            last8.append('0'+str(i) + last6[k])

for k in range(0,len(last8)):
    for i in range(10,100):
        if len(str(i) + last8[k]) == len(set(str(i) + last8[k])):
            answers.append(str(i) + last8[k])
            
print(answers)
sum = 0
for i in range(0,len(answers)):
    sum = sum+int(answers[i])
    
print(sum)

    
        

    