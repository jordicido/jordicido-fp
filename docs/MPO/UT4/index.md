# UT4: Funciones y módulos

## Introducción

Bienvenid@s a la Unidad de Trabajo 4 (UT4) del módulo profesional optativo (MPO) de Python. En esta unidad, nos centraremos en el concepto de funciones y módulos, dos elementos fundamentales para estructurar y organizar nuestro código de manera eficiente.
Las funciones nos permiten encapsular bloques de código que realizan tareas específicas, mientras que los módulos nos permiten agrupar funciones relacionadas en archivos separados, facilitando la reutilización y el mantenimiento del código.

Perfecto. A continuación tienes el **material teórico ampliado** sobre **funciones en Python**, pensado para alumnado de **1º de DAM**, en el módulo de **Programación**. Incluye definiciones detalladas, analogías, ejemplos comentados y consejos didácticos.

## Funciones

Una **función** es un **bloque de código con nombre** que se puede ejecutar cuando se necesite. Sirve para **resolver una tarea específica** y puede recibir datos (llamados *parámetros*) y devolver un resultado (*valor de retorno*).

**Piensa en una función como una máquina**:
Le das ingredientes (parámetros), hace un trabajo (instrucciones), y puede darte un resultado (valor de retorno).

### Ventajas de usar funciones

* **Reutilización de código**: Escribes una vez, usas muchas.
* **Modularidad**: Puedes dividir un programa en partes más pequeñas, claras y fáciles de entender.
* **Facilita la prueba de errores**: Puedes probar una función de forma aislada.
* **Mejora la legibilidad**: Los programas con funciones bien nombradas se entienden mejor.

## ¿Cómo se define una función en Python?

### Sintaxis básica

```python
def nombre_funcion(parámetros):
    """Descripción de lo que hace la función (opcional pero recomendable)"""
    instrucciones
    return valor  # opcional
```

### Detalle de cada parte

* `def`: palabra reservada que indica que se va a definir una función.
* `nombre_funcion`: identificador que le damos a la función. Se recomienda usar minúsculas y guiones bajos (`snake_case`) si tiene varias palabras.
* `parámetros`: variables que recibe la función como entrada (pueden ser cero o más).
* `return`: sirve para **devolver** un resultado desde la función (es opcional).

## Ejemplos

### Ejemplo 1: Función sin parámetros ni retorno

```python
def saludar():
    print("Hola, bienvenido al curso de DAM")

saludar()
```

> Esta función no necesita datos externos. Simplemente ejecuta una instrucción (mostrar un mensaje).

### Ejemplo 2: Función con parámetros

```python
def saludar_persona(nombre):
    print(f"Hola, {nombre}. ¡Bienvenido!")

saludar_persona("Laura")
```

> Aquí, la función recibe un valor externo (`nombre`) y lo usa para personalizar el saludo. Los **parámetros** permiten hacer funciones más flexibles.

### Ejemplo 3: Función con retorno (`return`)

```python
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(5, 3)
print("La suma es:", total)
```

> Esta función **devuelve un valor**. La palabra clave `return` se usa para **enviar el resultado** de vuelta al lugar donde fue llamada.
Es muy útil cuando necesitamos que la función nos diga el resultado de su operación.

### Ejemplo 4: Función con valores por defecto

```python
def saludar(nombre="invitado"):
    print(f"Hola, {nombre}")

saludar()           # Hola, invitado
saludar("Carlos")   # Hola, Carlos
```

> Si el usuario no proporciona un valor, se usa el **valor por defecto** (`"invitado"`). Esto hace que la función sea más flexible.

### Ejemplo 5: Función con múltiples valores de retorno

```python
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

x, y = operaciones(10, 4)
print("Suma:", x)
print("Resta:", y)
```

> Python permite devolver **varios valores separados por comas**, y luego se pueden recoger en varias variables.

## Buenas prácticas al crear funciones

* Usa nombres descriptivos: que indiquen claramente qué hace la función (`calcular_area`, `obtener_precio`, etc.).
* Añade comentarios o **docstrings** (`"""texto"""`) para explicar la función.
* Divide tareas complejas en varias funciones más simples.
* No dependas de variables externas (globales) dentro de una función.
* Procura que cada función haga una sola cosa. Esto se llama el principio de **responsabilidad única**.

## ¿Cuándo usar funciones?

* Siempre que tengas código que se repite
* Siempre que una parte del programa pueda separarse y probarse sola
* Cuando quieras organizar tu programa de forma modular

## [Ejercicios de clase: funciones](ejercicios_funciones_clase.md)
