from Problem18 import solve

with open('triangle.txt','r') as f:
    print(solve([list(map(int, line.split())) for line in f]))