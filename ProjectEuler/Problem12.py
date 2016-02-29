from functools import reduce

def get_triangle_nums(num):
    total = 0
    for n in range(num+1):
         total+= n

    return total

def factors(n):    
    step = 2 if n%2 else 1
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1, step) if n % i == 0)))       

n = 10000

while(True):
    num = get_triangle_nums(n)
    if(len(factors(num)) > 500):
        print(num)
        exit()
    n += 1

            