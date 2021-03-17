import numpy as np
from scipy.linalg import lu

def crearVector():
    n = 80
    v = np.zeros(n, float)
    for i in range(0, n):
        v[i] = np.pi

    return v

def crearMatriz():
    n = 80
    m = np.zeros((n, n), float)
    for i in range(n):
        for j in range(n):
            if (j + 1 == i + 1 and (i + 1 >= 1 and i + 1 <= 80)):
                m[i, j] = 2 * (i + 1)
            elif (j + 1 == i + 1 + 2 and (i + 1 >= 1 and i + 1 <= 78)) or (j + 1 == i + 1 - 2 and (i + 1 >= 3 and i + 1 <= 80)):
                m[i, j] = 0.5 * (i + 1)
            elif (j + 1 == i + 1 + 4 and (i + 1 >= 1 and i + 1 <= 76)) or (j + 1 == i + 1 - 4 and (i + 1 >= 5 and i + 1 <= 80)):
                m[i, j] = 0.25 * (i + 1)
            else:
                m[i, j] = 0
            
    return m

def calculoW(a):
    p, l, u = lu(a)
    q = l + u
    d = np.linalg.inv(np.diagflat(np.diag(a)))
    t = np.dot(d, q)
    u = np.amax(np.linalg.eigvals(t))
    if u**2 < 1:
        return 2 / (1 + np.sqrt(1 - u**2))
    else:
        return None

def evalDiagonalDominante(a):
    d = np.diag(np.abs(a))
    s = np.sum(np.abs(a), axis=1)
    if np.all(d > s):
        return True
    else:
        return False

def evalPositivaDefinida(e):
    return np.all(np.linalg.eigvals(e) > 0)

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
                    suma += a[i, j] * x[j]

            x[i] = (b[i] - suma) / a[i, i]

        e = (np.linalg.norm(x - r, np.inf)) / (np.linalg.norm(x, np.inf))

    return x

print("Taller Punto 6")
t = float(input("\nIngrese el valor de la tolerancia: "))
rep = True
while(rep):
    a = crearMatriz()
    b = crearVector()

    print("\nMatriz propuesta para solución:")
    print(a)
    print("\nVector de terminos independientes:")
    print(b)
    if evalDiagonalDominante(a) or evalPositivaDefinida(a):
        print("\nArreglo solución (Gauss-Seildel):")
        print(gaussSeidel(a, b, t))
    else:
        print("\nEl metodo de Gauss-Seidel no converge")

    if evalPositivaDefinida(a):
        print("\nArreglo solución (SOR):")
        #print("Con valor w = {}".format(print(calculoW(a))))
        w = float(input("\nIngrese el valor del parametro w: "))
        print(sor(a, b, w, t))
    else:
        print("\nEl metodo SOR no converge")
    
    rta = input("\nDesea evaluar otro valor de w? s(si)/n(no): ")
    rta = rta.lower()
    if (rta == 'n'):
        rep = False