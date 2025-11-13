# UT 7. Configuración de la información en sistemas operativos propietarios: Windows

## Introducción

En esta unidad, aprenderemos a configurar la información en sistemas operativos Windows. Veremos cómo gestionar usuarios y grupos, configurar la red, gestionar servicios y procesos desde CMD, y utilizar herramientas de configuración del sistema.

## Configuración de usuarios y grupos

En Windows, la gestión de usuarios y grupos es fundamental para la seguridad y organización del sistema. Utilizaremos comandos como `net user`, `net localgroup` para crear y gestionar usuarios y grupos desde CMD.

Los usuarios en Windows tienen un identificador único (SID - Security Identifier) y pertenecen a uno o más grupos. Los grupos permiten gestionar permisos de acceso a archivos y recursos del sistema de manera colectiva.

### Listar usuarios y grupos

Para ver todos los usuarios locales del sistema:

```cmd
net user
```

Para ver información detallada de un usuario específico:

```cmd
net user nombre_usuario
```

Para ver todos los grupos locales:

```cmd
net localgroup
```

Para ver los miembros de un grupo específico:

```cmd
net localgroup nombre_grupo
```

### Crear un usuario

Para crear un nuevo usuario en Windows, utilizamos el comando `net user`:

```cmd
net user juan contraseña123 /add
```

Este comando crea un usuario llamado "juan" con la contraseña especificada.

**Opciones útiles:**
```cmd
net user juan * /add                    REM Solicita la contraseña de forma segura
net user juan /add /fullname:"Juan Pérez"    REM Con nombre completo
net user juan /add /comment:"Usuario de prueba"    REM Con comentario
```

Para ver la información de un usuario:

```cmd
net user juan
```

Para cambiar la contraseña de un usuario existente:

```cmd
net user juan nueva_contraseña
```

### Crear un grupo

Para crear un nuevo grupo local en Windows, utilizamos el comando `net localgroup`:

```cmd
net localgroup desarrolladores /add
```

Este comando crea un grupo local llamado "desarrolladores".

Para añadir un usuario a un grupo:

```cmd
net localgroup desarrolladores juan /add
```

Para ver los miembros de un grupo:

```cmd
net localgroup desarrolladores
```

### Eliminar un usuario o grupo

Para eliminar un usuario:

```cmd
net user juan /delete
```

Para eliminar un grupo:

```cmd
net localgroup desarrolladores /delete
```

Para quitar un usuario de un grupo (sin eliminarlo del sistema):

```cmd
net localgroup desarrolladores juan /delete
```

### Grupos predefinidos importantes

Windows tiene grupos predefinidos con permisos específicos:

- **Administradores**: Control total del sistema
- **Usuarios**: Permisos estándar limitados
- **Usuarios avanzados**: Permisos intermedios
- **Invitados**: Acceso muy limitado

Para añadir un usuario al grupo Administradores:

```cmd
net localgroup Administradores juan /add
```

## Gestión de procesos y servicios

En Windows, los procesos son programas en ejecución. Podemos gestionar los procesos utilizando comandos como `tasklist`, `taskkill` y herramientas del sistema.

### Visualizar procesos

Para ver los procesos en ejecución:

```cmd
tasklist
```

Este comando muestra una lista de todos los procesos en ejecución, incluyendo el nombre del proceso, el PID (identificador del proceso) y el uso de memoria.

Para ver procesos con más detalles:

```cmd
tasklist /v
```

Para filtrar procesos por nombre:

```cmd
tasklist | find "chrome"
```

Para ver procesos de forma detallada con formato de tabla:

```cmd
tasklist /fo table
```

### Finalizar procesos

Para finalizar un proceso por su PID:

```cmd
taskkill /PID 1234
```

Para forzar la finalización de un proceso:

```cmd
taskkill /PID 1234 /F
```

Para finalizar un proceso por su nombre:

```cmd
taskkill /IM chrome.exe /F
```

Para finalizar todos los procesos con un nombre específico:

```cmd
taskkill /IM notepad.exe /F
``` 

### Gestión de servicios

En Windows, los servicios son programas que se ejecutan en segundo plano para proporcionar funcionalidades específicas. Podemos gestionar los servicios utilizando los comandos `sc` y `net`.

**Listar todos los servicios:**

```cmd
sc query
```

**Ver el estado de un servicio específico:**

```cmd
sc query nombre_servicio
```

**Iniciar un servicio:**

```cmd
net start nombre_servicio
```

o

```cmd
sc start nombre_servicio
```

**Detener un servicio:**

```cmd
net stop nombre_servicio
```

o

```cmd
sc stop nombre_servicio
```

**Configurar un servicio para inicio automático:**

```cmd
sc config nombre_servicio start= auto
```

**Configurar un servicio para inicio manual:**

```cmd
sc config nombre_servicio start= demand
```

**Deshabilitar un servicio:**

```cmd
sc config nombre_servicio start= disabled
```

**Ejemplos comunes:**

```cmd
net start spooler           REM Iniciar servicio de impresión
net stop spooler            REM Detener servicio de impresión
sc query type= service state= all    REM Listar todos los servicios
```

**Nota:** Es necesario ejecutar CMD como Administrador para gestionar servicios.

## Gestión de la red en Windows

La configuración de la red en Windows se puede realizar utilizando varios comandos desde CMD. Los comandos más comunes son `ipconfig`, `netsh`, `ping` y `tracert`.

### Ver la configuración de red

Para ver la configuración de red actual:

```cmd
ipconfig
```

Para ver información detallada de todas las interfaces:

```cmd
ipconfig /all
```

### Renovar dirección IP (DHCP)

Para liberar la dirección IP actual:

```cmd
ipconfig /release
```

Para obtener una nueva dirección IP del servidor DHCP:

```cmd
ipconfig /renew
```

### Limpiar caché DNS

```cmd
ipconfig /flushdns
```

### Configurar una IP estática

Para configurar una dirección IP estática, utilizamos `netsh`:

```cmd
netsh interface ip set address name="Ethernet" static 192.168.1.100 255.255.255.0 192.168.1.1
```

Donde:
- `Ethernet`: nombre de la interfaz de red
- `192.168.1.100`: dirección IP
- `255.255.255.0`: máscara de subred
- `192.168.1.1`: puerta de enlace

### Configurar DNS

```cmd
netsh interface ip set dns name="Ethernet" static 8.8.8.8
netsh interface ip add dns name="Ethernet" 8.8.4.4 index=2
```

### Verificar conectividad

Para comprobar la conectividad con otro dispositivo:

```cmd
ping 192.168.1.1
ping www.google.com
```

Para ver la ruta que siguen los paquetes:

```cmd
tracert www.google.com
```

### Ver conexiones activas

Para ver conexiones de red activas y puertos en escucha:

```cmd
netstat -ano
```

Para ver solo conexiones establecidas:

```cmd
netstat -ano | find "ESTABLISHED"
```

### Mostrar información de interfaces de red

```cmd
netsh interface show interface
```

### Habilitar/Deshabilitar una interfaz de red

```cmd
netsh interface set interface "Ethernet" admin=disable
netsh interface set interface "Ethernet" admin=enable
```

**Nota:** Se requieren permisos de administrador para modificar la configuración de red.