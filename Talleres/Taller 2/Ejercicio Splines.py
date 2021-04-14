import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt

#Ejercicio Splines
#Jose Calderon - Santiago Fernandez - Mariana Galavis - German Velasco
#Principales referencias durante el desarrollo del codigo:
#https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splprep.html#scipy.interpolate.splprep
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splev.html#scipy.interpolate.splev

#(Superior) Primera curva
x0 = np.array([1, 2, 5, 6, 7, 8, 10, 13, 17], float)
y0 = np.array([3, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5], float)
s0 = spi.splrep(x0, y0)
xn0 = np.linspace(1, 17, 100)
yn0 = spi.splev(xn0, s0)
#(Superior) Segunda curva
x1 = np.array([17, 20, 23, 24, 25, 27, 27.7], float)
y1 = np.array([4.5, 7, 6.1, 5.6, 5.8, 5.2, 4.1], float)
s1 = spi.splrep(x1, y1)
xn1 = np.linspace(17, 27.7, 100)
yn1 = spi.splev(xn1, s1)
#(Superior) Tercera curva
x2 = np.array([27.7, 28, 29, 30], float)
y2 = np.array([4.1, 4.3, 4.1, 3], float)
s2 = spi.splrep(x2, y2)
xn2 = np.linspace(27.7, 30, 100)
yn2 = spi.splev(xn2, s2)
#(Inferior) Primera curva
xi0 = np.array([1,3,5,7,8.5], float)
yi0 = np.array([3,2.7,2.7,2.7,3.2], float)
si0 = spi.splrep(xi0, yi0)
xni0 = np.linspace(1, 8.5, 100)
yni0 = spi.splev(xni0, si0)
#(Inferior) Segunda curva
xi1 = np.array([8,8.2,8.4,8.5], float)
yi1 = np.array([2.1,2.5,2.8,3.2], float)
si1 = spi.splrep(xi1, yi1)
xni1 = np.linspace(8, 8.5, 100)
yni1 = spi.splev(xni1, si1)
#(Inferior) Tercera curva
xi2 = np.array([8,8.4,9.5,10.7,11.5], float)
yi2 = np.array([2.1,1.8,1.7,2,1.7], float)
si2 = spi.splrep(xi2, yi2)
xni2 = np.linspace(8, 11.5, 100)
yni2 = spi.splev(xni2, si2)
#(Inferior) Cuarta curva
xi3 = np.array([11.5,13,14,14.5,15.5,16.5,17.5], float)
yi3 = np.array([1.7,1.5,1.6,1.7,1.7,1.7,1.7], float)
si3 = spi.splrep(xi3, yi3)
xni3 = np.linspace(11.5, 17.5, 100)
yni3 = spi.splev(xni3, si3)
#(Inferior) Quinta curva
xi4 = np.array([17.5, 17.7,18.5,18.7], float)
yi4 = np.array([1.7,1.5,1.5,1.7], float)
si4 = spi.splrep(xi4, yi4)
xni4 = np.linspace(17.5, 18.7, 100)
yni4 = spi.splev(xni4, si4)
#(Inferior) Sexta curva
xi5 = np.array([18.7,20,21.5,23.4,24.8], float)
yi5 = np.array([1.7,1.6,1.5,1.2,1.5], float)
si5 = spi.splrep(xi5, yi5)
xni5 = np.linspace(18.7, 24.8, 100)
yni5 = spi.splev(xni5, si5)
#(Inferior) Septima curva
xi6 = np.array([24.8,25,27.5,27.7,29,29.3,29.5, 30], float)
yi6 = np.array([1.5,1.5,2.6,2.8,2.6, 2.8,2.7,3], float)
si6 = spi.splrep(xi6, yi6)
xni6 = np.linspace(24.8, 30, 100)
yni6 = spi.splev(xni6, si6)


#Grafica de acuerdo con los resultados
plt.plot(x0, y0, 'ko', xn0, yn0, 'r--', x1, y1, 'ro', xn1, yn1, 'g--', x2, y2, 'mo', xn2, yn2, 'b--')
plt.plot(xi0, yi0, 'ko', xni0, yni0, 'r--', xi1, yi1, 'ro', xni1, yni1, 'g--', xi2, yi2, 'mo', xni2, yni2, 'b--', xi3, yi3, 'go', xni3, yni3, 'k--', xi4, yi4, 'bo', xni4, yni4, 'm--',xi5, yi5, 'ro', xni5, yni5, 'b--',xi6, yi6, 'o', xni6, yni6, 'k--')
plt.show()