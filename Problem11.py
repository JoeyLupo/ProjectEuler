from functools import reduce
import time

start_time = time.time()
ADJ = 4
grid = []
diag_tot= []
diag= []
vert = []
lat = []
    
def diagonal(grid):
    
    #NW-SE Diagonal
    for x in range(len(grid)-(ADJ - 1)):
        for y in range(len(grid)-(ADJ - 1)):
            l = []
            for n in range(ADJ):
                l.append(grid[x+n][y+n])
                
            diag.append(l)
            
    #SW-NE Diagonal 
    for x in range(len(grid)-(ADJ-1)):
        for y in range((ADJ-1),len(grid)):   
            l = []     
            for n in range(ADJ):
                l.append(grid[x+n][y-n])
            diag.append(l)
    
    
    for seq in diag:
        diag_tot.append(reduce(lambda x,y: x*y, seq))           
    
    return max(diag_tot)
   
def lateral(grid):
    for x in grid:
        for n in range(len(x)):          
            lat.append(reduce(lambda x,y: x*y, x[n:n+4]))
    
    return max(lat)

def vertical(grid):
    grid = [list(x) for x in zip(*grid)]
            
    for x in grid:
        for n in range(len(x)):          
            vert.append(reduce(lambda x,y: x*y, x[n:n+4]))
    
    return max(vert)
    

with open('grid.txt', 'r') as f: 
    for line in f:
        grid.append([int(i) for i in str(line.rstrip('\n')).split(' ')])
                 
print(max(vertical(grid),lateral(grid),diagonal(grid)), 'in {} seconds'.format(time.time()-start_time))      