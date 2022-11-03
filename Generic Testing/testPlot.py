from sympy import symbols, sympify
import sympy as sp
from mpmath import radians
from matplotlib import pyplot as plt
 
x = symbols("x")

IsRadians = True
XPreValue = 3
XActualValue = None
if(IsRadians):
    XActualValue = XPreValue
else:
    XActualValue = radians(XPreValue)

ax = []
ay = []
string = '2*x + 5'
expr2 = "sqrt(sin(log(x^2 + 1) + cos(180)))"
expr = sympify(string)
 
#print(expr)
#print(expr.subs(x, XActualValue))

expr = sympify(expr2)
#print(expr)
print(expr.subs(x, XActualValue))
print(sp.N(expr.subs(x, XActualValue)))
s = sp.N(expr.subs(x, XActualValue))
print(s)

for i in range(0,100):
    f = sp.N(expr.subs(x, i))
    print(type(f))
    ax.append(i) 
    ay.append(f)

s = sp.N(expr.subs(x,XActualValue))


plt.plot(ax, ay)
plt.show()