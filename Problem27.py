from Problem21 import get_factors
import time
start = time.time()
primes = []
maxi = [0,0,0]

def is_prime(num):
    if num < 2: 
        return False
    elif num == 2: return True
    else:
        for n in range(2,int(num**0.5+1)): 
            if num % n == 0: return False
    
    return True

for b in range(-999,1000):
    if not is_prime(b): continue
    for a in range(-999,1000):
        n = 0
        if(n**2 + a*n + b)>1:
            while(is_prime(n**2 + a*n + b)):
                n+=1
        if n > maxi[2]:
            maxi = [a,b,n]    
                
  
print(maxi[0]*maxi[1], 'in',time.time()-start,'seconds')               

