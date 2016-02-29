from functools import reduce

f = open('num.txt','r+')
num = []
total = []

with open('num.txt', 'r') as f: 
    for line in f:
        num += [int(i) for i in list(str(line.rstrip('\n')))]
        

for n in range(len(num)-13):
    total.append(reduce(lambda x,y: x*y, num[n:n+13], 1)) 

print(max(total))