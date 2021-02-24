import sympy as sp
import matplotlib.pyplot as plt

def graficaError(arr, t):
    arr1 = []
    arr1.append(0)
    for i in range (0, len(arr)-1):
        arr1.append(arr[i])

    plt.plot(arr, arr1, linewidth=0.8)
    plt.xlabel('x - Ei')
    plt.ylabel('y - Ei+1')
    plt.title("Comportamiento del Error en {}".format(t))
    plt.show()

def biseccion(f, a, b, t):
    c, i = 0, 0
    if(f.evalf(subs={x: a}) * f.evalf(subs={x: b}) >= 0):
        return None
    while(i <= t):
        c = (a + b) / 2
        
        if(f.evalf(subs={x: c}) == 0):
            break

        if(f.evalf(subs={x: a}) * f.evalf(subs={x: c}) < 0):
            b = c
        else:
            a = c

        i += 1

    return c

def ralstonRabinowitz(f, h, e):
    df = sp.diff(f)
    dff = sp.diff(df)
    n, i, num, den = 0, 0, 0, 0
    t = h
    if(h == None):
        print("\nEl metodo de Newton-Raphson no puede ser aplicado")
        return None
    n = h - ((f.evalf(subs={x: h})) / (df.evalf(subs={x: h})))
    error = abs(n - h)
    arr = []
    while(error > e):
        num = (f.evalf(subs={x: h}) * df.evalf(subs={x: h}))
        den = ((df.evalf(subs={x: h}))**2 - f.evalf(subs={x: h}) * dff.evalf(subs={x: h}))
        n = h - (num / den)

        if(f.evalf(subs={x: h}) == 0):
            break
        
        if(df.evalf(subs={x: h}) == 0):
            print("\nEl metodo de Newton-Raphson no puede ser aplicado")
            return None

        error = abs(n - h)
        h = n
        i += 1
        arr.append(error)

    print("\nLa funcion {} tiene un cero en el punto x = {} con punto x0 = {} con {} iteraciones".format(f, n, t, i))
    graficaError(arr, "Newton-Raphson (Modificado)")

def nrAitken(f, h, e):
    df = sp.diff(f)
    n, r, i, mx = 0, 0, 0, 0
    t = h
    if(h == None):
        print("\nEl metodo de Newton-Raphson no puede ser aplicado")
        return None
    n = h - ((f.evalf(subs={x: h})) / (df.evalf(subs={x: h})))
    error = abs(n - h)
    arr = []
    while(error > e):
        n = h - ((f.evalf(subs={x: h})) / (df.evalf(subs={x: h})))
        r = n - ((f.evalf(subs={x: n})) / (df.evalf(subs={x: n})))

        if(f.evalf(subs={x: h}) == 0):
            break
        
        if(df.evalf(subs={x: h}) == 0):
            print("\nEl metodo de Newton-Raphson no puede ser aplicado")
            return None

        error = abs(n - h)
        
        if ((n - h)**2 / (h - 2*n + r)) == sp.nan:
            break

        h = h - ((n - h)**2 / (h - 2*n + r))
        i += 1
        mx += 1
        if mx == 100:
            print("\nEl metodo de Newton-Raphson no puede ser aplicado")
            return None
        
        arr.append(error)

    print("\nLa funcion {} tiene un cero en el punto x = {} con punto x0 = {} con {} iteraciones".format(f, h, t, i))
    graficaError(arr, "Newton-Raphson (Aitken)")

def newtonRaphson(f, h, e):
    df = sp.diff(f)
    n, i, mx = 0, 0, 0
    t = h
    print(h)
    if(h == None):
        print("\nEl metodo de Newton-Raphson no puede ser aplicado")
        return None
    
    n = h - ((f.evalf(subs={x: h})) / (df.evalf(subs={x: h})))
    error = abs(n - h)
    arr = []
    while(error > e):
        n = h - ((f.evalf(subs={x: h})) / (df.evalf(subs={x: h})))

        if(f.evalf(subs={x: h}) == 0):
            break
        
        if(df.evalf(subs={x: h}) == 0):
            print("\nEl metodo de Newton-Raphson no puede ser aplicado")
            return None

        error = abs(n - h)
        h = n
        i += 1
        mx += 1
        if mx == 100:
            print("\nEl metodo de Newton-Raphson no puede ser aplicado")
            return None

        arr.append(error)

    print("\nLa funcion {} tiene un cero en el punto x = {} con punto x0 = {} con {} iteraciones".format(f, n, t, i))
    graficaError(arr, "Newton-Raphson")

x = sp.Symbol('x')
rep = True
f = x
while rep:
    print("\nFUNCIONES DISPONIBLES")
    print("a. f(x) = (cos(x))^2 - x^2")
    print("b. f(x) = x*sin(x) - 1")
    print("c. f(x) = x^3 - 2x^2 + 4/3x - 8/27")
    print("d. f(x) = ((9.8*68.1)/x)*1-e^(-(x/68.1)*10)-40")
    print("e. f(x) = x^3 - 2x - 5")
    op = input("\nOpcion a elegir: ")
    op.lower()
    if op == 'a':
        f = (sp.cos(x))**2 - x**2
    elif op == 'b':
        f = x*sp.sin(x) - 1
    elif op == 'c':
        f = x**3 - 2*x**2 + (4/3)*x - (8/27)
    elif op == 'd':
        f= (9.8*68.1)/x * 1 - sp.exp(-(x/68.1)*10) - 40
    elif op == 'e':
        f = x**3 - 2*x - 5
    else:
        print("\nRespuesta no valida, intente de nuevo")

    p = sp.plot(f, line_color = "red", title = "Grafica de la funcion f(x) = {}".format(f))
    a = float(input("\nIngrese el primer punto del intervalo: "))
    b = float(input("\nIngrese el segundo punto del intervalo: "))
    e = float(input("\nIngrese numero de iteraciones de biseccion: "))
    w = float(input("\nIngrese el valor de la toleracia 10^-x: "))

    print("\nMetodo Newton-Raphson")
    newtonRaphson(f, biseccion(f, a, b, e), 10 ** (-w))
    print("\nMetodo Newton-Raphson (Aitken)")
    nrAitken(f, biseccion(f, a, b, e), 10**(-w))
    print("\nMetodo Newton-Raphson (Modificado)")
    ralstonRabinowitz(f, biseccion(f, a, b, e), 10**(-w))

    rta = input("\nDesea evaluar otra funcion? s(si)/n(no): ")
    rta = rta.lower()
    if (rta == 'n'):
        rep = False