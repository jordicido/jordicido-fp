# Ejercicios de clase UT5: Configuración de la información en sistemas operativos Libres: Linux

## Contexto

En esta unidad, hemos aprendido a gestionar usuarios y grupos en sistemas operativos libres como Linux. Ahora, pondremos en práctica estos conceptos a través de una serie de ejercicios enfocados en la creación, modificación y eliminación de usuarios y grupos utilizando la terminal de Linux. Asegúrate de entender cada problema y de implementar una solución adecuada utilizando los comandos aprendidos.

Intenta realizar estos ejercicios en un entorno Linux real o en una máquina virtual para familiarizarte con la gestión de usuarios y grupos. Además, intenta utilizar solo la terminal para completar los ejercicios, evitando el uso de interfaces gráficas. Si tienes dudas sobre algún comando, recuerda que puedes consultar su manual utilizando el comando `man` seguido del nombre del comando (por ejemplo, `man useradd`).

## Ejercicio 1 - Crear un usuario

1. Crea un nuevo usuario llamado `maria`.
2. Establece una contraseña para el usuario `maria`.
3. Verifica la creación del usuario utilizando el comando `id maria`.

## Ejercicio 2 - Crear un grupo

1. Crea un nuevo grupo llamado `administradores`.
2. Añade el usuario `maria` al grupo `administradores`.
3. Verifica que `maria` pertenece al grupo `administradores` utilizando el comando `id maria`.

## Ejercicio 3 - Modificar un usuario

1. Crea un nuevo usuario llamado `carlos`.
2. Cambia el nombre del usuario `carlos` a `carlitos`.
3. Verifica el cambio de nombre utilizando el comando `id carlitos`.

## Ejercicio 4 - Eliminar un usuario

1. Crea un nuevo usuario llamado `pedro`.
2. Elimina el usuario `pedro` del sistema.
3. Verifica que el usuario `pedro` ha sido eliminado intentando obtener su información con el comando `id pedro`.

## Ejercicio 5 - Eliminar un grupo

1. Crea un nuevo grupo llamado `temporal`.
2. Elimina el grupo `temporal` del sistema.
3. Verifica que el grupo `temporal` ha sido eliminado intentando obtener su información con el comando `getent group temporal`.

## Ejercicio 6 - Listar usuarios y grupos

1. Muestra la lista completa de usuarios en el sistema utilizando el archivo `/etc/passwd`.
2. Muestra la lista completa de grupos en el sistema utilizando el archivo `/etc/group`.

## Ejercicio 7 - Script Hola, Mundo personalizado

1. Crea un script en bash llamado `hola_mundo.sh` que imprima "Hola, Mundo desde [tu_nombre]!" en la terminal, donde `[tu_nombre]` es tu nombre real.
2. Asigna permisos de ejecución al script.
3. Ejecuta el script y verifica que la salida sea correcta.

## Ejercicio 8 - Calculadora básica en bash

1. Crea un script en bash llamado `calculadora.sh` que solicite al usuario dos números y sume esos números.
2. Asigna permisos de ejecución al script.
3. Ejecuta el script y verifica que la suma sea correcta.

## Ejercicio 9 - Comprobador de edad

1. Crea un script en bash llamado `comprobador_edad.sh` que solicite al usuario su edad y determine si es mayor o menor de edad (18 años).
2. Asigna permisos de ejecución al script.
3. Ejecuta el script y verifica que la salida sea correcta según la edad ingresada.

## Ejercicio 10 - Creador de usuarios simple

1. Crea un script en bash llamado `creador_usuarios.sh` que solicite al usuario el nombre de un nuevo usuario y lo cree en el sistema.
2. Debe solicitar también una contraseña para el nuevo usuario.
3. Asigna permisos de ejecución al script.
4. Ejecuta el script y verifica que el usuario se haya creado correctamente.