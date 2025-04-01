import math
import matplotlib.pyplot as plt

xmax = float(input("Max value of x? "))
x0 = float(input("Value of x0? "))
y0 = float(input("Value of y0?" ))
dx = float(input("Value of step dx? "))
x = x0
y = y0


def real(x):
    return x**2*math.exp(x)

def dydx(x):
    return 2*x*math.exp(x)+x**2*math.exp(x)

Euler_ylist = [y0]
Real_ylist = [real(x0)]
xlist = [x0]

while x + dx <= xmax:
    y = y + dydx(x)*dx
    x = x + dx
    Euler_ylist += [y]
    Real_ylist += [real(x)]
    xlist += [x]

print("Euler list: ", Euler_ylist)
print("Real list: ", Real_ylist)
plt.plot(xlist, Euler_ylist, "-b", label="Euler")
plt.plot(xlist, Real_ylist, "-r", label="Analytical")
plt.legend(loc="upper left")
plt.show()




    
    
