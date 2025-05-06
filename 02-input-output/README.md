# 02 – Entrada y salida de datos

En este módulo aprenderás cómo interactuar con el usuario a través de la entrada y salida de datos en Python. Usaremos las funciones `input()` para recibir datos y `print()` para mostrarlos.

## Entrada de datos: `input()`
La función `input()` permite al usuario ingresar datos desde el teclado. Estos datos siempre se reciben como texto (tipo `str`).

Ejemplo:
```python
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
```

## Salida de datos: `print()`
La función `print()` se utiliza para mostrar información en la pantalla.

## Conversión de tipos
Si necesitas trabajar con números, puedes convertir el texto ingresado con `input()` a otro tipo de dato, como `int` o `float`.

Ejemplo:
```python
edad = int(input("Edad: "))
print("Tu edad es:", edad)
```

## Formas de concatenar texto en Python
Existen tres formas principales de combinar texto en Python:

1. **Usando comas `,` dentro de `print()`**  
    Las comas permiten combinar texto y variables sin necesidad de conversión de tipo.  
    ```python
    print("Hola,", nombre, "tienes", edad, "años.")
    ```

2. **Usando el operador `+`**  
    Requiere que todos los elementos sean cadenas de texto (`str`). Si no lo son, debes convertirlos.  
    ```python
    print("Hola, " + nombre + ". Tienes " + str(edad) + " años.")
    ```

3. **Usando f-strings**  
    Es la forma más moderna y recomendada. Permite insertar variables directamente dentro de una cadena.  
    ```python
    print(f"Hola, {nombre}. Tienes {edad} años.")
    ```

## Actividad sugerida
1. Pide al usuario su nombre y edad.
2. Muestra un saludo utilizando las tres formas de concatenación explicadas.

Ejemplo:
```python
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

# Forma 1: Usando comas
print("Hola,", nombre, "tienes", edad, "años.")

# Forma 2: Usando +
print("Hola, " + nombre + ". Tienes " + str(edad) + " años.")

# Forma 3: Usando f-strings
print(f"Hola, {nombre}. Tienes {edad} años.")
```

## Cómo ejecutar el archivo `entrada_salida.py`
1. Asegúrate de tener Python instalado en tu computadora.
2. Guarda el código en un archivo llamado `entrada_salida.py`.
3. Abre una terminal o consola.
4. Navega hasta la carpeta donde guardaste el archivo.
5. Ejecuta el archivo con el comando:  
    ```bash
    python3 entrada_salida.py
    ```

¡Diviértete aprendiendo Python!  