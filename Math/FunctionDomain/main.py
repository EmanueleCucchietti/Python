from sympy import Symbol, S
from sympy.calculus.util import continuous_domain
from sympy import *
import sympy

x = Symbol("x")
f = tan(x)
domain = continuous_domain(f, x, S.Reals)

print(isinstance(domain,sympy.sets.sets.Complement)) # returns Complement(Reals, Union(ImageSet(Lambda(_n, 2*_n*pi + pi/2), Integers), ImageSet(Lambda(_n, 2*_n*pi + 3*pi/2), Integers)))
print(type(domain.args[1])) # returns Union(ImageSet(Lambda(_n, 2*_n*pi + pi/2), Integers), ImageSet(Lambda(_n, 2*_n*pi + 3*pi/2), Integers))
print(type(domain.args[1].args[0])) # returns ImageSet(Lambda(_n, 2*_n*pi + pi/2), Integers)
print(type(domain.args[1].args[0].args[0])) # returns Lambda(_n, 2*_n*pi + pi/2)
print(type(domain.args[1].args[0].args[0](0))) # returns the evaluation of the function at _n = value passed

"""
IDEA
ricorsive function that given a domain returned from continuous_domain will scan in search of the range of the function
will unpack it to find a lambda function or an interval
will get the type of the domain and either unpack it or evaluate it
"""

def getNegativeRange(index = -1, arr=[], maxValue = -100):
    # recursively call this function until the value of the function at n is less than -100
    f = float(domain.args[1].args[0].args[0](index))
    if f > maxValue:
        arr.append(f)
        getNegativeRange(index-1, arr, maxValue)
    return arr

def getPositiveRange(index = 0, arr=[], minValue = 100):
    # recursively call this function until the value of the function at n is greater than 100
    f = float(domain.args[1].args[0].args[0](index))
    if f < minValue:
        arr.append(f)
        getPositiveRange(index+1, arr, minValue)
    return arr

def getRange(index = 0, arr=[], minValue = 100, maxValue = -100):
    # recursively call this function until the value of the function at n is greater than 100
    znegative = getNegativeRange()
    zpositive = getPositiveRange()
    return znegative + zpositive



#zpositive = []
#znegative = []
## populate the list zpositive with the values of the function at n so as to the list zpositive contains all values in the range [0,100]
#i=1
#while domain.args[1].args[0].args[0](i) < 100:
#    z.append(domain.args[1].args[0].args[0](i))
#    i=i+1
# populate the list znegative with the values of the function at n so as to the list znegative contains all values in the range [-100,0]
#i=0
#while domain.args[1].args[0].args[0](i) > -100:
#    z.append(domain.args[1].args[0].args[0](i))
#    i=i-1

zx = getRange(minValue = -100, maxValue = 100)
zx.sort()
for i in zx:
    print(float(i))