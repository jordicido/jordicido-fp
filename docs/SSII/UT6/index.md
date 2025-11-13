# UT 6: Gestión de la información en sistemas operativos propietarios: Windows

## Introducción

En esta unidad, aprenderemos a gestionar la información en sistemas operativos Windows. Veremos cómo funcionan los sistemas de archivos en Windows, los comandos básicos para la gestión de archivos y directorios desde CMD y PowerShell, el usuario Administrador y UAC, los permisos y propiedades de archivos, y la estructura del sistema operativo Windows.

## Sistemas de archivos en Windows

Windows utiliza principalmente el sistema de archivos NTFS (New Technology File System), aunque también soporta FAT32 y exFAT para dispositivos extraíbles. NTFS ofrece características avanzadas como:

- Permisos de seguridad granulares
- Compresión de archivos
- Cifrado de archivos (EFS - Encrypting File System)
- Cuotas de disco
- Journaling para recuperación de datos
- Soporte para archivos y volúmenes grandes

La estructura de archivos en Windows se organiza por unidades (C:, D:, E:, etc.), donde cada unidad representa una partición o dispositivo de almacenamiento. La unidad C: suele contener el sistema operativo y los archivos de programa.

Cuando conectáis un dispositivo de almacenamiento externo (como un pendrive o un disco duro) en Windows, el sistema lo detecta automáticamente y le asigna una letra de unidad. Si el sistema de archivos no es compatible (por ejemplo, ext4 de Linux), Windows puede solicitar formatear el dispositivo o necesitaréis software de terceros para acceder a los datos.

## CMD (Símbolo del sistema)

Windows utiliza CMD como interfaz de línea de comandos, heredera de MS-DOS. Para abrirlo: Win + R, escribir `cmd` y Enter, o buscarlo en el menú inicio.

## Comandos básicos para la gestión de archivos y directorios

Aunque Windows cuenta con el Explorador de archivos (GUI), es fundamental conocer los comandos de línea de comandos para tareas administrativas y automatización:

- `dir`: Lista los archivos y directorios.
- `cd`: Cambia el directorio actual. Sin parámetros muestra la ruta actual.
- `mkdir` o `md`: Crea un nuevo directorio.
- `del`: Elimina archivos.
- `rmdir` o `rd`: Elimina directorios.
- `copy`: Copia archivos.
- `xcopy`: Copia archivos y directorios con más opciones.
- `move`: Mueve o renombra archivos o directorios.
- `ren`: Renombra archivos o directorios.
- `type`: Muestra el contenido de un archivo de texto.
- `cls`: Limpia la pantalla de la consola.

## Argumentos y Parámetros de Línea de Comandos

Los comandos pueden aceptar argumentos y parámetros (modificadores o switches) para modificar su comportamiento:

```cmd
dir /w C:\Users\Usuario
```

- `/w`: parámetro que indica formato de lista ancha
- `C:\Users\Usuario`: argumento que especifica el directorio a listar

**Para consultar la ayuda**, la mayoría de comandos aceptan `/?`:
```cmd
dir /?
xcopy /?
help dir
```

## Rutas Absolutas y Relativas

