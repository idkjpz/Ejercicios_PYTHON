"""Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos"""

contador_pares = 0
contador_impares = 0
menor_numero = 0 
pares_mayornumero = 0
suma_positivos = 0
producto_negativos = 0

for i in range (5):
    ingreso_numeros = int(input("Ingresa hasta 5 numeros: "))
    print(f"Numero ingresado {ingreso_numeros}")

    if ingreso_numeros % 2 == 0:
        contador_pares = contador_pares + 1
    else:
        contador_impares = contador_impares + 1

print(f"La cantidad de numeros par es {contador_pares}")
print(f"La cantidad de numeros impar es {contador_impares}")
