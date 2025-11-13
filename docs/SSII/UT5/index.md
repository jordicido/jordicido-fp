# UT 5. Configuración de la información en sistemas operativos Libres: Linux

## Introducción

En esta unidad, aprenderemos a configurar la información en sistemas operativos libres, centrándonos en Linux. Veremos cómo configurar la red, gestionar servicios y procesos, y utilizar herramientas de configuración del sistema.

## Configuración de usuarios y grupos

En Linux, la gestión de usuarios y grupos es fundamental para la seguridad y organización del sistema. Utilizaremos comandos como `useradd`, `usermod`, `groupadd` y `passwd` para crear y gestionar usuarios y grupos.

Los usuarios en Linux tienen un identificador único (UID) y pertenecen a uno o más grupos, que también tienen un identificador único (GID). Los grupos permiten gestionar permisos de acceso a archivos y recursos del sistema de manera colectiva.

La información sobre usuarios y grupos se almacena en archivos del sistema, como `/etc/passwd` para usuarios y `/etc/group` para grupos. Podemos ver el contenido de estos archivos utilizando comandos como `cat`, `less` o `more`.

```bash
cat /etc/passwd
cat /etc/group
```

Si os fijais, cada línea en estos archivos representa un usuario o grupo, con campos separados por dos puntos (`:`). Sin embargo, la información de las contraseñas no se almacena directamente en `/etc/passwd` por razones de seguridad; en su lugar, se utiliza el archivo `/etc/shadow`, que es accesible solo por el usuario root.

¿Qué información contiene cada uno de estos archivos? Puedes investigar y describir brevemente la función de cada campo en estos archivos.

### Crear un usuario

Para crear un nuevo usuario en Linux, utilizamos el comando `useradd` seguido del nombre del usuario. Por ejemplo:

```bash
sudo useradd juan
```

Con este comando, hemos creado un usuario llamado "juan". Para establecer una contraseña para este usuario, utilizamos el comando `passwd`:

```bash
sudo passwd juan
```

Si usamos el comando `id juan`, podemos ver la información del usuario, incluyendo su UID, GID y grupos a los que pertenece.

El comando `useradd` tiene varias opciones útiles, como `-m` para crear un directorio home para el usuario y `-G` para añadir el usuario a grupos adicionales.

Podéis buscar cual es la diferencia entre los comandos `useradd` y `adduser`?

### Crear un grupo

Para crear un nuevo grupo en Linux, utilizamos el comando `groupadd` seguido del nombre del grupo. Por ejemplo:

```bash
sudo groupadd desarrolladores
```

Con este comando, hemos creado un grupo llamado "desarrolladores". Podemos añadir usuarios a este grupo utilizando el comando `usermod`:

```bash
sudo usermod -aG desarrolladores juan
```

Los argumentos `-aG` indican que estamos añadiendo (`-a`) el usuario a un grupo secundario (`-G`).

### Eliminar un usuario o grupo

Para eliminar un usuario, utilizamos el comando `userdel` seguido del nombre del usuario. Por ejemplo:

```bash
sudo userdel juan
```

Para eliminar un grupo, utilizamos el comando `groupdel` seguido del nombre del grupo. Por ejemplo:

```bash
sudo groupdel desarrolladores
```

### Iniciar sesión como otro usuario

Para iniciar sesión como otro usuario sin cerrar la sesión actual, utilizamos el comando `su` seguido del nombre del usuario. Por ejemplo:

```bash
su - juan
```

El comando `-` asegura que se cargue el entorno del usuario al iniciar sesión.

## Gestión de procesos y servicios

En Linux, los procesos son programas en ejecución. Podemos gestionar los procesos utilizando comandos como `ps`, `top`, `kill` y `systemctl`.

### Visualizar procesos

Para ver los procesos en ejecución, utilizamos el comando `ps`:

```bash
ps aux
```

Este comando muestra una lista detallada de todos los procesos en ejecución, incluyendo el usuario que los inició, el PID (identificador del proceso), el uso de CPU y memoria, entre otros.

También podemos utilizar el comando `top` para ver los procesos en tiempo real:

```bash
top
```

### Finalizar procesos

Para finalizar un proceso, utilizamos el comando `kill` seguido del PID del proceso. Por ejemplo:

```bash
sudo kill 1234
```

La opción `-9` puede utilizarse para forzar la finalización de un proceso:

```bash
sudo kill -9 1234
``` 

### Gestión de servicios

