import numpy as np
from scipy import optimize

#Reto 1
#Analisis Numerico
#Jose Calderon - Santiago Fernandez - Mariana Galavis - German Velasco
#Principales referencias durante el desarrollo del codigo:
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html
#https://github.com/scipy/scipy/blob/v1.6.1/scipy/optimize/zeros.py#L650-L777
#https://github.com/scipy/scipy/blob/5ab7426247900db9de856e790b8bea1bd71aec49/scipy/optimize/zeros.py#L70

def f(x):
    return x**3 - 2*x**2 + (4/3)*x - (8/27)

def fun(x):
    return [x[0]**2 + x[0]*x[1] - 10, x[1] + 3*x[0]*x[1]**2 - 57]

def gun(x):
    return [(x[0] + 2)**2 + (x[1] - 2)**2 - 1, x[1] + (x[0] + 2)**2 - 3]

def hun(x):
    return [4*x[0]**3 - x[1]*np.exp(x[1]), 2*x[0]*np.exp(x[0]) + x[1]**2 - 2]

def aplicarMetodosNL(f, x, y):
    try:
        print("Resultado con la funcion fsolve = {}".format(optimize.fsolve(f, [x, y], xtol = 2**(-16))))
    except Exception as e:
        print("El metodo fsolve no converge")
    try:
        print("Resultado mediante el metodo de Newton-Krylov = {}".format(optimize.newton_krylov(f, [x, y], x_tol = 2**(-16))))
    except Exception as e:
        print("El metodo de Newton-Krylov no converge")

    try:
        print("Resultado mediante el metodo de Broyden 1 = {}".format(optimize.broyden1(f, [x, y], x_tol = 2**(-16))))
    except Exception as e:
        print("El metodo de Broyden 1 no converge")

    try:
        print("Resultado mediante el metodo de Broyden 2 = {}".format(optimize.broyden2(f, [x, y], x_tol = 2**(-50))))
    except Exception as e:
        print("El metodo de Broyden 2 no converge")

print("Reto 1")
print("\nPRIMER PUNTO - ALGORITMO DE BRENT")
rep1 = True
while rep1:
    print("\nFuncion a evaluar: x^3 - 2x^2 + 4x/3 - 8/27")
    a = float(input("\nIngrese el primer punto: "))
    b = float(input("Ingrese el segundo punto: "))
    x0 = float(input("(N)Ingrese el punto inicial x0: "))
    r, q = optimize.brentq(f, a, b, xtol = 2**(-50), full_output = 1)
    t, v = optimize.newton(f, x0, tol = 2**(-50), full_output = 1)
    print("\nRaiz Metodo Brent = {}".format(r))
    print("Numero iteraciones Metodo Brent = {}".format(q.iterations))
    print("\nRaiz Metodo Newton = {}".format(t))
    print("Numero iteraciones Metodo Newton = {}".format(v.iterations))
    print("Diferencia entre Newton y Brent es de {}".format(abs(r - t)))
    print("\nDiferencia del metodo de Brent con el resultado de wolfram = {}".format(abs(r-(2/3))))
    print("\nDiferencia del metodo de Newton con el resultado de wolfram = {}".format(abs(t-(2/3))))
    rta1 = input("\nDesea evaluar otro intervalo? s(si)/n(no): ")
    rta1 = rta1.lower()
    if (rta1 == 'n'):
        rep1 = False

print("\nSEGUNDO PUNTO - INTERSECCION ENTRE CURVAS")
rep2 = True
while rep2:
    print("\na. [1] x^2 + xy = 10 [2] y + 3xy^2 = 57")
    print("\nb. [1] (x + 2)^2 + (y - 2)^2 = 1 [2] y + (x + 2)^2 = 3")
    print("\nc. [1] 4x^3 + ye^y = 0 [2] 2xe^x+y^2 - 2 = 0")
    op = input("\nOpcion a elegir: ")
    x = float(input("\nIngrese el valor de x: "))
    y = float(input("Ingrese el valor de y: "))
    op.lower()
    if op == 'a':
        aplicarMetodosNL(fun, x, y)
    elif op == 'b':
        aplicarMetodosNL(gun, x, y)
    elif op == 'c':
        aplicarMetodosNL(hun, x, y)

    rta2 = input("\nDesea evaluar otro intervalo y/o funcion? s(si)/n(no): ")
    rta2 = rta2.lower()
    if (rta2 == 'n'):
        rep2 = False