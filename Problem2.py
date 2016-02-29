total = 0

x = y = 1;
while(x < 4000000):
    if(x % 2 == 0):
        total += x
    z = x
    x += y
    y = z    
    
print(total)    
        

    
    
    