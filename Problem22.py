letter_val = dict(zip([chr(a) for a in range(97,123)],[val for val in range(1,27)]))
names = []
total = 0
def val_name(name):
    value = 0
    for let in name:
        value += letter_val[let]
    
    return(value)

with open('names.txt', 'r') as f:
    names = [n.strip('"').lower() for n in f.readline().split(",")]
    names.sort()
    
    
for i,name in enumerate(names):
    total += (i+1)*val_name(name)    
    
print(total)