import math

def get_primes(num):
    x= 0
    while(x <= math.sqrt(num)):
        if is_prime(x):
            yield x
            
        x += 1

def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(num) + 1), 2):
            if num % current == 0:
                return False
        return True
    return False     
   
if __name__ == '__main__':
    num = 600851475143
    prime = get_primes(num)

    for n in prime: 
        if(num % n == 0):
            print(n)    
      