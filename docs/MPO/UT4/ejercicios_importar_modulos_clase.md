# Ejercicios de clase UT4: Importar módulos

## Contexto

Los módulos en Python son una herramienta muy importante y poderosa. Se debe explorar y probar diferentes módulos para sacar el mayor provecho de estos. En los siguientes ejercicios exploraremos los módulos más típicos.

## Ejercicio 1 - Gestor de Archivos con Python usando el módulo `os`

Desarrollar un programa en Python que permita gestionar archivos y directorios mediante un menú interactivo, utilizando las funciones principales del módulo `os`.  

El programa debe incluir las siguientes funcionalidades:  

1. **Menú principal** con las siguientes opciones:  

    - Listar archivos del directorio actual  
    - Verificar si un archivo existe  
    - Crear un nuevo archivo  
    - Crear un nuevo directorio  
    - Salir  

2. **Implementación de cada opción:**  

    - **Listar archivos:** Mostrar todos los archivos y carpetas en el directorio actual.  
    - **Verificar existencia:** Pedir al usuario un nombre de archivo y comprobar si existe.  
    - **Crear archivo:** Solicitar un nombre y generar un archivo vacío.  
    - **Crear directorio:** Pedir un nombre y crear una carpeta nueva.  

3. **Manejo de errores:**  

    - Evitar que el programa falle si el usuario ingresa datos incorrectos.  
    - Mostrar mensajes claros (ej: "❌ El archivo no existe", "✅ Operación exitosa").  

4. **Bucle infinito:**
  
    - El menú debe mostrarse continuamente hasta que el usuario elija "Salir".  

### Funciones del módulo `os` a utilizar

| **Función**          | **Descripción**                                      | **Ejemplo de uso**                     |  
|----------------------|----------------------------------------------------|----------------------------------------|  
| `os.listdir()`       | Lista archivos en un directorio                     | `os.listdir('.')`                      |  
| `os.path.exists()`   | Verifica si un archivo/directorio existe            | `os.path.exists("archivo.txt")`        |  
| `os.mkdir()`         | Crea un nuevo directorio                            | `os.mkdir("nueva_carpeta")`            |  
| `open()` (modo `'w'`)| Crea/sobrescribe un archivo (no es de `os`, pero útil) | `open("archivo.txt", "w").close()`     |  

## Ejercicio 2 - Coloreando la Terminal con `colorama`

Vamos a evolucionar el programa del ejercicio anterior para que los mensajes se muestren con colores utilizando el módulo `colorama`.

Concretamente vamos a modificar la opción de listar archivos.

En vez de imprimir los nombres de los archivos directamente, vamos a colorearlos según su tipo:
- Archivos de texto (`.txt`) en **verde**.
- Archivos de imagen (`.jpg`, `.png`) en **azul**.
- Archivos de audio (`.mp3`, `.wav`) en **amarillo**.
- Otros archivos en **blanco**.

### Funciones del módulo `colorama` a utilizar
| **Función**          | **Descripción**                                      | **Ejemplo de uso**                     |
|----------------------|----------------------------------------------------|----------------------------------------|
| `Fore`                | Colores del texto                                   | `Fore.GREEN`, `Fore.BLUE`, etc.        |
| `Style`               | Estilos del texto                                   | `Style.RESET_ALL`                      |

### Ejemplo de implementación

```python
import os
from colorama import Fore, Style
def pintar_terminal():
    print("Ejemplo de uso de colorama")
    print(Fore.GREEN + "Este texto es verde" + Style.RESET_ALL)
    print(Fore.BLUE + "Este texto es azul" + Style.RESET_ALL)
    print(Fore.YELLOW + "Este texto es amarillo" + Style.RESET_ALL)
    print(Fore.WHITE + "Este texto es blanco" + Style.RESET_ALL)
    print("Fin del ejemplo")
```

Una vez implementado, el programa debería mostrar los archivos del directorio actual con los colores correspondientes según su tipo. Asegúrate de que el usuario pueda ver claramente los nombres de los archivos coloreados. A continuación imprime detalles de cada archivo, como su tamaño y fecha de modificación usando la función `os.stat()`.

Con estas modificaciones vamos a tener una suerte de comando `ls`(o `dir` en Windows) mejorado, que no solo lista los archivos, sino que también los colorea según su tipo y muestra información adicional.