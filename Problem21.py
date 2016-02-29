from itertools import chain
def get_factors(num):
    factors = []
    for n in range(1,int(abs(num)**0.5)+1):
        if num % n == 0: 
            factors.append(n) 
            if num // n != num: 
                factors.append(num//n)
    
    if num < 1: factors += [-x for x in factors]
              
    return set(factors)


if __name__ == '__main__':
    answer = 0
    for x in range(1,10001):
        y = sum(get_factors(x))
        if y > x:
            if x == sum(get_factors(y)):
                answer += x + y
    
    print(answer)
    print(get_factors(16))
    