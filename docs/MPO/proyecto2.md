# Proyecto 2: Gestor de Archivos en Consola

## Objetivo del proyecto

Desarrollar una aplicación de consola en Python que permita gestionar archivos y carpetas del sistema de forma sencilla.
El usuario podrá listar contenido, crear o eliminar carpetas y archivos, escribir dentro de ellos y visualizar información básica.

---

## Requisitos funcionales mínimos

Tu aplicación deberá permitir al usuario interactuar mediante un **menú principal** que se repita hasta que decida salir.

### MENÚ PRINCIPAL

1. Listar contenido del directorio actual
2. Crear un nuevo directorio
3. Crear un archivo de texto
4. Escribir texto en un archivo existente
5. Eliminar un archivo o directorio
6. Mostrar información del archivo
7. Salir

### Detalles de funcionamiento

* El programa debe **mostrar la ruta actual** en todo momento.
* Al listar el contenido, deberá indicar si cada elemento es **archivo o carpeta**.
* Al crear un archivo de texto, deberá permitir **introducir un nombre y escribir contenido inicial** (usando `open()` y `write()`).
* La opción de escribir texto deberá **abrir un archivo existente y añadir nuevo contenido** al final.
* Al mostrar información, deberá indicar **tamaño**, **fecha de modificación** y **tipo** (archivo o carpeta).
* El programa debe gestionar errores comunes, tales como:
* Intentar acceder o escribir en un archivo que no existe.

  * Intentar eliminar un archivo o carpeta inexistente.
  * Intentar crear un archivo o carpeta con un nombre ya existente.
  * Problemas de permisos o rutas incorrectas.
* En todos estos casos, el programa no debe cerrarse, sino mostrar un mensaje de error amigable para el usuario.

---

## Contenidos del módulo que se aplican

* Entrada/salida de datos por consola.
* Manejo de archivos de texto (`open()`, `read()`, `write()`, `append()`, `close()`).
* Uso del módulo `os` para manipular el sistema de archivos:

  * `os.listdir()`, `os.getcwd()`, `os.mkdir()`, `os.remove()`, `os.rmdir()`, `os.path`.
* Control de flujo (`if`, `elif`, `else`).
* Bucles (`while`, `for`).
* Funciones con parámetros y valores de retorno.

---

## Estructura sugerida del programa

```python
def mostrar_menu():
    # Muestra las opciones disponibles
    pass

def listar_contenido():
    # Lista archivos y carpetas del directorio actual
    pass

def crear_directorio():
    # Crea una nueva carpeta
    pass

def crear_archivo():
    # Crea un archivo de texto y permite escribir en él
    pass

def escribir_en_archivo():
    # Abre un archivo existente y añade texto al final
    pass

def eliminar_elemento():
    # Elimina un archivo o carpeta
    pass

def mostrar_informacion():
    # Muestra tamaño y fecha de modificación
    pass

def main():
    # Bucle principal del programa
    pass
```

---

## Extras (para subir nota o como ampliación)

* Permitir navegar hacia atrás (directorio padre).
* Colorear los nombres de archivos y carpetas (usando `colorama`).
* Permitir renombrar archivos o carpetas.
* Implementar un **historial de comandos** ejecutados en la sesión.
* Mostrar el tamaño total de los archivos dentro del directorio actual.

---

## Rúbrica de Evaluación (10 puntos)

| Criterio                                     | Descripción                                                                      | Puntuación Máxima | Nivel Avanzado (100%)                                                                      | Nivel Medio (75%)                                                           | Nivel Básico (50%)                                                                   |
| -------------------------------------------- | -------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Funcionalidad completa**                   | El programa cumple todos los requisitos funcionales mínimos del enunciado.       | 4                 | Todas las funciones operan correctamente y el menú es totalmente funcional.                | Faltan una o dos opciones menores del menú o alguna presenta fallos leves.  | Solo funcionan parcialmente las opciones principales (listar, crear o eliminar).     |
| **Uso del módulo `os` y manejo de archivos** | Utiliza correctamente las funciones de `os` y `open()`.                          | 2                 | Hace un uso correcto y variado del módulo `os` y gestiona archivos con control de errores. | Utiliza `os` pero con errores o redundancias; falta control de errores.     | Uso limitado o incorrecto de las funciones del módulo `os` y del manejo de archivos. |
| **Estructura del código y modularización**   | Organización del código en funciones y claridad general.                         | 2                 | Código bien modularizado, con funciones reutilizables y nombres descriptivos.              | Código parcialmente modular o con funciones demasiado largas.               | Código desordenado o sin funciones diferenciadas.                                    |
| **Legibilidad y buenas prácticas**           | Comentarios, sangrado, nombres de variables, claridad general.                   | 1                 | Código claro, bien documentado y legible.                                                  | Código entendible pero con escasos comentarios o nombres poco descriptivos. | Código confuso, con errores de estilo o mala indentación.                            |
| **Gestión de errores**                       | Tratamiento de situaciones no previstas (archivos inexistentes, permisos, etc.). | 1                 | Controla adecuadamente los errores más comunes y no se interrumpe la ejecución.            | Controla parcialmente los errores.                                          | El programa se interrumpe ante errores comunes.                                      |

**Total: 10 puntos**

