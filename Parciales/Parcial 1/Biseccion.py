import sympy as sp

def biseccion(f, a, b, t):
    c, i = 0, 0
    if(f.evalf(subs={x: a}) * f.evalf(subs={x: b}) >= 0):
        return None
    while(abs(b - a) > t):
        c = (a + b) / 2
        
        if(f.evalf(subs={x: c}) == 0):
            break

        if(f.evalf(subs={x: a}) * f.evalf(subs={x: c}) < 0):
            b = c
        else:
            a = c

        i += 1

    print("Numero de iteraciones: {}".format(i))

    return c

x = sp.Symbol('x')
#f = (sp.cos(x))**2 - x**2
#f = x*sp.sin(x) - 1
#f = x**3 - 2*x**2 + (4/3)*x - (8/27)
#f= (9.8*68.1)/x * 1 - sp.exp(-(x/68.1)*10) - 40
#f = x**3 - 2*x - 5
print("Metodo Biseccion")
a = float(input("\nIngrese el primer punto del intervalo: "))
b = float(input("\nIngrese el segundo punto del intervalo: "))
print("\nLa funcion {} tiene un cero en el punto x = {} en el intervalo [{}, {}]".format(f, biseccion(f, a, b, 10 ** (-7)), a, b))