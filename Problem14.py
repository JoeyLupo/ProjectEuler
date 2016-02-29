
def collatz_gen(num):
    while True:
        if num == 0:
            print('Enter number > 0')
            return
        if num == 1:
            yield num
            steps_to_1 = 0
            break
        elif num % 2 == 0:
            yield num
            num //= 2
        else:
            yield num
            num = num * 3 + 1
            
 
max_steps = 0
answer = 0
for num in range(1,1000001):
    count = 1
    x = collatz_gen(num)
    for n in x:
        count += 1
    
    if count > max_steps:
        max_steps = count
        answer = num

           
print(answer)
"""

x = collatz_gen(837799)
count = 0
for n in x:
    count += 1 
print(count)
"""  