def evalDerivada(polinom, x):
  suma = multi = 0
  r = polinom[0]
  n = len(polinom)
  q = 0
  for i in range(1, n):
    q = r + x * q
    r = polinom[i] + x * r
    multi = multi + 2
    suma = suma + 2

  print ("\nEl resultado de la derivada del polinomio es: {} con un total de sumas: {} y un total de multiplicaciones:  {}".format(q, suma, multi))

def evalPoli(polinomio, x):
  suma = multi = 0
  r = polinomio[0]
  n = len(polinomio)
  for i in range (1, n):
    r = polinomio[i] + r * x
    multi = multi + 1
    suma = suma + 1

  print ("\nEl resultado del polinomio es: {} con un total de sumas: {} y un total de multiplicaciones:  {}".format(r, suma, multi))


def main ():
  repetir = True
  print("Bienvenido al programa que resuelve un polinomio con el método de Horner\n")
  while(repetir==True):
    polinomio = []
    gradoP = int(input("¿Cuál es el grado del polinomio?: "))
    aux = gradoP
    print("\nRecuerde ORDENAR el polinomio en forma DESCENDENTE")
    for i in range (0, (gradoP+1)):
      num = float(input("\nIngrese el coeficiente del x^{}: ".format(aux - i)))
      polinomio.append(num)

    x = float(input("\nIngrese el valor de X para el polinomio: "))
    evalPoli(polinomio, x)
    evalDerivada(polinomio, x)
    rta = input("\nDesea evaluar otro polinomio? s(si)/n(no): ")
    rta = rta.lower()
    if (rta=='n'):
      repetir=False

main()