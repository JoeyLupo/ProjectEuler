
def is_palindrome(num):
    n_list = [int(c) for c in str(num)]
    l = len(n_list)
    for n in range(l//2):           
            if(n_list[n] != n_list[-(n+1)]):
                return False   
    return True

def get_range(num_digits):
    if num_digits < 1:
        print('Invalid number of digits')
        return 
    rng = []     
    maxim = int('1' + '0' * num_digits) - 1
    if num_digits == 1:
        minim = 0
    else: 
        minim = int('1' + '0' * (num_digits-1))
    
    rng.append(minim)
    rng.append(maxim)    
    return rng

def find_largest_palindrome(mn, mx):
    for x in range(mn,mx+1):
        for y in range(mn, mx+1):
            num = x*y
            if is_palindrome(num):
                yield num
    


mn,mx = get_range(3)  
largest = 0
a = find_largest_palindrome(mn, mx)

for num in a:
    if(num > largest):
        largest = num
        
print(largest)        