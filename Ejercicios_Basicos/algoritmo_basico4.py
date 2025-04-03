"""
Este módulo contiene un ejercicio para clasificar a una persona según su edad.
"""

edad_ingresada = int(input("Por favor ingrese su edad: "))
if edad_ingresada <= 12:
    print(f"Ud tiene {edad_ingresada} y es menor ")
elif edad_ingresada <= 17:
    print(f"Ud tiene {edad_ingresada} y es adolescente")
else:
    print(f"Ud es mayor de edad, tiene {edad_ingresada}")
