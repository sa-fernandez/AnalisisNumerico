import math
import sympy

def cifras(v, c):
  return round(v, c - int(math.floor(math.log10(abs(v)))) - 1)

def aprox(v, a, n):
  x = sympy.Symbol('x')
  ex = x**(1/2)
  r = ex.evalf(subs={x: a})
  for i in range(1, n + 1):
    ex = sympy.diff(ex)
    r = r + ((ex.evalf(subs={x: a})/math.factorial(i))*(v - a)**i)

  return cifras(r, 8)

for i in range(2, 12):
  print("Aproximacion de sqrt(0.0088) con n="+str(i)+"->"+str(aprox(0.0088, 0.5, i)))