En Windows, las rutas pueden ser absolutas o relativas. Windows usa la barra invertida (`\`) como separador de directorios.

**Ruta absoluta:**
```cmd
C:\Users\Usuario\Documentos\archivo.txt
```

**Ruta relativa:**
```cmd
Documentos\archivo.txt
```

**Notación especial:**
- `.` representa el directorio actual
- `..` representa el directorio padre

**Ejemplos:**
```cmd
cd ..                          REM Sube un nivel
cd ..\..                       REM Sube dos niveles
cd Documentos\Proyectos        REM Ruta relativa hacia abajo
```

## Redirecciones de Entrada y Salida

En Windows, es posible redirigir la entrada y salida de los comandos utilizando operadores especiales:

**Operadores de redirección:**
- `>`: Redirige la salida a un archivo, sobrescribiendo su contenido.
- `>>`: Redirige la salida a un archivo, agregando al final.
- `<`: Redirige la entrada desde un archivo.
- `|`: Pipe - conecta la salida de un comando con la entrada de otro.

**Ejemplos:**
```cmd
dir > lista.txt
```
Crea (o sobrescribe) el archivo `lista.txt` con la lista de archivos del directorio actual.

```cmd
dir >> lista.txt
```
Añade la salida al final del archivo `lista.txt` sin sobrescribir.

```cmd
dir C:\DirectorioInexistente 2> errores.txt
```
Redirige los mensajes de error al archivo `errores.txt`.

## Ayuda y documentación

La mayoría de comandos aceptan el modificador `/?` para mostrar información de ayuda:

```cmd
dir /?
copy /?
xcopy /?
```

También existe el comando `help`:
```cmd
help
help dir
```

**Recursos adicionales:**
- Documentación oficial de Microsoft: docs.microsoft.com
- Foros de la comunidad y Stack Overflow

## El usuario Administrador y UAC

En Windows, el usuario Administrador tiene privilegios completos para realizar cualquier operación en el sistema. Sin embargo, Windows implementa el Control de Cuentas de Usuario (UAC - User Account Control) como medida de seguridad.

### Control de Cuentas de Usuario (UAC)
UAC es una característica de seguridad que solicita confirmación o credenciales cuando se intentan realizar tareas que requieren permisos de administrador. Esto ayuda a prevenir cambios no autorizados en el sistema.

### Ejecutar como Administrador
Para ejecutar un programa o comando con privilegios elevados:

**Desde la GUI:**
- Clic derecho en un programa o acceso directo
- Seleccionar "Ejecutar como administrador"

**Desde CMD:**
- Buscar "CMD" en el menú inicio
- Clic derecho y seleccionar "Ejecutar como administrador"
- La ventana mostrará "Administrador" en el título

**Verificar si tienes privilegios de administrador:**
```cmd
net session
```
Si no muestra errores, tienes privilegios de administrador.

## Permisos y propiedades de archivos

En Windows, el sistema de permisos NTFS es más complejo que en sistemas más antiguos como FAT32. Los permisos determinan qué usuarios y grupos pueden acceder y modificar archivos y directorios.

### Tipos de permisos básicos en NTFS:
- **Control total**: Todos los permisos, incluida la capacidad de cambiar permisos y propietario
- **Modificar**: Leer, escribir, eliminar archivos y subcarpetas
- **Lectura y ejecución**: Ver contenido y ejecutar programas
- **Lectura**: Ver archivos y propiedades
- **Escritura**: Crear archivos y escribir datos

### Ver permisos desde la GUI:
1. Clic derecho en un archivo o carpeta
2. Seleccionar "Propiedades"
3. Ir a la pestaña "Seguridad"
4. Aquí se muestran los usuarios/grupos y sus permisos

### Ver permisos desde CMD:
```cmd
icacls archivo.txt
icacls C:\Carpeta
```

El comando `icacls` muestra los permisos de forma abreviada:
- `F` = Control total (Full)
- `M` = Modificar
- `RX` = Lectura y ejecución
- `R` = Lectura (Read)
- `W` = Escritura (Write)

**Ejemplo de salida:**
```cmd
archivo.txt NT AUTHORITY\SYSTEM:(F)
            BUILTIN\Administrators:(F)
            DESKTOP-PC\Usuario:(R,W)
```

## Cambiar los permisos de un archivo

Para cambiar los permisos de archivos y directorios en Windows, se utiliza el comando `icacls`:

**Sintaxis básica:**
```cmd
icacls archivo.txt /grant Usuario:(permisos)
```

**Ejemplos:**
```cmd
icacls archivo.txt /grant Usuario:(F)          REM Control total
icacls archivo.txt /grant Usuario:(R)          REM Lectura
icacls archivo.txt /grant Usuario:(R,W)        REM Lectura y escritura
icacls archivo.txt /remove Usuario             REM Quitar permisos
icacls C:\Carpeta /grant Usuario:(F) /T        REM Recursivo
```

## Cambio de propietario

Para cambiar el propietario de un archivo o directorio en Windows:

**Usar takeown para tomar propiedad:**
```cmd
takeown /f archivo.txt
takeown /f C:\Carpeta /r /d y        REM Recursivo
```

**Usar icacls para cambiar el propietario:**
```cmd
icacls archivo.txt /setowner NuevoUsuario
icacls C:\Carpeta /setowner NuevoUsuario /T        REM Recursivo
```

**Nota:** Necesitáis permisos de administrador para cambiar propietarios.

## Pipes

Los pipes (`|`) conectan la salida de un comando con la entrada de otro, permitiendo encadenar comandos:

**Ejemplos:**
```cmd
dir | find "txt"                    REM Filtrar archivos que contienen "txt"
dir | sort                          REM Ordenar resultados
dir C:\Windows\System32 | more      REM Paginar salida larga
dir | find /c /v ""                 REM Contar líneas
```

**Comandos útiles con pipes:**
- `find`: Busca texto
- `findstr`: Búsqueda con expresiones regulares
- `sort`: Ordena texto
- `more`: Pagina la salida

## Atributos de archivos en Windows

Windows utiliza atributos especiales para marcar características de archivos:

**Atributos principales:**
- **R** (Read-only): Solo lectura
- **H** (Hidden): Oculto
- **S** (System): Archivo del sistema
- **A** (Archive): Archivo modificado (para backups)

### Ver atributos:
```cmd
attrib archivo.txt
```

### Modificar atributos:
```cmd
attrib +h archivo.txt    REM Hace el archivo oculto
attrib -h archivo.txt    REM Quita el atributo oculto
attrib +r archivo.txt    REM Solo lectura
attrib -r archivo.txt    REM Quita solo lectura
```

**Aplicar de forma recursiva:**
```cmd
attrib +h C:\Carpeta\*.* /s /d
```

## Estructura del sistema operativo Windows

**Directorios principales:**

- **C:\Windows**: Archivos del sistema operativo
  - `System32`: Archivos y programas del sistema
  - `Temp`: Archivos temporales del sistema
- **C:\Program Files**: Programas instalados
- **C:\Users**: Perfiles de usuarios
  - `Usuario\Desktop`: Escritorio
  - `Usuario\Documents`: Documentos
  - `Usuario\Downloads`: Descargas
  - `Usuario\AppData`: Datos de aplicaciones
- **C:\ProgramData**: Datos compartidos de aplicaciones

**Variables de entorno:**

Windows utiliza variables de entorno para referenciar ubicaciones comunes:

```cmd
echo %USERPROFILE%     REM C:\Users\Usuario
echo %TEMP%            REM Carpeta temporal
echo %SYSTEMROOT%      REM C:\Windows
echo %PROGRAMFILES%    REM C:\Program Files
```

## [Práctica en clase](practica_comandos.md)