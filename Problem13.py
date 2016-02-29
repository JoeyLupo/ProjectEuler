total = 0

with open('sum.txt', 'r') as f:
    for line in f:
        total += int(line)
        
print(str(total)[:10])        