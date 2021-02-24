def evalDevPoli(polinom, x):
    

def evalPoli(polinom, x):
    n = len(polinom)
    r = polinom[0]
    suma = 0
    multi = 0
    for i in range (1, n):
        r = polinom[i] + r*x
        if polinom[i] != 0:
            suma += 1
        
        multi += 1
    
    print("Polinomio -> "+polinomio(polinom)+" evaluado en "+str(x)+" = "+str(r)+" Sumas -> "+str(suma)+" Multiplicaciones -> "+str(multi))

evalPoli([2, 0, -3, 3, -4], 0.5)
evalPoli([2, 1, -3, 3, -4], 1)