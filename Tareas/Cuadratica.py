import math

def cuadratica(a, b, c, s):
    if s == '+':
        return ((-b + math.sqrt(b**2 - 4*a*c))/(2*a))

    if s == '-':
        return ((-b - math.sqrt(b**2 - 4*a*c))/(2*a))

def cuadraticaMod(a, b, c, s):
    if s == '+':
        return ((-2*c)/(b + math.sqrt(b**2 - 4*a*c)))

    if s == '-':
        return ((-2*c)/(b - math.sqrt(b**2 - 4*a*c)))

print("Formula Cuadratica->"+str(cuadratica(1, 9**12, -3, '+')))
print("Formula Cuadratica con conjugado->"+str(cuadraticaMod(1, 9**12, -3, '+')))