import math
def is_div(num, div):
    if(num == 0):
        return False
    for n in range(1, div+1):
        if num % n:
            return False
        
    return True  

num = 0
while(num < math.factorial(20)):
    if(is_div(num, 20)): 
        print(num)
        break
    num +=20
    
        

        
        