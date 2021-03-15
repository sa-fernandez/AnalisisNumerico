import numpy as np

#Taller Sistemas Lineales
#Jose Calderon - Santiago Fernandez - Mariana Galavis - German Velasco
#Principales referencias durante el desarrollo del codigo:
#https://numpy.org/doc/stable/reference/routines.linalg.html

def evalPositivaDefinida(e):
    for k in e:
        if(k < 0 or isinstance(k, complex)):
            return False

    return True

def evalDiagonalDominante(a):
    d = np.diag(np.abs(a))
    s = np.sum(np.abs(a), axis=1)
    if np.all(d > s):
        return True
    else:
        return False

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
rep = True
while(rep):
    t = float(input("\nIngrese el valor de la tolerancia: "))
    a = np.array([[10, 10**2, np.exp(0.15 * 10)], [15, 15**2, np.exp(0.15 * 15)], [20, 20**2, np.exp(0.15 * 20)]], float)
    b = np.array([25, 190, 950], float)

    print("\nMatriz propuesta para solución:")
    print(a)
    print("\nArreglo solución (Gauss-Seildel):")
    print(gaussSeidel(a, b, t))
    rta = input("\nDesea evaluar otro sistema? s(si)/n(no): ")
    rta = rta.lower()
    if (rta == 'n'):
        rep = False