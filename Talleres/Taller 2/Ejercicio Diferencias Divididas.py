import numpy as np
import math

#Ejercicio Splines
#Jose Calderon - Santiago Fernandez - Mariana Galavis - German Velasco
#Principales referencias durante el desarrollo del codigo:
#https://es.wikipedia.org/wiki/Interpolaci%C3%B3n_polin%C3%B3mica_de_Newton

def diferenciasDivididas(x, y):
    n = len(y)
    div = np.zeros([n, n])
    div[:,0] = y
    for j in range(1, n):
        for i in range(n - j):
            if x[i+j] == x[i]:
                div[i][j] = 1 / math.factorial(i)
            else:
                div[i][j] = (div[i+1][j-1] - div[i][j-1]) / (x[i+j]-x[i])
            
    return div

x = np.array([0, 0, 1, 2], float)
y = np.array([10.5, 10.5, 15.33, 5.789], float)
arr = diferenciasDivididas(x, y)
print("Matriz resultado de diferencias divididas")
print(arr)