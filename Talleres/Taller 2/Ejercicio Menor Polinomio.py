import numpy as np
import sympy as sp
import scipy.interpolate as spi
import matplotlib.pyplot as plt

xn = np.array([0, 1, 2], float)
y = np.array([10.5, 15.33, 5.789], float)
dydx = np.array([1, (y[1]-y[0])/(xn[1]-xn[0]), (y[2]-y[1])/(xn[2]-xn[1])], float)
a = spi.CubicHermiteSpline(xn, y, dydx)
arr = np.array([a.c[0,0],a.c[1,0],a.c[2,0],a.c[3,0]])
x = sp.Symbol('x')
fun = arr[0]*x**0 + arr[1]*x**1 + arr[2]*x**2 + arr[3]*x**3
xnew = np.linspace(0, 2, 50)
plt.plot(xnew, a(xnew), 'r--')
plt.show()
print("La funcion del MENOR grado tres que pasa por los puntos es f(x) = {}".format(fun))