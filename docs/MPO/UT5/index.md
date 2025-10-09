# UT5: Manejo de Archivos y Errores

## Introducción

En esta unidad, aprenderemos a manejar archivos en Python, incluyendo la lectura y escritura de archivos, así como la gestión de errores mediante excepciones. Estos conceptos son fundamentales para desarrollar aplicaciones robustas y eficientes.

## Manejo de Archivos

En Python, podemos trabajar con archivos utilizando funciones integradas que nos permiten abrir, leer, escribir y cerrar archivos de manera sencilla.

### Abrir un archivo

Para abrir un archivo, utilizamos la función `open()`, que recibe dos argumentos: el nombre del archivo y el modo en que queremos abrirlo (lectura, escritura, etc.).

```python
archivo = open('mi_archivo.txt', 'r')  # 'r' para lectura
```

### Modos de apertura

Los modos de apertura más comunes son:

```python
archivo = open('mi_archivo.txt', 'r')  # 'r' para lectura
archivo = open('mi_archivo.txt', 'w')  # 'w' para escritura
archivo = open('mi_archivo.txt', 'a')  # 'a' para agregar contenido al final
archivo = open('mi_archivo.txt', 'r+') # 'r+' para lectura y escritura
```

### Leer un archivo

Para leer el contenido de un archivo, podemos usar métodos como `read()`, `readline()` o `readlines()`.

Las diferencias entre estos métodos son:

- `read()`: Lee todo el contenido del archivo de una sola vez y lo devuelve como una cadena.
- `readline()`: Lee una línea del archivo cada vez que se llama y devuelve esa línea como una cadena.
- `readlines()`: Lee todas las líneas del archivo y las devuelve como una lista de cadenas.

```python
contenido = archivo.read()  # Lee todo el contenido
linea = archivo.readline()  # Lee una línea
lineas = archivo.readlines() # Lee todas las líneas
```

Conocemos como cursor al indicador de posición en el archivo. Cada vez que leemos o escribimos, el cursor se mueve automáticamente. Por ejemplo, después de leer una línea con `readline()`, el cursor se mueve a la siguiente línea.

### Escribir en un archivo

Para escribir en un archivo, utilizamos el método `write()` o `writelines()`.

La diferencia entre estos métodos es:

- `write()`: Escribe una cadena en el archivo.
- `writelines()`: Escribe una lista de cadenas en el archivo.

```python
archivo = open('mi_archivo.txt', 'w')  # Abrir en modo escritura
archivo.write('Hola, mundo!\n')        # Escribir una línea
archivo.writelines(['Línea 1\n', 'Línea 2\n']) # Escribir varias líneas
```

Igual que al leer, el cursor se mueve automáticamente después de escribir.

??? warning "Importante"
    Al abrir un archivo en modo escritura (`'w'`), si el archivo ya existe, su contenido se borrará. Si queremos agregar contenido sin borrar lo existente, debemos usar el modo `'a'` (append).

### Cerrar un archivo

Es importante cerrar el archivo después de terminar de trabajar con él para liberar recursos. Utilizamos el método `close()`.

Este método no recibe argumentos y no devuelve ningún valor. Simplemente cierra el archivo que hemos abierto previamente.

```python
archivo.close()
```

### Uso de `with` para manejar archivos

Una forma recomendada de manejar archivos en Python es utilizando la declaración `with`. Esto asegura que el archivo se cierre automáticamente al finalizar el bloque de código, incluso si ocurre un error.

```python
with open('mi_archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
# El archivo se cierra automáticamente aquí
```

## Tratamiento de errores

El manejo de errores en Python se realiza mediante excepciones. Podemos capturar errores utilizando bloques `try` y `except`.

### Estructura básica de manejo de excepciones

```python
try:
    # Código que puede generar un error
    resultado = 10 / 0  # Esto generará un error de división por cero
except ZeroDivisionError:
    # Código que se ejecuta si ocurre un error específico
    print("Error: División por cero.")
except Exception as e:
    # Código que se ejecuta para cualquier otro error
    print(f"Error: {e}")
```

### Bloque `finally`

El bloque `finally` se ejecuta siempre, independientemente de si ocurrió un error o no. Es útil para realizar tareas de limpieza, como cerrar archivos.

```python
try:
    archivo = open('mi_archivo.txt', 'r')
    contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe.")
finally:
    archivo.close()  # Aseguramos que el archivo se cierre
```

### Cómo lanzar excepciones

Podemos lanzar nuestras propias excepciones utilizando la palabra clave `raise`.

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b
    
try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

Las excepciones pueden ser personalizadas creando nuevas clases que hereden de la clase `Exception`.

```python
class MiErrorPersonalizado(Exception):
    pass

def funcion_con_error():
    raise MiErrorPersonalizado("Este es un error personalizado.")
    
try:
    funcion_con_error()
except MiErrorPersonalizado as e:
    print(f"Error: {e}")
```

## Ejercicios de clase: [Manejo de Archivos y Errores](ejercicios_archivos_clase.md)