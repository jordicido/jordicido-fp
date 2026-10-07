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

```python hl_lines="2 3 4"
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

```python hl_lines="1"
with open('mi_archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
# El archivo se cierra automáticamente aquí
```

## Tratamiento de errores

Cuando ejecutamos un programa pueden aparecer situaciones que impidan que continúe funcionando con normalidad. Por ejemplo, el usuario puede introducir texto cuando esperábamos un número, podemos intentar abrir un archivo que no existe o dividir un número entre cero.

Python permite gestionar este tipo de situaciones mediante **excepciones**.

Una excepción es un error que se produce durante la ejecución de un programa. Si no la gestionamos, Python detiene el programa y muestra un mensaje indicando qué ha ocurrido.

Por ejemplo:

```python
numero = int(input("Introduce un número: "))
print(numero)
```

Si el usuario introduce `hola`, Python no puede convertir ese texto a un número entero y genera una excepción:

```text
ValueError: invalid literal for int() with base 10: 'hola'
```

El programa termina en ese momento. La gestión de excepciones nos permite detectar estos errores y decidir qué debe hacer el programa en lugar de cerrarse inesperadamente.

!!! info "Idea principal"
    Las excepciones no sirven para evitar que ocurran errores, sino para **controlar qué hace nuestro programa cuando ocurre un error que podemos prever**.

### Excepciones habituales

Python dispone de diferentes tipos de excepciones. Cada una representa una situación concreta.

| Excepción | Cuándo puede producirse |
|-----------|-------------------------|
| `ValueError` | Cuando un valor tiene un formato incorrecto. |
| `TypeError` | Cuando realizamos una operación con un tipo de dato no adecuado. |
| `ZeroDivisionError` | Cuando intentamos dividir entre cero. |
| `FileNotFoundError` | Cuando intentamos abrir un archivo que no existe. |
| `PermissionError` | Cuando no tenemos permisos para acceder a un archivo o recurso. |
| `IndexError` | Cuando intentamos acceder a una posición inexistente de una lista. |
| `KeyError` | Cuando intentamos acceder a una clave inexistente de un diccionario. |

Por ejemplo:

```python
# ValueError
numero = int("hola")
```

```python
# ZeroDivisionError
resultado = 10 / 0
```

```python
# IndexError
numeros = [10, 20, 30]
print(numeros[5])
```

```python
# KeyError
usuario = {
    "nombre": "Ana",
    "edad": 25
}

print(usuario["email"])
```

No necesitamos memorizar todas las excepciones existentes. Lo importante es reconocer las que aparecen con más frecuencia y entender qué situación las ha provocado.

### Estructura básica: `try` y `except`

Para gestionar una excepción utilizamos los bloques `try` y `except`:

```python
try:
    # Código que puede producir una excepción
except TipoDeExcepcion:
    # Código que se ejecuta si ocurre esa excepción
```

Por ejemplo:

```python
try:
    edad = int(input("Introduce tu edad: "))
except ValueError:
    print("Debes introducir un número entero.")
```

El funcionamiento es el siguiente:

1. Python comienza ejecutando el código del bloque `try`.
2. Si todo funciona correctamente, el bloque `except` no se ejecuta.
3. Si se produce una excepción del tipo indicado, Python deja de ejecutar el bloque `try`.
4. A continuación ejecuta el bloque `except`.
5. Después, el programa puede continuar normalmente.

```python
try:
    edad = int(input("Introduce tu edad: "))
    print(f"Tienes {edad} años.")
except ValueError:
    print("La edad introducida no es válida.")

print("Fin del programa.")
```

Si el usuario introduce `25`, se muestra la edad y el programa continúa. Si introduce `hola`, se muestra el mensaje de error y también se alcanza `Fin del programa.`

!!! warning "Importante"
    Dentro del bloque `try` debemos colocar únicamente el código que realmente puede producir la excepción que queremos controlar.

### Capturar diferentes tipos de excepciones

Un mismo fragmento de código puede producir diferentes errores:

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No es posible dividir entre cero.")
```

Cada bloque `except` se encarga de un tipo concreto de error. Esto permite mostrar mensajes más claros y responder de forma diferente según el problema ocurrido.

Si queremos realizar la misma acción para varios tipos de excepciones, podemos agruparlas utilizando una tupla:

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
    print(resultado)
except (ValueError, ZeroDivisionError):
    print("No se ha podido realizar la operación.")
```

Cuando sea útil para el usuario saber qué ha ocurrido exactamente, suele ser mejor utilizar bloques `except` separados.

### Obtener información sobre una excepción con `as`

Podemos guardar el objeto de la excepción en una variable utilizando `as`:

```python
try:
    numero = int("hola")
except ValueError as error:
    print("Se ha producido un error:")
    print(error)
```

El nombre de la variable puede ser cualquiera, aunque es habitual utilizar nombres como `error` o `e`.

```python
except ValueError as e:
    print(e)
```

Esto puede ser útil para obtener información adicional durante el desarrollo de un programa.

### Evitar capturas demasiado generales

También es posible capturar excepciones de forma muy general:

```python
try:
    numero = int(input("Introduce un número: "))
except Exception:
    print("Ha ocurrido un error.")
```

Esto funciona, pero normalmente no es la mejor opción. Si capturamos cualquier excepción, podemos estar ocultando errores que no habíamos previsto:

```python
try:
    numero = int(input("Introduce un número: "))
    print(variable_que_no_existe)
except Exception:
    print("Ha ocurrido un error.")
```

El problema real no tiene relación con el número introducido, pero el programa muestra simplemente un mensaje genérico. Por eso es preferible capturar excepciones concretas:

```python
try:
    numero = int(input("Introduce un número: "))
except ValueError:
    print("Debes introducir un número válido.")
```

!!! tip "Buena práctica"
    Captura únicamente las excepciones que sabes cómo gestionar. Cuanto más específico sea el `except`, más fácil será detectar y corregir problemas.

### El bloque `else`

Podemos añadir un bloque `else` después de los bloques `except`. El código situado dentro de `else` solamente se ejecuta cuando **no se ha producido ninguna excepción**.

```python
try:
    edad = int(input("Introduce tu edad: "))
except ValueError:
    print("La edad introducida no es válida.")
else:
    print(f"Tienes {edad} años.")
```

Podemos pensar en los bloques de esta forma:

```text
try     → intenta realizar la operación
except  → qué hacer si ocurre un error
else    → qué hacer si todo ha funcionado correctamente
```

El uso de `else` ayuda a mantener dentro del `try` únicamente las instrucciones que pueden provocar la excepción que queremos controlar.

```python
try:
    numero = int(input("Introduce un número: "))
except ValueError:
    print("El valor no es válido.")
else:
    resultado = numero * 2
    print(f"El doble es {resultado}.")
```

### El bloque `finally`

El bloque `finally` contiene código que se ejecuta **siempre**, independientemente de que se haya producido una excepción o no.

```python
try:
    numero = int(input("Introduce un número: "))
except ValueError:
    print("Valor incorrecto.")
finally:
    print("La operación ha finalizado.")
```

La estructura completa es:

```python
try:
    # Código que puede producir una excepción
except TipoDeExcepcion:
    # Se ejecuta si ocurre esa excepción
else:
    # Se ejecuta si no ocurre ninguna excepción
finally:
    # Se ejecuta siempre
```

No es obligatorio utilizar todos los bloques. Dependiendo del problema podemos utilizar únicamente `try` y `except`, o añadir `else` y `finally` cuando sean necesarios.

### Excepciones y archivos

Las excepciones son especialmente útiles cuando trabajamos con archivos:

```python
try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("No se ha encontrado el archivo datos.txt.")
```

Podemos controlar también otros posibles problemas:

```python
try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
except PermissionError:
    print("No tienes permisos para leer el archivo.")
else:
    print(contenido)
```

Al utilizar `with`, el archivo se cerrará automáticamente cuando terminemos de trabajar con él.

!!! tip "Archivos y `with`"
    Cuando trabajemos con archivos, utilizaremos normalmente `with` en lugar de abrir y cerrar el archivo manualmente. Esto simplifica el código y garantiza que el archivo se cierre correctamente incluso si aparece una excepción.

### ¿Dónde debemos capturar una excepción?

Una excepción no tiene que gestionarse necesariamente en la misma función donde se produce:

```python
def leer_edad():
    edad = int(input("Introduce tu edad: "))
    return edad


try:
    edad = leer_edad()
    print(f"Tienes {edad} años.")
except ValueError:
    print("Debes introducir una edad válida.")
```

La excepción puede producirse dentro de `leer_edad()` cuando se ejecuta `int()`. Sin embargo, la función no contiene ningún `try`: la excepción se transmite a la parte del programa que ha llamado a la función y allí puede ser capturada. Este comportamiento se conoce como **propagación de excepciones**.

!!! info "Capturar o propagar"
    No todas las funciones tienen que capturar todas las excepciones. En muchas ocasiones es mejor dejar que el error se propague y gestionarlo en una parte del programa donde podamos decidir correctamente qué hacer.

### Lanzar excepciones con `raise`

También podemos provocar una excepción nosotros mismos utilizando la instrucción `raise`. Esto resulta útil cuando queremos indicar que se ha incumplido alguna regla de nuestro programa.

```python
def registrar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")

    print(f"Edad registrada: {edad}")
```

Podemos capturar esa excepción:

```python
try:
    edad = int(input("Introduce tu edad: "))
    registrar_edad(edad)
except ValueError as error:
    print(f"Error: {error}")
```

`raise ValueError("La edad no puede ser negativa.")` significa que, en esa situación, el programa no puede continuar con normalidad y genera una excepción de tipo `ValueError`.

Otro ejemplo de validación mediante `raise`:

```python
def calcular_descuento(precio, porcentaje):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100.")

    descuento = precio * porcentaje / 100
    return precio - descuento
```

### Validar datos con excepciones

Podemos repetir una operación hasta que el usuario introduzca un dato válido:

```python
while True:
    try:
        edad = int(input("Introduce tu edad: "))

        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")

        break

    except ValueError as error:
        print(f"Error: {error}")

print(f"Edad registrada: {edad}")
```

En este ejemplo podemos recibir un `ValueError` porque el usuario introduce algo que no puede convertirse a entero o porque generamos manualmente el error al introducir una edad negativa.

### Excepciones personalizadas

También podemos crear nuestros propios tipos de excepción mediante una clase que herede de `Exception`:

```python
class EdadNoValidaError(Exception):
    pass
```

Después podemos lanzarla y capturarla como cualquier otra excepción:

```python
def registrar_edad(edad):
    if edad < 0:
        raise EdadNoValidaError("La edad no puede ser negativa.")

    print(f"Edad registrada: {edad}")


try:
    registrar_edad(-5)
except EdadNoValidaError as error:
    print(f"Error: {error}")
```

!!! note "Ampliación"
    En programas sencillos normalmente utilizaremos excepciones incorporadas en Python como `ValueError`, `FileNotFoundError` o `ZeroDivisionError`. Las excepciones personalizadas resultan más útiles cuando nuestras aplicaciones crecen y necesitamos representar errores específicos.

### Buenas prácticas al trabajar con excepciones

Al utilizar excepciones debemos seguir algunas recomendaciones:

1. **Capturar excepciones concretas.** Es preferible `except ValueError:` que utilizar un `except:` genérico.
2. **No utilizar excepciones para ocultar errores.** Debemos evitar `except Exception: pass`, porque ignora completamente el error.
3. **Mostrar mensajes útiles.** Es mejor indicar qué debe corregir el usuario, por ejemplo: `Debes introducir un número entero.`
4. **Mantener el bloque `try` lo más pequeño posible.** Así queda claro qué instrucción puede producir la excepción.
5. **Utilizar `with` al trabajar con archivos.** Esto garantiza que el archivo se cierre correctamente siempre que sea posible.

### Ejemplo completo

El siguiente programa combina archivos, funciones y excepciones para guardar nombres en un archivo:

```python
def guardar_nombre(nombre):
    if nombre == "":
        raise ValueError("El nombre no puede estar vacío.")

    with open("nombres.txt", "a") as archivo:
        archivo.write(nombre + "\n")


try:
    nombre = input("Introduce un nombre: ")
    guardar_nombre(nombre)
except ValueError as error:
    print(f"Error: {error}")
except PermissionError:
    print("No tienes permisos para escribir en el archivo.")
else:
    print("Nombre guardado correctamente.")
finally:
    print("Fin del programa.")
```

En este ejemplo:

- La función recibe un nombre.
- Si está vacío, genera un `ValueError`.
- El archivo se abre utilizando `with`.
- El programa controla posibles errores.
- `else` se ejecuta únicamente si todo ha funcionado correctamente.
- `finally` se ejecuta siempre.

### Resumen

Las excepciones permiten crear programas más robustos y controlar errores que pueden aparecer durante la ejecución.

```python
try:
    # Intentamos ejecutar una operación

except TipoDeExcepcion:
    # Gestionamos un error concreto

else:
    # Se ejecuta si no ocurre ningún error

finally:
    # Se ejecuta siempre
```

También podemos generar nuestras propias excepciones utilizando:

```python
raise ValueError("Mensaje del error")
```

Las ideas más importantes que debemos recordar son:

- Una excepción es un error producido durante la ejecución.
- `try` contiene el código que puede producir una excepción.
- `except` permite gestionar errores concretos.
- Podemos utilizar varios bloques `except`.
- `else` se ejecuta cuando no ha ocurrido ninguna excepción.
- `finally` se ejecuta siempre.
- Las excepciones pueden propagarse entre funciones.
- `raise` permite generar una excepción de forma intencionada.
- Es preferible capturar excepciones específicas en lugar de ocultar cualquier error.
- Al trabajar con archivos, `with` facilita una gestión segura de los recursos.

## Ejercicios de clase: [Manejo de Archivos y Errores](ejercicios_archivos_clase.md)
