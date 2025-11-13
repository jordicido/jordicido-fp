# UT 9. Docker y contenedores

# **1. ¿Qué es Docker?**

Docker es una tecnología que permite ejecutar aplicaciones dentro de **contenedores**, que son entornos ligeros, aislados y reproducibles.
En ellos podemos:

* Instalar versiones concretas de software
* Asegurar que el proyecto funciona igual en cualquier ordenador
* Evitar conflictos de dependencias
* Distribuir proyectos fácilmente

---

# **2. Requisitos previos en Windows**

Antes de instalar Docker, debemos comprobar:

### **2.1. Arquitectura del sistema**

* Windows 10 o 11
* Procesador compatible con virtualización (casi todos los modernos)

### **2.2. Virtualización activada**

Debes activar:

* **Virtualización (Intel VT-x / AMD-V)** desde la BIOS/UEFI
* En algunos casos, **Hyper-V** (si tienes Windows Pro)

---

# **3. Instalar Docker en Windows**

Existen **dos formas oficiales** de tener Docker en Windows. Se usa una u otra según tu versión del sistema.

---

## **3.1. Opción A: Docker Desktop (Windows 10/11 Home/Pro)**

### **Pasos a seguir:**

### **Paso 1 – Instalar WSL2 (Windows Subsystem for Linux 2)**

Abrir PowerShell como Administrador y ejecutar:

```
wsl --install
```

Reiniciar el equipo si es necesario.

### **Paso 2 – Instalar una distribución Linux**

Windows descargará Ubuntu automáticamente o te permitirá elegir.

### **Paso 3 – Descargar Docker Desktop**

Buscar en Google: **Docker Desktop for Windows**
Instalar desde la web oficial.

### **Paso 4 – Configurar**

Durante la instalación, marcar:

* ✔ *Use WSL 2 instead of Hyper-V*

### **Paso 5 – Finalizar**

Reiniciar el equipo si lo solicita.
Docker Desktop se iniciará automáticamente.

---

# **4. Modos de funcionamiento de Docker en Windows**

Docker funciona sobre un motor Linux. En Windows puede funcionar de estas formas:

---

## **4.1. Modo WSL 2 (recomendado)**

* Kernel Linux real
* Mejor rendimiento
* Ideal para desarrollo
* Disponible en Windows Home y Pro

---

## **4.2. Modo Hyper-V**

* Requiere Windows Pro/Enterprise/Education
* Usado históricamente por Docker
* Menor rendimiento que WSL2

---

## **4.3. Docker Engine en WSL (modo Linux puro)**

* No usa Docker Desktop
* Ligero
* Todo se hace desde terminal

---

# **5. ¿Cómo usar Docker una vez instalado?**

Puedes trabajar con Docker de tres maneras.

---

## **5.1. Terminal (PowerShell, CMD o Linux WSL2)**

Ejemplos básicos:

### Probar Docker:

```bash
docker run hello-world
```

### Listar contenedores:

```bash
docker ps
```

### Descargar una imagen:

```bash
docker pull ubuntu
```

### Crear y entrar en un contenedor:

```bash
docker run -it ubuntu bash
```

---

## **5.2. Docker Desktop (Interfaz gráfica)**

Permite ver:

* Contenedores activos
* Imágenes descargadas
* Volúmenes
* Logs de contenedores
* Estadísticas de uso

Excelente para que los estudiantes entiendan visualmente cómo funciona Docker.

---

## **5.3. Visual Studio Code (extensión Docker)**

VS Code permite:

* Ver contenedores e imágenes
* Crear Dockerfiles
* Abrir carpetas dentro de contenedores
* Ejecutar comandos sin usar terminal

Ideal para principiantes.

---

# **6. Tabla resumen para alumnos**

| Opción                       | Requisitos              | Ventajas              | Limitaciones        |
| ---------------------------- | ----------------------- | --------------------- | ------------------- |
| **Docker Desktop (WSL2)**    | Windows Home/Pro + WSL2 | Rápido, sencillo, GUI | Ocupa más recursos  |
| **Docker Desktop (Hyper-V)** | Windows Pro             | Estable               | No funciona en Home |
| **Docker Engine en WSL2**    | Solo WSL2 Linux         | Muy ligero            | Sin GUI             |


