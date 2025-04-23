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

## Estructuras de control de repetición

Las estructuras de control de repetición permiten ejecutar un bloque de código varias veces, ya sea un número determinado de veces o hasta que se cumpla una condición específica. En Python, las estructuras de control de repetición más comunes son los bucles `for` y `while`.

### Bucle `for`

El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, una tupla o un rango). La sintaxis básica es la siguiente:

```python
for variable in secuencia:
    # Bloque de código a ejecutar en cada iteración
```

Para iterar sobre una secuencia de números, puedes utilizar la función `range()`. Por ejemplo:

```python
for i in range(5):
    print(i)
```

La función `range(5)` genera una secuencia de números del 0 al 4, y el bucle `for` imprime cada número en la consola. Range también puede aceptar un segundo argumento para especificar el número de inicio y un tercer argumento para especificar la secuencia de iteración. Por ejemplo, `range(1, 10, 2)` generará la secuencia 1, 3, 5, 7, 9.

Así pues, la función `range()` tiene la siguiente sintaxis:

```python
range(inicio, fin, paso)
```

Lo que pasa en un bucle `for` es que la variable toma el valor de cada elemento de la secuencia en cada iteración. Por ejemplo:

```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
```

En este ejemplo, el bucle `for` itera sobre la lista `numeros` y asigna cada número a la variable `numero`, que luego se imprime en la consola.

### Bucle `while`

El bucle `while` se utiliza para ejecutar un bloque de código mientras una condición sea verdadera. La sintaxis básica es la siguiente:

```python
while condición:
    # Bloque de código a ejecutar mientras la condición sea verdadera
```

El bucle `while` es útil cuando no se conoce de antemano cuántas veces se debe ejecutar el bloque de código. Por ejemplo:

```python
numero = int(input("Introduce un número: "))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input("Introduce otro número (0 para salir): "))
print("La suma es:", suma)
```

En este ejemplo, el bucle `while` se ejecuta mientras el usuario no introduzca 0. En cada iteración, se suma el número ingresado a la variable `suma` y se solicita un nuevo número al usuario.

### Instrucción `break`

La instrucción `break` se utiliza para salir de un bucle antes de que se complete su iteración. Esto puede ser útil si se cumple una condición específica y no es necesario continuar con el bucle. Por ejemplo:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

En este ejemplo, el bucle `for` se detiene cuando `i` es igual a 5, por lo que solo se imprimen los números del 0 al 4.

### Instrucción `continue`

La instrucción `continue` se utiliza para omitir la iteración actual de un bucle y continuar con la siguiente iteración. Esto puede ser útil si se desea saltar ciertos valores en una secuencia. Por ejemplo:

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

En este ejemplo, la instrucción `continue` se utiliza para omitir los números pares, por lo que solo se imprimen los números impares del 0 al 9.

## [Ejercicios de clase: estructuras de control condicionales](ejercicios_if_clase.md)

## [Ejercicios de clase: estructuras de control de repetición](ejercicios_for_while_clase.md)

## [Ejercicios prácticos (Nivel básico)](ejercicios_ut2_bas.md)

Asegúrate de leer atentamente cada ejercicio y de intentar resolverlo por tu cuenta antes de consultar las soluciones. Esto te ayudará a consolidar tus conocimientos y a mejorar tus habilidades de programación.
