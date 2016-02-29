"""
s = 0
for num in range(1,101):
    s += num ** 2
 
a = sum(range(1,101))**2 - s    
              
print(a)      
"""

x = sum(range(101))**2 - sum(map(lambda x: x**2, range(101)))

print(x) 