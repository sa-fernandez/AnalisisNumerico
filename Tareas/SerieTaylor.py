import math

def expAprox(x, t):
  a = math.exp(x)
  r = 0
  i = 0
  while(abs(a - r)>t):
    r = r + x**i/math.factorial(i)
    i = i + 1
  
  return r

print("Aproximacion de e^(2.5)->"+str(expAprox(2.5, 10**(-7))))