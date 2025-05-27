# Operadores Lógicos en Python

## Objetivo del módulo

Comprender cómo usar los operadores `and`, `or` y `not` para construir condiciones compuestas y tomar decisiones lógicas en un programa.

---

## ¿Qué son los operadores lógicos?

Los operadores lógicos permiten combinar condiciones para tomar decisiones más complejas en tus programas. En Python, los principales operadores lógicos son:

| Operador | Significado | Ejemplo en palabras |
|----------|-------------|--------------------|
| `and`    | Y           | Es verdadero si ambas condiciones son verdaderas |
| `or`     | O           | Es verdadero si al menos una condición es verdadera |
| `not`    | No          | Invierte el valor de verdad de una condición |

---

## Tabla de verdad

| A     | B     | A and B | A or B | not A |
|-------|-------|---------|--------|-------|
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |

---

## Actividad central: Diseña el juego de Cachipún (Piedra, Papel o Tijera)

### Descripción del problema

Imagina que quieres crear el clásico juego de Cachipún (también conocido como Piedra, Papel o Tijera) para que una persona juegue contra la computadora. El objetivo es que el jugador y la CPU elijan una opción y, según las reglas, se determine quién gana cada ronda.

### Instrucciones

1. **Describe las reglas del juego en texto:** Antes de programar, escribe claramente cómo se gana, se pierde o se empata en Cachipún.
2. **Determina las condiciones a verificar:** Piensa qué situaciones debes comprobar para saber quién gana cada ronda.
3. **Construye la lógica antes del código:** Usa operadores lógicos (`and`, `or`, `not`) para imaginar cómo comparar las jugadas y decidir el resultado.

El objetivo es que puedas diseñar la lógica del juego usando operadores lógicos, ¡sin preocuparte aún por la sintaxis!

---

## Sugerencias de pasos

- Cuales son las jugadas posibles: piedra, papel, tijera.
- ¿Cómo se gana? (Piedra gana a Tijera, Tijera gana a Papel, Papel gana a Piedra).
- Haz que la CPU elija una jugada al azar.

---

## Desafío adicional

Agrega una opción secreta llamada `"diosito"` que siempre gane, sin importar la jugada de la CPU.

---

**¡Recuerda que lo más importante es que seas capaz de pensar cómo resolver el problema!**