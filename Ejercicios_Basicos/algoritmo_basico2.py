"""
Este módulo clasifica las notas de un alumno según su valor numérico.
"""
nota_ingresada = int(input("Ingrese la nota del alumno:"))
if nota_ingresada >= 1 and nota_ingresada < 4:
    print(f"Desaprobado la nota es {nota_ingresada}")
elif nota_ingresada <= 5:
    print(f"Aprobado la nota es {nota_ingresada}")
elif nota_ingresada <= 10:
    print(f"Promocion directa la nota es {nota_ingresada}")
else:
    print("dato incorrecto.")
