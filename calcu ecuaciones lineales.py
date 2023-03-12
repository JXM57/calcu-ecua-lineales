print("Calculadora de Ecuaciones linales")

# Pedir los coeficientes

a = float(input("Introduce el coeficiente de x: "))
b = float(input("Introduce el coeficiete de y:" ))   
c = float(input("Introduce el termino independiente:"))

# Calcular El resultado
if a == 0 and b == 0:
    print("La ecuacion no tiene solucion.")
elif a == 0:
    print("La ecuacion tiene solucion unica: y =", c/b)
elif b == 0:
    print("La ecuacion tiene solucion unica:x, =", c/a)
else:
    print("la solucuon de la ecuacuon es:x =", (c-b/a, "y =", (c-a)/b))

