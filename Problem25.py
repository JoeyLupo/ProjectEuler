def F():
    a,b = 1,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
        
fib = F()
count = 0
x = 1
while(len(str(x)) != 1000):
    x = next(fib)
    count+=1
  
print(count)    