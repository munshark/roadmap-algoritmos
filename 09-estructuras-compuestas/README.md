# 09 – Estructuras compuestas: listas anidadas, tuplas y diccionarios

## Introducción  
Las estructuras compuestas son herramientas fundamentales en Python que permiten organizar y manipular datos de manera eficiente. Entre las más comunes se encuentran las listas anidadas, las tuplas y los diccionarios. Estas estructuras son esenciales para resolver problemas complejos y organizar información en programas.

## Subtemas  

### 1. **Listas anidadas (matrices)**  
- **¿Qué es una matriz?**  
    Una matriz es una lista que contiene otras listas como elementos, formando una estructura bidimensional. Y se utiliza para representar datos en filas y columnas, como una tabla. Y se define con corchetes dentro de corchetes `[[...], [...]]`.
- **Acceso a elementos con doble índice:**  
    ```python
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matriz[0][1])  # Resultado: 2
    ```
- **Ejemplo:**  
    ```python
    matriz = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
    ]
    print(matriz[1][2])  # Resultado: 6
    ```

### 2. **Tuplas**  
- **Diferencia con listas:**  
    Las tuplas son inmutables, lo que significa que no se pueden modificar después de ser creadas. Y son útiles para almacenar datos que no deben cambiar. Están definidas con paréntesis `()` en lugar de corchetes `[]`. 
- **Ejemplo de tupla:**  
    ```python
    coordenadas = (10, 20)
    print(coordenadas[0])  # Resultado: 10
    ```
- **Acceso a elementos por índice:**  
    ```python
    datos = ("nombre", "edad", "ciudad")
    print(datos[1])  # Resultado: edad
    ```

### 3. **Diccionarios**  
- **Estructura clave-valor:**  
    Los diccionarios almacenan datos en pares clave-valor, lo que permite un acceso rápido a la información. Y son útiles para representar datos que tienen una relación directa entre sí. Se definen con llaves `{}`.  
- **Acceso con claves:**  
    ```python
    persona = {"nombre": "Juan", "edad": 25}
    print(persona["nombre"])  # Resultado: Juan
    ```
- **Métodos comunes:**  
    ```python
    persona = {"nombre": "Ana", "edad": 30}
    print(persona.keys())   # Resultado: dict_keys(['nombre', 'edad'])
    print(persona.values()) # Resultado: dict_values(['Ana', 30])
    print(persona.items())  # Resultado: dict_items([('nombre', 'Ana'), ('edad', 30)])
    ```

## Actividades sugeridas  
1. Crear una matriz 3x3 y mostrar un elemento específico.  
2. Crear una tupla con 3 datos personales y mostrar uno.  
3. Crear un diccionario con información de un estudiante y mostrar sus valores.  

## Instrucciones para ejecutar el archivo `estructuras.py`  
1. Asegúrate de tener Python instalado en tu sistema.  
2. Guarda el archivo `estructuras.py` en la misma carpeta que este README.  
3. Abre una terminal y navega a la carpeta `09-estructuras-compuestas`.  
4. Ejecuta el archivo con el comando:  
     ```bash
     python3 estructuras.py
     ```  

¡Explora y experimenta con estas estructuras para mejorar tus habilidades en Python!  