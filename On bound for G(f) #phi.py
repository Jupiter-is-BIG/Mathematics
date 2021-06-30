import math
from math import gcd
from sympy.ntheory.factor_ import totient
from fractions import gcd
from functools import reduce
def f(n):
    return 27*(n**3)+9*(n**2)+3*n+1 #poly
n=1
l=[]
while n<250:
    l.append(totient(f(n)))
    n=n+1
print(reduce(gcd,l))
