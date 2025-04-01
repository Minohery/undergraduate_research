import matplotlib.pyplot as plt

c = float(input("Dmaping coefficient? "))
m = float(input("Mass m? "))
k = float(input("Spring coefficient? "))
y0 = float(input("Initial position? "))
ydot0 = float(input("Initiana velocity? "))
r = float(input("Desired position? "))
f0 = float(input("Initial force? "))
Ki = float(input("Integrator coefficient? "))
dt = float(input("Value of step? "))
tlimit = float(input("Duration of simulation? "))

end = False

y = y0
ydot = ydot0
f = f0
t0 = 0
t = t0
ylist = [y0]
flist = [f0]
tlist = [0]
x0 = ydot0
x = x0

def xdot(f, ydot, y):
    return f/m-c*ydot/m-k/m*y

while  t+dt <= tlimit:
    t += dt
    tlist += [t]
    e = r-y
    f += Ki*dt*e
    flist += [f]
    xdot = 1/m*f-c/m*ydot-k/m*y
    x += xdot*dt
    y += x*dt
    ylist += [y]
    ydot = x

plt.plot(tlist, ylist)
plt.show()
