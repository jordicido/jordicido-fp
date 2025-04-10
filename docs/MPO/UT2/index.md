# UT2: Estructuras de control

## Introducción

Bienvenid@s a la Unidad de Trabajo 2 (UT2) del módulo profesional optativo (MPO) de Python. En esta unidad, nos centraremos en las estructuras de control, que son fundamentales para el desarrollo de programas en Python. Aprenderás a utilizar estructuras de control de flujo y repetición para crear programas más complejos y eficientes.
A lo largo de esta unidad, exploraremos las diferentes estructuras de control disponibles en Python, incluyendo condicionales (`if`, `elif`, `else`) y bucles (`for`, `while`). También aprenderás a utilizar la instrucción `break` para salir de un bucle y la instrucción `continue` para omitir una iteración.

## Estructuras de control de flujo

Las estructuras de control de flujo permiten tomar decisiones en función de condiciones específicas. En Python, las estructuras de control de flujo más comunes son las condicionales `if`, `elif` y `else`. Estas estructuras permiten ejecutar diferentes bloques de código según si una condición es verdadera o falsa.

### Estructura `if`

La estructura `if` se utiliza para evaluar una condición y ejecutar un bloque de código si la condición es verdadera. La sintaxis básica es la siguiente:

```python
if condición:
    # Bloque de código a ejecutar si la condición es verdadera
```

### Estructura `elif`

La estructura `elif` (abreviatura de "else if") se utiliza para evaluar múltiples condiciones. Si la primera condición es falsa, se evalúa la siguiente condición `elif`. La sintaxis básica es la siguiente:

```python
if condición1:
    # Bloque de código a ejecutar si condición1 es verdadera
elif condición2:
    # Bloque de código a ejecutar si condición2 es verdadera
```

### Estructura `else`

La estructura `else` se utiliza para ejecutar un bloque de código si todas las condiciones anteriores son falsas. La sintaxis básica es la siguiente:

```python
if condición1:
    # Bloque de código a ejecutar si condición1 es verdadera
elif condición2:
    # Bloque de código a ejecutar si condición2 es verdadera
else:
    # Bloque de código a ejecutar si todas las condiciones anteriores son falsas
```

### Ejemplo de estructura de control de flujo

```python
edad = int(input("Introduce tu edad: "))
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de edad.")
```

En este ejemplo, se solicita al usuario que introduzca su edad y se evalúa en qué categoría de edad se encuentra. Dependiendo de la edad ingresada, se imprime un mensaje diferente.

## [Ejercicios de clase: estructuras de control condicionales](ejercicios_if_clase.md)

## [Ejercicios prácticos (Nivel básico)](ejercicios_ut2_bas.md)

Asegúrate de leer atentamente cada ejercicio y de intentar resolverlo por tu cuenta antes de consultar las soluciones. Esto te ayudará a consolidar tus conocimientos y a mejorar tus habilidades de programación.
