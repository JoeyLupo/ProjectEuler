from Problem21 import get_factors
import time

start = time.time()

abundant_nums = [x for x in range(1,28123) if sum(get_factors(x)) > x]
sums = []
answer = 0
for l in abundant_nums:
    for x in abundant_nums:
        if l+x < 28123:
            sums.append(l+x)  

sums = set(sums)
for n in range(1,28123):
    if n not in sums:         
        answer += n     
print('Found', answer, 'in', time.time()-start,'seconds')         

