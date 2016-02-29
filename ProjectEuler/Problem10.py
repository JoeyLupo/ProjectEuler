from Problem3 import is_prime
total = 0
def sum_primes(num):
    while True:
        if is_prime(num):
            yield num
        num += 1
        
        
for p in sum_primes(2):
    if p < 2000000:
        total += p
    else:
        print(total) 
        exit()    
   
 