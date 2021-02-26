from scipy import optimize

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html
#https://github.com/scipy/scipy/blob/v1.6.1/scipy/optimize/zeros.py#L650-L777
#https://github.com/scipy/scipy/blob/5ab7426247900db9de856e790b8bea1bd71aec49/scipy/optimize/zeros.py#L70

def f(x):
    return x**3 - 2*x**2 + (4/3)*x - (8/27)

a = float(input("\nIngrese el primer punto: "))
b = float(input("\nIngrese el segundo punto: "))
x0 = float(input("\nIngrese el punto inicial x0: "))
r, q = optimize.brentq(f, a, b, xtol = 2**(-50), full_output = 1)
t, v = optimize.newton(f, x0, tol = 2**(-50), full_output = 1)
print("\nRaiz Metodo Brent = {}".format(r))
print("Numero iteraciones Metodo Brent = {}".format(q.iterations))
print("\nRaiz Metodo Newton = {}".format(t))
print("Numero iteraciones Metodo Newton = {}".format(v.iterations))