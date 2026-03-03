# UT1: Fundamentos de Python

## Objetivos de la unidad

Al finalizar esta unidad serás capaz de:

- Comprender qué es Python y cómo se ejecuta.
- Escribir programas simples correctamente estructurados.
- Utilizar variables, tipos de datos y operadores.
- Gestionar entrada y salida de datos.
- Aplicar buenas prácticas básicas de programación.
- Interpretar y solucionar errores comunes.

---

## 1. ¿Qué es Python?

Python es un lenguaje de programación:

- Interpretado
- De alto nivel
- Multiparadigma (imperativo, orientado a objetos y funcional)
- De tipado dinámico
- Multiplataforma

Se utiliza en:

- Desarrollo web
- Automatización
- Ciencia de datos
- Inteligencia artificial
- Ciberseguridad
- DevOps

---

## 2. ¿Cómo se ejecuta un programa en Python?

Comprobar versión instalada:

```bash
python --version
```

Ejecutar un archivo:

```bash
python main.py
```

---

## 3. Entorno de desarrollo

Puedes programar en:

- VS Code
- PyCharm
- Jupyter Notebook

---

## 4. Sintaxis básica

### 4.1 Comentarios

Los comentarios son líneas que el intérprete ignora. Sirven para explicar el código a otros programadores (o a ti mismo en el futuro).

Existen dos tipos:

Comentario de una línea:

```python
# Esto es un comentario
```

Documentación (docstring):

```python
"""
Descripción del módulo o función.
"""
```

---

### 4.2 Variables

Las variables son contenedores para almacenar datos. En Python, no es necesario declarar el tipo de variable, ya que es un lenguaje de tipado dinámico. El tipo se asigna automáticamente según el valor que se le asigne.

Las variables reciben ese nombre ya que pueden cambiar su valor a lo largo del programa.

```python
nombre = "Jordi"
edad = 30
```

Para conocer el tipo de una variable, usamos la función `type()`:

```python
print(type(edad))
```

#### Reglas para nombres de variables

- No pueden empezar por número
- No pueden contener espacios
- No pueden usar palabras reservadas
- Se recomienda usar `snake_case`

Ejemplo correcto:

```python
precio_total = 19.99
```

---

### 4.3 Tipos de datos básicos

En Python existen varios tipos de datos básicos. Los datos básicos son aquellos que no se pueden descomponer en partes más pequeñas. Son los bloques de construcción de cualquier programa.

Los tipos de datos básicos más comunes en Python son:

#### Enteros

```python
x = 10
```

#### Flotantes

```python
pi = 3.1416
```

#### Cadenas de texto

```python
mensaje = "Hola mundo"
```

#### Booleanos

```python
activo = True
desactivado = False
```

---

### 4.4 Conversión de tipos

Los datos pueden convertirse de un tipo a otro usando funciones de conversión. Esta acción se llama **casting** o **casteo**. Debes tener cuidado al convertir tipos, ya que no todos los valores pueden convertirse a todos los tipos.

Por ejemplo, no podemos convertir una cadena de texto que no representa un número a un entero:

```python
edad = int("18")     # Esto funciona porque "18" es un número válido
edad = int("veinte") # Esto genera un error porque "veinte" no es un número
```

Un error común es intentar operar con tipos incompatibles, como sumar un número y una cadena de texto:

```python
"5" + 5  # TypeError
```

Las funciones de conversión más comunes son:

- `int()`: convierte a entero
- `float()`: convierte a flotante
- `str()`: convierte a cadena de texto
- `bool()`: convierte a booleano

---

## 5. Entrada y salida de datos

### 5.1 Salida con `print()`

```python
print("Hola mundo")
```

#### Uso profesional: f-strings

```python
nombre = "Ana"
print(f"Hola {nombre}")
```

---

### 5.2 Entrada con `input()`

```python
nombre = input("Introduce tu nombre: ")
```

⚠ `input()` siempre devuelve un `str`.

---

## 6. Operadores

### 6.1 Aritméticos

Los operadores aritméticos se utilizan para realizar operaciones matemáticas básicas. Los principales operadores aritméticos en Python son:

- `+` suma
- `-` resta
- `*` multiplicación
- `/` división
- `//` división entera (redondea hacia abajo)
- `%` módulo (resto de la división)
- `**` potencia

Ejemplo de uso:

```python
a = 10
b = 3
print(a + b)  # Suma: 13
print(a - b)  # Resta: 7
print(a * b)  # Multiplicación: 30
print(a / b)  # División: 3.3333...
print(a // b) # División entera: 3
print(a % b)  # Módulo: 1
print(a ** b) # Potencia: 1000
```

---

### 6.2 Comparación

Los operadores de comparación se utilizan para comparar dos valores y devuelven un valor booleano (`True` o `False`). Son fundamentales para controlar el flujo de un programa mediante estructuras condicionales.

Existen varios operadores de comparación:

- `==`: Igual a
- `!=`: Distinto de
- `<`: Menor que
- `>`: Mayor que
- `<=`: Menor o igual que
- `>=`: Mayor o igual que

Un ejemplo de uso sería:

```python
edad = 20
print(edad >= 18)  # Esto imprimirá True porque 20 es mayor o igual que 18
```

---

### 6.3 Lógicos

Los operadores lógicos se utilizan para combinar expresiones booleanas. Los principales operadores lógicos en Python son:

- `and`: Devuelve `True` si ambas expresiones son verdaderas.
- `or`: Devuelve `True` si al menos una de las expresiones es verdadera.
- `not`: Devuelve el valor contrario de la expresión.

---

### 6.4 Asignación compuesta

Los operadores de asignación permiten modificar el valor de una variable de forma más concisa. Por ejemplo:

```python
x = 5
x = x + 3  # Equivale a x = x + 3
```

Se puede escribir de forma más compacta usando el operador de asignación compuesto:

```python
x = 5
x += 3  # Esto es equivalente a x = x + 3
```

Los operadores de asignación compuesta disponibles son:

- `+=`: Suma y asigna
- `-=`: Resta y asigna
- `*=`: Multiplica y asigna
- `/=`: Divide y asigna
- `//=`: División entera y asigna
- `%=`: Módulo y asigna
- `**=`: Potencia y asigna

---

## 7. Indentación y bloques de código

Python no utiliza llaves `{}`.

La indentación define los bloques.

```python
edad = 20

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

Se recomienda usar **4 espacios**.

---

## 8. Errores comunes

### SyntaxError

Error de sintaxis.

### TypeError

Tipos incompatibles.

### NameError

Variable no definida.

### IndentationError

Problema con la indentación.

Aprender a leer el mensaje de error es fundamental.

---

## 9. Modelo mental: Cómo piensa un programa

Todo programa sigue este esquema:

1. Entrada de datos (Input)
2. Procesamiento (Process)
3. Salida de datos (Output)

Modelo IPO:

```
Input → Process → Output
```

Ejemplo:

```python
numero = int(input("Introduce un número: "))
resultado = numero * 2
print(f"El doble es {resultado}")
```

---

## 10. Buenas prácticas básicas

- Usar nombres descriptivos.
- Mantener el código limpio y legible.
- No repetir código innecesariamente.
- Comentar lo necesario, no lo obvio.
- Seguir la convención PEP8 (4 espacios, nombres en `snake_case`).

---

## [Ejercicios UT1](ejercicios_ut1.md)
