import numpy as np
import sympy as sp

#Taller Sistemas Lineales
#Jose Calderon - Santiago Fernandez - Mariana Galavis - German Velasco
#Principales referencias durante el desarrollo del codigo:
#https://numpy.org/doc/stable/reference/routines.linalg.html

def infectados(v):
    x = sp.symbols('x')
    f = v[0] * x+ v[1] * x **2 + v[2] * sp.exp(0.15 * x)
    rta = 0
    numero = 0
    while (rta < 1500 or rta > 1600):
        rta = f.evalf(subs={x:numero})
        numero = numero + 1

    print ("\nEl día en que los infectados es igual a {} es el numero {}".format(int(rta), numero - 1))

def evalPositivaDefinida(e):
    return np.all(np.linalg.eigvals(e) > 0)

def evalDiagonalDominante(a):
    d = np.diag(np.abs(a))
    s = np.sum(np.abs(a), axis=1)
    if np.all(d > s):
        return True
    else:
        return False

def sor(a, b, w, tol):
    n = len(b)
    x = np.ones(n, float)
    r = np.zeros(n, float)
    e = (np.linalg.norm(x - r, np.inf)) / (np.linalg.norm(x, np.inf))
    suma = 0
    while(e > tol):
        for i in range(n):
            suma = 0
            r[i] = x[i]
            for j in range(n):
                if j != i:
                    suma += a[i, j] * x[j]

            x[i] = ((1 - w) * x[i]) + (w * (b[i] - suma)) / a[i, i]

        e = (np.linalg.norm(x - r, np.inf)) / (np.linalg.norm(x, np.inf))

    return x

def gaussSeidel(a, b, tol):
    n = len(b)
    x = np.ones(n, float)
    r = np.zeros(n, float)
    e = (np.linalg.norm(x - r, np.inf)) / (np.linalg.norm(x, np.inf))
    suma = 0
    while(e > tol):
        for i in range(n):
            suma = 0
            r[i] = x[i]
            for j in range(n):
                if j != i:
                    suma = suma + a[i, j] * x[j]

            x[i] = (b[i] - suma) / a[i, i]

        e = (np.linalg.norm(x - r, np.inf)) / (np.linalg.norm(x, np.inf))

    return x

print("Taller Sistemas Lineales")
t = float(input("\nIngrese el valor de la tolerancia: "))
rep = True
while(rep):
    a = np.array([[10, 10**2, np.exp(0.15 * 10)], [15, 15**2, np.exp(0.15 * 15)], [20, 20**2, np.exp(0.15 * 20)]], float)
    b = np.array([25, 190, 950], float)
    
    print("\nMatriz propuesta para solución:")
    print(a)
    print("\nVector de terminos independientes:")
    print(b)
    if evalDiagonalDominante(a) or evalPositivaDefinida(a):
        print("\nArreglo solución (Gauss-Seildel):")
        v = gaussSeidel(a, b, t)
        print(v)
    else:
        print("\nEl metodo de Gauss-Seidel no converge")

    if evalPositivaDefinida(a):
        print("\nArreglo solución (SOR):")
        #print("Con valor w = {}".format(print(calculoW(a))))
        w = float(input("\nIngrese el valor del parametro w: "))
        v = sor(a, b, w, t)
        print(v)
    else:
        print("\nEl metodo SOR no converge")

    infectados(v)
    rta = input("\nDesea evaluar otro valor de w? s(si)/n(no): ")
    rta = rta.lower()
    if (rta == 'n'):
        rep = False