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

- **Interpretado**: el código se ejecuta línea a línea, sin necesidad de compilarlo antes.
- **De alto nivel**: su sintaxis se parece mucho al inglés natural, lo que lo hace fácil de leer.
- **Multiparadigma**: puedes programar de forma imperativa, orientada a objetos o funcional.
- **De tipado dinámico**: no necesitas decirle a Python qué tipo de dato es una variable, lo detecta solo.
- **Multiplataforma**: funciona en Windows, Linux y macOS sin cambios.

Se utiliza en sectores muy variados:

- Desarrollo web (Django, FastAPI)
- Automatización de tareas repetitivas
- Ciencia de datos e inteligencia artificial
- Ciberseguridad y hacking ético
- DevOps y administración de sistemas

!!! tip "¿Por qué aprender Python?"
    Python es el lenguaje más utilizado en el mundo según los índices TIOBE y Stack Overflow. Aprenderlo bien te abre las puertas a prácticamente cualquier área de la informática.

---

## 2. ¿Cómo se ejecuta un programa en Python?

Antes de nada, comprueba que tienes Python instalado:

```bash
python --version
```

Verás algo como `Python 3.12.x`. Si aparece un error, necesitas instalar Python desde [python.org](https://python.org).

Para ejecutar un archivo:

```bash
python main.py
```

!!! note "¿Python o Python3?"
    En algunos sistemas (especialmente Linux y macOS) puede que necesites escribir `python3` en lugar de `python`. En Windows suele funcionar directamente `python`.

---

## 3. Entorno de desarrollo

Puedes programar en cualquier editor de texto, pero para este módulo recomendamos:

- **VS Code** — gratuito, ligero y con soporte excelente para Python. Es la opción recomendada.
- PyCharm — muy completo, pero más pesado. Ideal cuando ya tengas más experiencia.
- Jupyter Notebook — útil para ciencia de datos y experimentos rápidos.

!!! tip "Configuración recomendada en VS Code"
    Instala la extensión oficial de **Python** (de Microsoft). Te dará resaltado de sintaxis, autocompletado y la posibilidad de ejecutar el código directamente desde el editor.

---

## 4. Sintaxis básica

### 4.1 Comentarios

Los comentarios son líneas que Python ignora al ejecutar el código. Sirven para explicar qué hace el código, tanto a otros como a ti mismo cuando lo releas días después.

Comentario de una línea (empieza con `#`):

```python
# Esto es un comentario, Python lo ignora completamente
nombre = "Jordi"  # También puedes ponerlos al final de una línea
```

Comentario de varias líneas (docstring, con comillas triples):

```python
"""
Este programa calcula el área de un círculo.
Autor: Jordi
Fecha: 2025
"""
```

!!! tip "¿Cuándo comentar?"
    Comenta el **por qué**, no el **qué**. Si el código ya es claro, no hace falta explicarlo. Un buen comentario aclara la intención detrás de una decisión.

---

### 4.2 Variables

Una variable es como una **caja con etiqueta** en la que guardas información. La etiqueta es el nombre de la variable y el contenido es su valor.

```python
nombre = "Jordi"   # caja llamada "nombre" que contiene el texto "Jordi"
edad = 30          # caja llamada "edad" que contiene el número 30
```

Se llaman "variables" porque su contenido puede **cambiar** a lo largo del programa:

```python
edad = 30
print(edad)   # 30
edad = 31
print(edad)   # 31
```

Para saber qué tipo de dato tiene una variable, usa `type()`:

```python
print(type(edad))    # <class 'int'>
print(type(nombre))  # <class 'str'>
```

#### Reglas para nombres de variables

| Regla | Ejemplo correcto | Ejemplo incorrecto |
|-------|-----------------|-------------------|
| No pueden empezar por número | `precio1` | `1precio` |
| No pueden contener espacios | `precio_total` | `precio total` |
| No pueden ser palabras reservadas | `total` | `if`, `for`, `while`... |
| Solo letras, números y `_` | `mi_variable` | `mi-variable`, `mi.variable` |

!!! tip "Convención: snake_case"
    En Python se recomienda usar `snake_case` para los nombres de variables: todas las letras en minúscula y las palabras separadas por guión bajo. Ejemplo: `precio_total`, `nombre_alumno`, `numero_intentos`.

---

### 4.3 Tipos de datos básicos

Cada variable tiene un **tipo** que determina qué clase de información almacena y qué operaciones puedes hacer con ella.

| Tipo | Nombre | Ejemplo |
|------|--------|---------|
| Entero | `int` | `edad = 25` |
| Decimal | `float` | `precio = 9.99` |
| Texto | `str` | `nombre = "Ana"` |
| Booleano | `bool` | `activo = True` |

Ejemplos:

```python
# Entero (int): números sin decimales
edad = 25

# Flotante (float): números con decimales
precio = 9.99
temperatura = -3.5

# Cadena de texto (str): cualquier texto entre comillas
nombre = "Ana"
apellido = 'García'   # También puedes usar comillas simples

# Booleano (bool): solo puede ser True o False (con mayúscula inicial)
activo = True
tiene_deuda = False
```

!!! warning "Las cadenas siempre van entre comillas"
    `nombre = Ana` daría un error porque Python buscaría una variable llamada `Ana`. Siempre usa comillas: `nombre = "Ana"`.

---

### 4.4 Conversión de tipos (casting)

A veces necesitas convertir un dato de un tipo a otro. A esto se le llama **casting**.

```python hl_lines="2 3 6"
# De texto a número
edad = int("18")       # "18" (str) → 18 (int)
precio = float("9.99") # "9.99" (str) → 9.99 (float)

# De número a texto
texto = str(42)        # 42 (int) → "42" (str)
```

Esto es especialmente útil con `input()`, que **siempre devuelve texto**:

```python hl_lines="1"
edad = int(input("¿Cuántos años tienes? "))  # convierte la respuesta a entero
```

!!! warning "No puedes convertir cualquier texto a número"
    ```python
    edad = int("veinte")  # ¡Error! "veinte" no es un número válido
    edad = int("20")      # Correcto
    ```

---

## 5. Entrada y salida de datos

### 5.1 Salida con `print()`

```python
print("Hola mundo")
print(42)
print(True)
```

La forma más moderna y recomendada de mostrar variables es usando **f-strings**:

```python hl_lines="3"
nombre = "Ana"
edad = 20
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
# Resultado: Hola, me llamo Ana y tengo 20 años.
```

Las f-strings empiezan con una `f` antes de las comillas y permiten insertar variables directamente entre `{}`.

---

### 5.2 Entrada con `input()`

`input()` pausa el programa y espera a que el usuario escriba algo y pulse Enter:

```python
nombre = input("Introduce tu nombre: ")
print(f"Hola, {nombre}!")
```

!!! warning "`input()` siempre devuelve texto (`str`)"
    Aunque el usuario escriba un número, `input()` lo devuelve como texto. Si quieres operar con él matemáticamente, conviértelo:
    ```python
    numero = int(input("Introduce un número: "))
    ```

---

## 6. Operadores

### 6.1 Aritméticos

```python hl_lines="8 9 10"
a = 10
b = 3

print(a + b)   # Suma:            13
print(a - b)   # Resta:            7
print(a * b)   # Multiplicación:  30
print(a / b)   # División:         3.333...
print(a // b)  # División entera:  3  (descarta los decimales)
print(a % b)   # Módulo (resto):   1  (10 = 3×3 + 1)
print(a ** b)  # Potencia:      1000  (10³)
```

!!! tip "¿Para qué sirve el módulo `%`?"
    El operador `%` devuelve el **resto** de una división entera. Es muy útil para saber si un número es par o impar:
    ```python
    numero = 7
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")   # Este se imprime
    ```

---

### 6.2 Comparación

Comparan dos valores y devuelven `True` o `False`:

```python
edad = 20

print(edad == 18)   # False  (¿es igual a 18?)
print(edad != 18)   # True   (¿es distinto de 18?)
print(edad > 18)    # True   (¿es mayor que 18?)
print(edad < 18)    # False  (¿es menor que 18?)
print(edad >= 18)   # True   (¿es mayor o igual que 18?)
print(edad <= 18)   # False  (¿es menor o igual que 18?)
```

!!! warning "`=` no es lo mismo que `==`"
    - `=` **asigna** un valor a una variable: `edad = 20`
    - `==` **compara** si dos valores son iguales: `edad == 20`

    Confundirlos es uno de los errores más frecuentes al empezar.

---

### 6.3 Lógicos

Combinan condiciones booleanas:

```python
edad = 20
tiene_carnet = True

# and: las DOS condiciones deben ser True
print(edad >= 18 and tiene_carnet)   # True

# or: al menos UNA debe ser True
print(edad >= 18 or tiene_carnet)    # True

# not: invierte el resultado
print(not tiene_carnet)              # False
```

---

### 6.4 Asignación compuesta

Forma abreviada de modificar el valor de una variable:

```python
x = 10
x += 3    # equivale a: x = x + 3  →  x vale 13
x -= 2    # equivale a: x = x - 2  →  x vale 11
x *= 2    # equivale a: x = x * 2  →  x vale 22
x /= 4    # equivale a: x = x / 4  →  x vale 5.5
```

---

## 7. Indentación y bloques de código

En Python la **indentación** (los espacios al inicio de una línea) es parte de la sintaxis. Define qué código pertenece a qué bloque.

```python hl_lines="3 6 9"
edad = 20

if edad >= 18:
    print("Mayor de edad")   # este print está DENTRO del if
    print("Puedes votar")    # este también
else:
    print("Menor de edad")   # este está dentro del else

print("Esto siempre se ejecuta")  # este está FUERA del if/else
```

!!! warning "Usa siempre 4 espacios"
    Python acepta cualquier cantidad de espacios, pero en la misma parte del código deben ser **consistentes**. Lo estándar (PEP8) son **4 espacios**. No mezcles espacios y tabulaciones.

---

## 8. Errores comunes

Cuando un programa falla, Python muestra un mensaje de error. Aprender a **leerlos** es una habilidad fundamental. No te asustes, son tus mejores aliados para depurar.

### SyntaxError — error de sintaxis

Python no entiende lo que has escrito. Suele ser una falta de paréntesis, dos puntos, o una palabra mal escrita.

```python
print("Hola"    # falta el paréntesis de cierre
```

```
SyntaxError: '(' was never closed
```

---

### TypeError — tipos incompatibles

Estás intentando operar con tipos que no son compatibles.

```python
edad = 20
print("Tengo " + edad + " años")  # no puedes sumar str con int
```

```
TypeError: can only concatenate str (not "int") to str
```

Solución: convierte el número a texto con `str()`:

```python
print("Tengo " + str(edad) + " años")
# O mejor aún, usa f-strings:
print(f"Tengo {edad} años")
```

---

### NameError — variable no definida

Estás usando una variable que no existe (o la has escrito mal).

```python
print(nmobre)   # la variable se llama "nombre", no "nmobre"
```

```
NameError: name 'nmobre' is not defined
```

---

### IndentationError — indentación incorrecta

La indentación no es consistente.

```python
if True:
print("Hola")   # falta la indentación
```

```
IndentationError: expected an indented block after 'if' statement
```

!!! tip "Cómo leer un error"
    Un mensaje de error de Python siempre te dice:

    1. **El tipo de error** (`TypeError`, `NameError`...)
    2. **El archivo y la línea** donde ocurre
    3. **Una descripción** del problema

    Lee siempre la **última línea** del error primero: es la descripción más concreta.

---

## 9. Modelo mental: cómo piensa un programa

Todo programa, por complejo que sea, sigue este esquema:

```
Entrada de datos → Procesamiento → Salida de resultados
     (Input)         (Process)          (Output)
```

Ejemplo práctico — programa que calcula el doble de un número:

```python hl_lines="2 5 8"
# INPUT: pedimos el dato al usuario
numero = int(input("Introduce un número: "))

# PROCESS: calculamos
resultado = numero * 2

# OUTPUT: mostramos el resultado
print(f"El doble de {numero} es {resultado}")
```

Antes de escribir código, pregúntate siempre:
- ¿Qué datos necesito como entrada?
- ¿Qué operación debo hacer?
- ¿Qué debo mostrar al final?

---

## 10. Buenas prácticas básicas

- **Nombres descriptivos**: `precio_total` es mucho mejor que `pt` o `x`.
- **Código limpio y legible**: deja espacios alrededor de los operadores (`x = 5`, no `x=5`).
- **No repitas código**: si algo se repite más de dos veces, probablemente necesita una función.
- **Comenta lo necesario**: explica el por qué, no el qué.
- **Sigue PEP8**: es la guía de estilo oficial de Python. VS Code puede avisarte de las infracciones automáticamente.

---

## [Ejercicios UT1](ejercicios_ut1.md)
