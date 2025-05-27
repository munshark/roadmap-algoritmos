# pruebas_logicas.py
# Práctica de operadores lógicos en Python

# Operadores lógicos:
# - and: Devuelve True solo si ambas condiciones son verdaderas.
# - or: Devuelve True si al menos una condición es verdadera.
# - not: Invierte el valor lógico (True a False, False a True).

# Ejemplo 1: Combinando dos variables booleanas
a = True
b = False

# ¿Qué debería imprimirse aquí?
print("a and b:", a and b)

# Cambia los valores de a y b y predice el resultado antes de ejecutar.
# print("a or b:", a or b)

# Ejemplo 2: Usando not
# ¿Qué debería imprimirse aquí?
print("not a:", not a)

# Ejemplo 3: Condiciones con números y cadenas
edad = 20
tiene_carnet = "si"

# ¿Qué debería imprimirse aquí?
print("¿Es mayor de edad y tiene cédula?", edad >= 18 and tiene_carnet == "si")

# Cambia el valor de edad o tiene_carnet y predice el resultado antes de ejecutar.

# Ejemplo 4: Combinando or y and
es_estudiante = True
tiene_descuento = False

# ¿Qué debería imprimirse aquí?
print("¿Puede obtener descuento?", es_estudiante or tiene_descuento)

# Ejemplo 5: Usando not con una condición compuesta
# ¿Qué debería imprimirse aquí?
print("¿No es mayor de edad o no tiene cédula?", not (edad >= 18 and tiene_carnet == "si"))

# Cambia las variables y predice el resultado antes de ejecutar.