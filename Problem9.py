

def is_py_triplet(a,b,c):
    if a**2 + b**2 ==c**2:
        return True
    else:
        return False
    
def equals_1000(a,b,c):
    if a+b+c == 1000:
        return True
    else:
        return False
    

for a in range(1,500):
    for b in range(2,500):
        for c in range(3,500):
            if is_py_triplet(a, b, c) and equals_1000(a, b, c):
                print(a*b*c)
                exit()