import numpy as np
import scipy.interpolate as spi

#Ejercicio Splines
#Santiago Fernandez - Mariana Galavis - German Velasco
#Principales referencias durante el desarrollo del codigo:
#https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.lagrange.html

x = np.array([4410000, 4830000, 5250000, 5670000], float)
y = np.array([1165978, 1329190, 1501474, 1682830], float)
x1 = np.array([4830000, 5250000, 5670000], float)
y1 = np.array([1329190, 1501474, 1682830], float)
f = spi.interp1d(x, y)
l2 = spi.lagrange(x1, y1)
l3 = spi.lagrange(x, y)
print("La cuota por impuesto de renta por interpolacion lineal es de = {}".format(f(5000000)))
print("La cuota por impuesto de renta por interpolacion cuadratica es de = {}".format(l2(5000000)))
print("La cuota por impuesto de renta por interpolacion cubica es de = {}".format(l3(5000000)))