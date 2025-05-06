# 01 – Variables en Python

## ¿Qué es una variable en programación?

Una variable es un espacio en la memoria de la computadora que se utiliza para almacenar datos. Es como una caja con un nombre, donde puedes guardar información que luego puedes usar o modificar.

## ¿Por qué usar variables?

Las variables son fundamentales en programación porque nos permiten:
- Guardar información para usarla más tarde.
- Hacer que nuestro código sea más flexible y reutilizable.
- Representar datos de manera clara y organizada.

## Reglas básicas para nombrar variables en Python

1. El nombre debe comenzar con una letra o un guion bajo (`_`).
2. No puede comenzar con un número.
3. Solo puede contener letras, números y guiones bajos.
4. Es sensible a mayúsculas y minúsculas (`edad` y `Edad` son diferentes).
5. No puede usar palabras reservadas de Python como `print`, `if`, `else`, etc.

## Ejemplos de variables en Python

```python
# Variables de diferentes tipos
nombre = "Ana"       # str (cadena de texto)
edad = 25            # int (número entero)
altura = 1.68        # float (número decimal)
es_estudiante = True # bool (valor booleano)

# Mostrar las variables
print(nombre)
print(edad)
print(altura)
print(es_estudiante)
```

## Asignar un valor vs. mostrarlo con `print()`

- **Asignar**: Es cuando le das un valor a una variable, como `edad = 25`.
- **Mostrar**: Es cuando usas `print()` para ver el valor de la variable en la pantalla.

Por ejemplo:
```python
# Asignar un valor
mensaje = "Hola mundo"

# Mostrar el valor
print(mensaje)
```

## Actividad sugerida

1. Crea un archivo llamado `variables.py`.
2. Dentro del archivo, define 4 variables: una de tipo `str`, una de tipo `int`, una de tipo `float` y una de tipo `bool`.
3. Usa `print()` para mostrar el valor de cada variable.
4. Asegúrate de seguir las reglas para nombrar variables que mencionamos antes.
5. Guarda el archivo y ejecútalo para ver los resultados.

## Cómo ejecutar el archivo `variables.py`

1. Asegúrate de tener Python instalado en tu computadora.
2. Guarda el archivo `variables.py` en una carpeta.
3. Abre una terminal o consola.
4. Navega a la carpeta donde guardaste el archivo.
5. Escribe el siguiente comando y presiona Enter:
    ```bash
    python3 variables.py
    ```

¡Listo! Deberías ver los valores de tus variables en la pantalla.  