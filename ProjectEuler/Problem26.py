from decimal import *

def get_decimal(num1, num2, op = 'None'):
    num1 = Decimal(num1)
    num2 = Decimal(num2)
    return num1/num2

def parse_decimal(num):
    num = str(num).split('.')[1]
    return num[:-1]

def find_repeating_pattern(strnum):
    found = False
    for n in range(1,len(strnum)):
        pattern = [strnum[i:i+n] for i in range(0, len(strnum), n) if len(strnum[i:i+n]) == n]
        if len(pattern) > 1 and pattern[1:] == pattern[:-1]: 
            found = True
            return pattern[0]
    
    if not found: find_repeating_pattern(strnum[1:])
    
getcontext().prec = 5001

answer = 0
maxi = 0
for d in range(1,1000):
    x = get_decimal(1, d)
    if(len(str(x))>100):
        x = parse_decimal(x)
        x = x[:5000]
        if len(str(find_repeating_pattern(x))) > maxi:
            maxi = len(str(find_repeating_pattern(x))) 
            answer = d
    print(d)
print('max number of repeating =',maxi)
print('number = ',answer)

