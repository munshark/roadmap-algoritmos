# 04 – Condicionales en Python

Las estructuras condicionales permiten que un programa tome decisiones basadas en ciertas condiciones. Son fundamentales para controlar el flujo de ejecución en Python y en cualquier lenguaje de programación.

## ¿Qué es una estructura condicional?

Una estructura condicional evalúa una condición (una expresión que puede ser verdadera o falsa) y ejecuta un bloque de código dependiendo del resultado. Esto permite que el programa responda de manera dinámica a diferentes situaciones.

## Sintaxis básica

En Python, las estructuras condicionales más comunes son `if`, `else` y `elif`. Por otro lado también existen las estructuras `switch` y `case`, pero no son nativas de Python. En su lugar, se pueden usar diccionarios o múltiples `if` y `elif` para lograr un comportamiento similar.

```python
if condicion:
    # Código a ejecutar si la condición es verdadera
elif otra_condicion:
    # Código a ejecutar si la otra condición es verdadera
else:
    # Código a ejecutar si ninguna de las condiciones anteriores es verdadera
```

## Evaluación de condiciones

Las condiciones en Python se evalúan como verdaderas (`True`) o falsas (`False`). Por ejemplo:

- `x > 0` es verdadero si `x` es mayor que 0.
- `x == 0` es verdadero si `x` es igual a 0.
- `x % 2 == 0` es verdadero si `x` es divisible entre 2 (número par).

## Ejemplo práctico

Pedir la edad de un usuario y determinar si es mayor de edad:

```python
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

## Actividad sugerida

1. Escribe un programa que:
   - Pida al usuario un número.
   - Muestre si el número es positivo, negativo o cero.
   - Indique si el número es par o impar.

2. Guarda tu código en un archivo llamado `condicionales.py`.

## Cómo ejecutar el archivo

Guarda el archivo `condicionales.py` en la misma carpeta que este README. Para ejecutarlo, abre una terminal y escribe:

```bash
python3 condicionales.py
```

¡Buena suerte aprendiendo condicionales en Python!  