En Linux, los servicios son programas que se ejecutan en segundo plano para proporcionar funcionalidades específicas. Podemos gestionar los servicios utilizando el comando `systemctl`.

Para iniciar un servicio, utilizamos:

```bash
sudo systemctl start nombre_servicio
```

Para detener un servicio, utilizamos:

```bash
sudo systemctl stop nombre_servicio
```

Para habilitar un servicio para que se inicie automáticamente al arrancar el sistema, utilizamos:

```bash
sudo systemctl enable nombre_servicio
```

Para deshabilitar un servicio, utilizamos:

```bash
sudo systemctl disable nombre_servicio
```

Para verificar el estado de un servicio, utilizamos:

```bash
sudo systemctl status nombre_servicio
```

Para listar todos los servicios disponibles, utilizamos:

```bash
systemctl list-units --type=service
```

## Gestión de la red en Linux

La configuración de la red en Linux se puede realizar utilizando varias herramientas y comandos. Algunos de los comandos más comunes para gestionar la red son `ifconfig`, `ip`, `nmcli` y `ping`.

### Configurar una interfaz de red

Para configurar una interfaz de red, podemos utilizar el comando `ip`. Por ejemplo, para asignar una dirección IP estática a una interfaz llamada `eth0`, utilizamos:

```bash
sudo ip addr add 192.168.1.100/24 dev eth0
```

Para activar la interfaz, utilizamos:

```bash
sudo ip link set eth0 up
```

### Verificar la configuración de red

Para verificar la configuración de red, utilizamos el comando `ip addr`:

```bash
ip addr
```

También podemos utilizar el comando `ping` para comprobar la conectividad con otro dispositivo en la red:

```bash
ping 192.168.1.1
```

El comando `nmcli` es otra herramienta útil para gestionar conexiones de red, especialmente en sistemas que utilizan NetworkManager.

```bash
nmcli device status
```

## Scripting para la automatización

Los scripts en Linux son archivos de texto que contienen una serie de comandos que se ejecutan secuencialmente. Los scripts se utilizan para automatizar tareas repetitivas y simplificar la administración del sistema.

Para crear un script, utilizamos un editor de texto para escribir los comandos y guardarlos con una extensión `.sh`. Por ejemplo, podemos crear un script llamado `backup.sh` que realice una copia de seguridad de un directorio:

En la primera línea del script, especificamos el intérprete que se utilizará para ejecutar el script, generalmente `#!/bin/bash` para scripts de Bash.

```bash
#!/bin/bash
tar -czvf backup.tar.gz /ruta/del/directorio
```

Para ejecutar el script, primero debemos darle permisos de ejecución utilizando el comando `chmod`:

```bash
chmod +x backup.sh
```

Luego, podemos ejecutar el script utilizando:

```bash
./backup.sh
```

### Lenguaje de scripting Bash

Bash (Bourne Again SHell) es el intérprete de comandos predeterminado en muchas distribuciones de Linux. Permite escribir scripts que pueden incluir variables, estructuras de control (como bucles y condicionales), funciones y más.

Los scripts de Bash se ejecutan en un entorno de línea de comandos y pueden interactuar con el sistema operativo para realizar tareas como la gestión de archivos, la configuración del sistema y la automatización de tareas.

Las estructuras de control en Bash incluyen:

- Condicionales (`if`, `else`, `elif`)
- Bucles (`for`, `while`, `until`)
- Funciones (`function nombre_funcion { ... }`)

Un ejemplo simple de un script de Bash que utiliza una estructura condicional es:

```bash
#!/bin/bash
echo "Introduce un número:"
read numero
if [ $numero -gt 10 ]; then
    echo "El número es mayor que 10."
else
    echo "El número es 10 o menor."
fi
```

Un ejemplo de script de Bash que utiliza un bucle es:

```bash
#!/bin/bash
for i in {1..5}; do
    echo "Número: $i"
done
```

Para profundizar en Bash y scripting en Linux, podéis consultar la documentación oficial de Bash y otros recursos en línea. Por ejemplo, el libro "The Linux Command Line" de William Shotts es una excelente referencia para aprender más sobre Bash y la línea de comandos en Linux.

Los argumentos de línea de comandos pueden ser accedidos en un script de Bash utilizando variables especiales como `$1`, `$2`, etc., que representan los argumentos pasados al script. El número total de argumentos se puede obtener con `$#`.

## [Práctica en clase](practica_usuarios.md)