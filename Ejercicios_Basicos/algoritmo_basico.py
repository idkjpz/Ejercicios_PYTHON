"""
Este módulo clasifica a un jugador de baloncesto según su altura en centímetros.
"""
# A partir del ingreso de la altura en centímetros de un jugador de baloncesto

altura_jugador = int(input("Ingrese la altura del jugador basada en CM: "))
if altura_jugador < 160:
    print("base")
elif altura_jugador < 180:
    print("Escolta")
elif altura_jugador < 200:
    print("Alero")
else:
    print("Ala-Pivot")
