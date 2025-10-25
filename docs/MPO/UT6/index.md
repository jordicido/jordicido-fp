# UT6: Automatización de Tareas del Sistema

## Introducción

En esta unidad, aprenderemos a automatizar tareas del sistema utilizando Python. La automatización puede ayudarnos a ahorrar tiempo y reducir errores en tareas repetitivas. Veremos cómo interactuar con el sistema operativo, manejar procesos y programar tareas automáticas. 

## Interacción con el Sistema Operativo

Python proporciona el módulo `os` que nos permite interactuar con el sistema operativo de manera sencilla. Podemos realizar operaciones como crear, eliminar y renombrar archivos y directorios, así como obtener información del sistema.

### Importar el módulo os

Para utilizar el módulo `os`, primero debemos importarlo en nuestro script de Python:

```python
import os
```

### Funciones comunes del módulo os

Algunas funciones comunes del módulo `os` incluyen:

- `os.getcwd()`: Obtiene el directorio de trabajo actual.
- `os.listdir(path)`: Lista los archivos y directorios en el directorio especificado.
- `os.mkdir(path)`: Crea un nuevo directorio.
- `os.remove(path)`: Elimina un archivo.
- `os.rmdir(path)`: Elimina un directorio vacío.
- `os.rename(src, dst)`: Renombra un archivo o directorio.  

```python
# Ejemplo de uso del módulo os
import os

# Obtener el directorio de trabajo actual
directorio_actual = os.getcwd()
print(f'Directorio actual: {directorio_actual}')

# Listar archivos y directorios en el directorio actual
contenido = os.listdir(directorio_actual)
print('Contenido del directorio:')
for item in contenido:
    print(item)
```

## Argumentos y Parámetros de Línea de Comandos

Python permite manejar argumentos y parámetros pasados desde la línea de comandos utilizando el módulo `sys`. Esto es útil para crear scripts que puedan recibir entradas dinámicas al ejecutarse.

### Importar el módulo sys

Para utilizar el módulo `sys`, primero debemos importarlo en nuestro script de Python:

```python
import sys
```

### Acceder a los argumentos de línea de comandos

Los argumentos de línea de comandos se almacenan en la lista `sys.argv`, donde el primer elemento es el nombre del script y los elementos siguientes son los argumentos pasados.

```python
# Ejemplo de uso del módulo sys
import sys
# Imprimir los argumentos de línea de comandos
print('Argumentos de línea de comandos:')
for arg in sys.argv:
    print(arg)
```

### Ejemplo práctico

A continuación, un ejemplo de un script que recibe un nombre de archivo como argumento y muestra su contenido:

```python
import sys
import os

if len(sys.argv) != 2:
    print('Uso: python script.py <nombre_del_archivo>')
    sys.exit(1)

nombre_archivo = sys.argv[1]

if not os.path.isfile(nombre_archivo):
    print(f'El archivo {nombre_archivo} no existe.')
    sys.exit(1)

with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print('Contenido del archivo:')
    print(contenido)  
```

Otros ejemplos combinando `os` y `sys` pueden incluir scripts para automatizar copias de seguridad, limpieza de archivos temporales, o cualquier otra tarea repetitiva que involucre el sistema de archivos. Por ejemplo, un script que elimine archivos antiguos en un directorio específico.

```python
import os
import sys

if len(sys.argv) != 3:
    print('Uso: python limpiar.py <directorio> <días>')
    sys.exit(1)

directorio = sys.argv[1]
dias = int(sys.argv[2])

# Obtener la fecha límite
fecha_limite = time.time() - (dias * 86400)

# Eliminar archivos antiguos
for root, dirs, files in os.walk(directorio):
    for nombre_archivo in files:
        ruta_archivo = os.path.join(root, nombre_archivo)
        if os.path.getmtime(ruta_archivo) < fecha_limite:
            os.remove(ruta_archivo)
            print(f'Archivo eliminado: {ruta_archivo}')
```

## Ejercicios de clase: [Scripts de Automatización](ejercicios_scripts_clase.md)