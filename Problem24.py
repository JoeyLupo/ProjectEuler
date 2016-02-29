from itertools import permutations
x = list(permutations(list('0123456789')))
print(''.join(x[999999]))