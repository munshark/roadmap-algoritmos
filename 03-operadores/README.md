# 03 – Operadores en Python

## Introducción  
En programación, un operador es un símbolo que indica una operación específica que se debe realizar sobre uno o más valores. Los operadores son fundamentales para realizar cálculos, comparaciones y asignaciones en Python.

## Tipos de Operadores  

### 1. Operadores Matemáticos  
Los operadores matemáticos permiten realizar operaciones aritméticas básicas:  
- `+` Suma  
- `-` Resta  
- `*` Multiplicación  
- `/` División  
- `%` Módulo (resto de una división)  
- `**` Potencia  
- `//` División entera (resultado sin decimales)  

**Ejemplo:**  
```python
a = 10
b = 3
print(a + b)  # Suma
print(a - b)  # Resta
print(a * b)  # Multiplicación
print(a / b)  # División
print(a % b)  # Módulo
print(a ** b) # Potencia
print(a // b) # División entera
```

### 2. Operadores Comparativos  
Los operadores comparativos se utilizan para comparar valores y devuelven un valor booleano (`True` o `False`):  
- `==` Igual a  
- `!=` Distinto de  
- `<` Menor que  
- `>` Mayor que  
- `<=` Menor o igual que  
- `>=` Mayor o igual que  

**Ejemplo:**  
```python
x = 5
y = 10
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False
print(x <= y)  # True
print(x >= y)  # False
```

### 3. Diferencia entre Asignar (`=`) y Comparar (`==`)  
- `=` se utiliza para asignar un valor a una variable.  
- `==` se utiliza para comparar si dos valores son iguales.  

**Ejemplo:**  
```python
a = 5  # Asignación
b = 5
print(a == b)  # Comparación: True
```

## Actividad Sugerida  
1. Solicita al usuario que ingrese dos números.  
2. Aplica cada operador matemático y muestra el resultado con `print()`.  
3. Compara los números ingresados y muestra si son iguales, distintos, mayor o menor.  

**Ejemplo de código:**  
```python
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Operadores matemáticos
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)
print("Módulo:", num1 % num2)
print("Potencia:", num1 ** num2)
print("División entera:", num1 // num2)

# Operadores comparativos
print("¿Son iguales?", num1 == num2)
print("¿Son distintos?", num1 != num2)
print("¿El primero es mayor?", num1 > num2)
print("¿El primero es menor?", num1 < num2)
```

## Notas Importantes  
- El operador `%` devuelve el resto de una división.  
- El operador `**` calcula potencias.  
- El operador `//` realiza una división entera, descartando los decimales.  

## Instrucciones para Ejecutar  
1. Crea un archivo llamado `operadores.py`.  
2. Copia y pega el código de la actividad sugerida en el archivo.  
3. Abre una terminal y navega hasta la carpeta donde se encuentra el archivo.  
4. Ejecuta el archivo con el comando:  
    ```bash
    python3 operadores.py
    ```
