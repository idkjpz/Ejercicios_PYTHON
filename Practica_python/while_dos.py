iterador = 1
ingreso_numero = 0
suma_numeros = 0
contador_vueltas = 0

while iterador <= 5:
    contador_vueltas += 1
    print(f"vuelta numero {contador_vueltas}" )
    ingreso_numero = int(input("Ingresa hasta 5 numeros: "))
    suma_numeros = suma_numeros + ingreso_numero
    promedio = suma_numeros / contador_vueltas
    iterador = iterador + 1

print(promedio)