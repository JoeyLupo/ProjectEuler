from Problem3 import is_prime

def get_primes(start):
    while True:
        if is_prime(start):
            yield start     
        start += 1
        
x = get_primes(2)
nth_prime = 10001
for _ in range(nth_prime-1):
    next(x)
    
print(next(x))

"""

def nth_prime(n):
    index = 1
    prime = 2
    i = 3
    while index < n:
        if is_prime(i):
            prime = i
            index += 1
        i += 2
    return prime

print(nth_prime(6))

"""