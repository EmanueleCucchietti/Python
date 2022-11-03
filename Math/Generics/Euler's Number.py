import math
import sympy as sp
from decimal import *

e = Decimal(0)
e2 = Decimal(0)
precision = 1000

for i in range(0,precision):
    e += Decimal((1/math.factorial(i)))

print("Sommatoria di 1/fattoriale dell'indice incrementante: " + str(e))

def fe(x):
    return (1+1/x)^x
x = sp.symb

e2 = sp.limit(fe(x, x, oo))

print(e2)
