# Ejercicios de clase UT4: Gestión de la información en sistemas operativos Libres: Linux

## Contexto

En esta unidad, hemos aprendido a utilizar los comandos básicos de la línea de comandos en Linux para gestionar archivos y directorios. Ahora, pondremos en práctica estos conceptos a través de una serie de ejercicios enfocados en la gestión de archivos y directorios utilizando la terminal de Linux. Asegúrate de entender cada problema y de implementar una solución adecuada utilizando los comandos aprendidos.

Intenta realizar estos ejercicios en un entorno Linux real o en una máquina virtual para familiarizarte con la línea de comandos y la gestión de archivos en sistemas operativos libres. Además, intenta utilizar solo la terminal para completar los ejercicios, evitando el uso de interfaces gráficas. Si tienes dudas sobre algún comando, recuerda que puedes consultar su manual utilizando el comando `man` seguido del nombre del comando (por ejemplo, `man ls`).

## Ejercicio 1 - Listar archivos en un directorio

1. Ve a la carpeta de tu usuario y lista todos los archivos y subdirectorios que contiene.
2. A continuación, lista los archivos en formato largo, mostrando detalles como permisos, propietario, tamaño y fecha de modificación.
3. Finalmente, lista todos los archivos, incluidos los ocultos.

## Ejercicio 2 - Crear y eliminar directorios

1. Crea un nuevo directorio llamado `prueba_directorio` en tu carpeta de usuario.
2. Dentro de `prueba_directorio`, crea dos subdirectorios llamados `subdir1` y `subdir2`.
3. Elimina el directorio `subdir2`. 
4. Finalmente, elimina el directorio `prueba_directorio` junto con su contenido.

## Ejercicio 3 - Copiar y mover archivos

1. Crea un archivo de texto llamado `archivo_origen.txt` en tu carpeta de usuario y escribe algo de texto en él (pudes usar el comando `echo` para esto).
2. Copia `archivo_origen.txt` a un nuevo archivo llamado `archivo_copia.txt`.
3. Vuelve a crear el directorio `prueba_directorio` y mueve `archivo_copia.txt` a este directorio.
4. Finalmente, renombra `archivo_origen.txt` a `archivo_renombrado.txt`.

## Ejercicio 4 - Eliminar archivos

1. Crea un archivo de texto llamado `archivo_a_eliminar.txt` en tu carpeta de usuario.
2. Verifica que el archivo existe listando los archivos en tu carpeta de usuario.
3. Elimina `archivo_a_eliminar.txt`.
4. Verifica que el archivo ha sido eliminado listando nuevamente los archivos en tu carpeta de usuario.

## Ejercicio 5 - Mostrar la ruta del directorio actual

1. Abre la terminal y asegúrate de estar en tu carpeta de usuario.
2. Utiliza el comando adecuado para mostrar la ruta completa del directorio actual.
3. Cambia a otro directorio (por ejemplo, `/tmp`) y vuelve a mostrar la ruta del directorio actual.

## Ejercicio 6 - Uso de argumentos y parámetros

Busca en el manual del comando `wc` (word count) y realiza lo siguiente:
1. Crea un archivo de texto llamado `texto_ejemplo.txt` con varias líneas de texto.
2. Utiliza el comando `wc` para contar el número de líneas, palabras y caracteres en `texto_ejemplo.txt`.
3. Luego utiliza el comando `wc` con el parámetro adecuado para mostrar solo el número de líneas en el archivo.
4. Ahora, utiliza el comando `wc` con el parámetro adecuado para contar los caracteres en el archivo.
5. Finalmente, utiliza el comando `wc` con el parámetro adecuado para contar la frase más larga en el archivo.

## Ejercicio 7 - Redirección de salida

1. Crea un archivo de texto llamado `salida_ejemplo.txt`.
2. Utiliza un comando que genere salida (por ejemplo, `ls -l`) y redirige esa salida al archivo `salida_ejemplo.txt`.
3. Verifica el contenido de `salida_ejemplo.txt` utilizando el comando `cat`.
4. Ahora, utiliza la redirección para agregar más información al archivo (por ejemplo, añade la frase `Fin del informe`).
5. Vuelve a verificar el contenido del archivo para asegurarte de que la nueva información se ha añadido correctamente.

## Ejercicio 8 - Buscando coincidencias con grep

1. Analiza con el manual del comando `grep` cómo funciona.
2. Crea un archivo de texto llamado `log_ejemplo.txt` con varias líneas de texto, algunas de las cuales contienen la palabra "error".
3. Utiliza el comando `grep` para buscar todas las líneas que contienen la palabra "error" en `log_ejemplo.txt`.
4. Ahora, utiliza `grep` con el parámetro adecuado para buscar la palabra "error" sin importar si está en mayúsculas o minúsculas.
5. Finalmente, utiliza `grep` con el parámetro adecuado para mostrar las líneas que no contienen la palabra "error".


## Ejercicio 9 - Permisos de archivos

1. Crea un archivo de texto llamado `permisos_ejemplo.txt` en tu carpeta de usuario.
2. Utiliza el comando `ls -l` para ver los permisos actuales del archivo.
3. Cambia los permisos del archivo para que solo el propietario tenga permisos de lectura y escritura.
4. Verifica los cambios en los permisos utilizando nuevamente `ls -l`.
5. Intenta abrir el archivo con otro usuario (si es posible) para verificar que no tiene acceso.

## Ejercicio 10 - Uso de rutas absolutas y relativas

1. Crea un directorio llamado `ruta_ejemplo` en tu carpeta de usuario.
2. Dentro de `ruta_ejemplo`, crea un archivo llamado `archivo_ruta.txt`.
3. Desde tu carpeta de usuario, utiliza una ruta relativa para acceder a `archivo_ruta.txt` y muestra su contenido.
4. Ahora, utiliza una ruta absoluta para acceder al mismo archivo y muestra su contenido.
5. Finalmente, elimina el directorio `ruta_ejemplo` junto con su contenido.