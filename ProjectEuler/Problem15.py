
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({},{})'.format(self.x,self.y)    
    
class Arrow:
    def __init__(self, Point):
        self.loc = Point   
    
    def move_up(self):    
        self.loc.x += 1 
        
    def move_right(self):    
        self.loc.y += 1
        
    def get_loc(self):
        return Point(self.loc.x, self.loc.y) 

start = Point(0,0)   
arrow = Arrow(start)
arrow.move_right()
arrow.move_up()

print(arrow.get_loc())     

"""
import time
 
def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L
 
start = time.time()
n = route_num(20)
elapsed = (time.time() - start)
print(n)   