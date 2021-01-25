from itertools import count
from math import factorial

def factor_gen():
    for el in count(1):
        yield factorial(el)

gener = factor_gen()
x = 0
for i in gener:
    if x < 4:
        print(i)
        x += 1
    else:
        break
