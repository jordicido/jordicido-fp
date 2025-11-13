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

## Rutas Absolutas y Relativas

En Linux, las rutas de archivos y directorios pueden ser absolutas o relativas. Una ruta absoluta comienza desde el directorio raíz (`/`) y especifica la ubicación completa del archivo o directorio. Por ejemplo:

```bash
# Ruta absoluta
/home/user/documentos/archivo.txt
```

Una ruta relativa, por otro lado, se especifica en relación con el directorio actual. Por ejemplo, si el directorio actual es `/home/user`, la ruta relativa al archivo `archivo.txt` en el subdirectorio `documentos` sería:

```bash
# Ruta relativa
documentos/archivo.txt
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

## Permisos y propiedades de archivos

En Linux, cada archivo y directorio tiene permisos y propiedades que determinan quién puede acceder y modificar esos archivos. Los permisos se dividen en tres categorías: propietario, grupo y otros. Cada categoría puede tener permisos de lectura (r), escritura (w) y ejecución (x).

Los permisos vienen indicados en una cadena de 10 caracteres al listar los archivos con el comando `ls -l`. El primer carácter indica el tipo de archivo (por ejemplo, `-` para archivos regulares y `d` para directorios), y los siguientes nueve caracteres representan los permisos para el propietario, grupo y otros, en ese orden.

Los permisos se pueden ver utilizando el comando `ls -l`, que muestra una lista detallada de archivos y sus permisos. Por ejemplo:

```bash
-rw-r--r-- 1 user group 1234 Jan 01 12:00 archivo.txt
``` 

En este ejemplo, el archivo `archivo.txt` tiene permisos de lectura y escritura para el propietario (user), permisos de lectura para el grupo (group) y permisos de lectura para otros usuarios.

## Cambiar los permisos de un archivo

Para cambiar los permisos de un archivo o directorio, se utiliza el comando `chmod` (change mode). Este comando permite modificar los permisos utilizando tanto notación simbólica como notación octal. Por ejemplo, para otorgar permisos de ejecución al propietario de un archivo, se puede utilizar el siguiente comando:

```bash
chmod u+x archivo.txt
```

Este comando añade el permiso de ejecución (`x`) al usuario propietario (`u`) del archivo `archivo.txt`.

También es posible utilizar notación octal para establecer los permisos. Por ejemplo, para establecer permisos de lectura, escritura y ejecución para el propietario, y solo lectura para el grupo y otros, se puede utilizar el siguiente comando:

```bash
chmod 755 archivo.txt
```

## Cambio de propietario y grupo

Para cambiar el propietario y el grupo de un archivo o directorio, se utilizan los comandos `chown` (change owner) y `chgrp` (change group). Por ejemplo, para cambiar el propietario de un archivo a un usuario llamado `nuevo_usuario`, se puede utilizar el siguiente comando:

```bash
sudo chown nuevo_usuario archivo.txt
```

Para cambiar el grupo de un archivo a un grupo llamado `nuevo_grupo`, se puede utilizar el siguiente comando:

```bash
sudo chgrp nuevo_grupo archivo.txt
```

## Pipes

En Linux, los pipes (`|`) permiten conectar la salida de un comando a la entrada de otro comando. Esto es útil para encadenar comandos y procesar datos de manera eficiente. Por ejemplo, para listar los archivos en un directorio y luego contar cuántos archivos hay, se puede utilizar el siguiente comando:

```bash
ls | wc -l
```

Este comando lista los archivos en el directorio actual y pasa esa lista al comando `wc -l`, que cuenta el número de líneas (es decir, el número de archivos).


## [Práctica en clase](practica_comandos.md)