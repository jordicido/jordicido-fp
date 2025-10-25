# UT 4: Gestión de la información en sistemas operativos Libres: Linux

## Introducción

En esta unidad, aprenderemos a gestionar la información en sistemas operativos libres, centrándonos en Linux. Veremos cómo funcionan los sistemas de archivos en Linux, los comandos básicos para la gestión de archivos y directorios, el usuario root y sudo, los permisos y propiedades de archivos, y la estructura del sistema operativo Linux.

## Sistemas de archivos en Linux

Linux utiliza un sistema de archivos jerárquico, donde todo se organiza en forma de árbol. El directorio raíz se representa con una barra diagonal (`/`), y todos los demás archivos y directorios se encuentran debajo de este. Algunos de los sistemas de archivos más comunes en Linux son ext4, XFS y Btrfs. El más utilizado es ext4, que ofrece un buen equilibrio entre rendimiento y fiabilidad. 

Alguna vez, os pasará que al montar un dispositivo de almacenamiento externo (como un pendrive o un disco duro) en Linux, el sistema de archivos utilizado en ese dispositivo no sea compatible con Linux. En estos casos, es posible que necesitéis instalar soporte adicional para ese sistema de archivos específico o utilizar herramientas de terceros para acceder a los datos.

## Comandos básicos para la gestión de archivos y directorios

Todos los sistemas operativos Linux actuales cuentan con una interfaz gráfica de usuario (GUI) que facilita la gestión de archivos y directorios. Sin embargo, es fundamental conocer los comandos básicos de la línea de comandos (CLI) para gestionar archivos y directorios de manera eficiente. Algunos de los comandos más comunes son:

- `ls`: Lista los archivos y directorios en el directorio actual.
- `cd`: Cambia el directorio actual.
- `pwd`: Muestra la ruta del directorio actual.
- `mkdir`: Crea un nuevo directorio.
- `rm`: Elimina archivos o directorios.
- `cp`: Copia archivos o directorios.
- `mv`: Mueve o renombra archivos o directorios.

## Argumentos y Parámetros de Línea de Comandos

Los comandos de la línea de comandos en Linux pueden aceptar argumentos y parámetros para modificar su comportamiento. Los argumentos son valores que se pasan al comando, mientras que los parámetros son opciones que alteran la forma en que se ejecuta el comando. Por ejemplo:

```bash
ls -l /home/user
```

En este caso, `-l` es un parámetro que indica que se debe mostrar la lista de archivos en formato largo, y `/home/user` es un argumento que especifica el directorio a listar.

Es importante consultar la documentación de cada comando para entender qué argumentos y parámetros acepta. Esto se puede hacer utilizando el comando `man`, que muestra el manual del comando:

```bash
man ls
```

## Redirecciones de Entrada y Salida

En Linux, es posible redirigir la entrada y salida de los comandos utilizando operadores especiales. Algunos de los operadores más comunes son:
- `>`: Redirige la salida estándar a un archivo, sobrescribiendo su contenido.
- `>>`: Redirige la salida estándar a un archivo, agregando al final del archivo.
- `<`: Redirige la entrada estándar desde un archivo.

Por ejemplo, para guardar la salida del comando `ls` en un archivo llamado `lista.txt`, se puede utilizar el siguiente comando:

```bash
ls > lista.txt
```

Este comando crea (o sobrescribe) el archivo `lista.txt` con la lista de archivos y directorios del directorio actual.

También es posible usar redirecciones de errores utilizando `2>` para redirigir la salida de error a un archivo. Por ejemplo:

```bash
ls /directorio_inexistente 2> errores.txt
```

Este comando intenta listar un directorio que no existe y redirige el mensaje de error al archivo `errores.txt`.

## Manuales y documentación

Linux cuenta con una amplia documentación y manuales para ayudar a los usuarios a comprender y utilizar el sistema operativo de manera efectiva. Podéis consultar los manuales de los comandos utilizando el comando `man`, que muestra la documentación detallada de cada comando. Además, existen numerosos recursos en línea, foros y comunidades donde podéis encontrar ayuda y compartir conocimientos sobre Linux.

Dentro de la documentación, es común encontrar secciones como:

- **NAME**: Nombre del comando y una breve descripción.
- **SYNOPSIS**: Sintaxis del comando, incluyendo los argumentos y parámetros que acepta
- **DESCRIPTION**: Descripción detallada del comando y su funcionamiento.
- **OPTIONS**: Lista de opciones y parámetros disponibles para el comando.
- **EXAMPLES**: Ejemplos de uso del comando.

## El usuario root y sudo

En Linux, el usuario root es el superusuario del sistema, con privilegios completos para realizar cualquier operación. Sin embargo, por razones de seguridad, no se recomienda utilizar la cuenta root directamente para tareas diarias. En su lugar, se utiliza el comando `sudo` (superuser do) para ejecutar comandos con privilegios elevados de manera temporal. Por ejemplo, para instalar un paquete utilizando el gestor de paquetes `apt`, se puede utilizar el siguiente comando:

```bash
sudo apt install nombre_del_paquete
```

## [Práctica en clase](practica_comandos.md)