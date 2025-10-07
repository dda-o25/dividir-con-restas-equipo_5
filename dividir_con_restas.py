"""
Larisa Carolina Alvarez Gonzalez

Diseña un programa para calcular el cociente y residuo de una división mediante restas sucesivas
"""

# Entradas
dividendo = int(input("Introduzca el dividendo: "))
divisor = int(input("Introduzca el divisor: "))


# Proceso
contador = 0
residuo = dividendo
while residuo >= divisor:
    residuo -= divisor
    contador += 1

cociente = contador


# Salidas
print(f"El cociente es {cociente}")
print(f"El residuo es {residuo}")
