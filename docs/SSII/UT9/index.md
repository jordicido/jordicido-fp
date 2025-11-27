# UT 9. Docker y contenedores

## Contexto

Docker es una plataforma de software que permite crear, desplegar y gestionar aplicaciones dentro de contenedores. Los contenedores son entornos ligeros y portátiles que incluyen todo lo necesario para ejecutar una aplicación, lo que facilita su despliegue en diferentes entornos sin preocuparse por las dependencias del sistema operativo.

## Diferencias entre máquinas virtuales y contenedores

Cuando hablamos de virtualización, es importante distinguir entre máquinas virtuales y contenedores. Ambas tecnologías permiten ejecutar aplicaciones en entornos aislados, pero lo hacen de maneras diferentes. Las máquinas virtuales emulan un sistema operativo completo, mientras que los contenedores comparten el kernel del sistema operativo host, lo que los hace más ligeros y eficientes.

| Característica           | Máquina Virtual                      | Contenedor                          |
|-------------------------|-------------------------------------|------------------------------------|
| Aislamiento             | Completo (incluye sistema operativo)| Parcial (comparte el kernel del host) |
| Tamaño                  | Grande (varios GB)                  | Pequeño (varios MB)                  |
| Tiempo de arranque      | Lento (minutos)                     | Rápido (segundos)                   |
| Uso de recursos         | Alto                              | Bajo                               |
| Portabilidad            | Menos portátil                      | Muy portátil                       |  
| Gestión                 | Más compleja                        | Más sencilla                       |

## Ventajas de usar contenedores

- **Portabilidad**: Los contenedores pueden ejecutarse en cualquier entorno que soporte Docker, garantizando que la aplicación funcione de la misma manera en desarrollo, pruebas y producción.
- **Eficiencia**: Los contenedores son ligeros y utilizan menos recursos que las máquinas virtuales, lo que permite ejecutar más instancias en el mismo hardware.
- **Aislamiento**: Cada contenedor opera de manera independiente, lo que mejora la seguridad y facilita la gestión de aplicaciones.
- **Facilidad de despliegue**: Docker simplifica el proceso de despliegue de aplicaciones, permitiendo a los desarrolladores empaquetar todo lo necesario en un contenedor.u

## Primeros pasos con Docker

Para comenzar a usar Docker, es necesario instalar Docker Desktop en tu sistema operativo. Docker Desktop está disponible para Windows y macOS, y proporciona una interfaz gráfica para gestionar contenedores, imágenes y volúmenes.

Aquí tienes los pasos básicos para instalar Docker Desktop en Windows: [Instalación Docker en Windows](./instalar_docker.md)

Una vez instalado Docker Desktop, puedes comenzar a crear y gestionar contenedores utilizando la línea de comandos o la interfaz gráfica proporcionada por Docker Desktop.

## Comandos básicos de Docker

Aquí tienes algunos comandos básicos para empezar a trabajar con Docker desde la línea de comandos:

- `docker --version`: Muestra la versión de Docker instalada.
- `docker pull nombre_imagen`: Descarga una imagen de Docker desde Docker Hub.
- `docker run -d -p puerto_host:puerto_contenedor nombre_imagen`: Crea y ejecuta un contenedor en segundo plano, mapeando puertos.
- `docker ps`: Lista los contenedores en ejecución.
- `docker ps -a`: Lista todos los contenedores, incluidos los detenidos.
- `docker stop id_contenedor`: Detiene un contenedor en ejecución.
- `docker rm id_contenedor`: Elimina un contenedor detenido.
- `docker images`: Lista las imágenes de Docker descargadas.
- `docker rmi id_imagen`: Elimina una imagen de Docker.
- `docker logs id_contenedor`: Muestra los registros de un contenedor.
- `docker exec -it id_contenedor bash`: Accede a la terminal de un contenedor en ejecución.

## Recursos adicionales

Para aprender más sobre Docker y contenedores, puedes consultar los siguientes recursos:
- [Documentación oficial de Docker](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/): Repositorio oficial de imágenes de Docker.
- [Tutoriales de Docker](https://www.docker.com/101-tutorial): Guías paso a paso para aprender a usar Docker.

## Imágenes de Docker

Las imágenes de Docker son plantillas inmutables que contienen todo lo necesario para ejecutar una aplicación, incluyendo el código, las bibliotecas, las dependencias y el sistema operativo. Las imágenes se utilizan para crear contenedores.

Las imágenes de Docker se pueden obtener de varios lugares, siendo Docker Hub el repositorio más popular. También es posible crear imágenes personalizadas utilizando Dockerfiles.

Para consultar las imágenes disponibles en Docker Hub, puedes visitar: [Docker Hub](https://hub.docker.com/)

## Volúmenes de Docker

### ¿Qué es un volumen en Docker?

Un **volumen** es un espacio de almacenamiento *persistente* que Docker usa para guardar datos **fuera del contenedor**.

**Idea clave:**
Los contenedores son *temporales*. Si borras un contenedor, sus datos se pierden.
Los volúmenes son *permanentes*. Aunque borres el contenedor, los datos siguen ahí.

### ¿Por qué son necesarios los volúmenes?

Porque muchas aplicaciones NECESITAN guardar datos:

* Bases de datos (PostgreSQL, MySQL, Mongo…)
* Servidores web que almacenan imágenes y documentos
* Aplicaciones que guardan logs
* Contenedores donde editas código
* Herramientas que necesitan configuraciones persistentes

Si no usas volúmenes → **todo se borra al reiniciar o eliminar el contenedor**.

### Tipos de volúmenes

Docker tiene **tres** formas de guardar datos persistentes.

---

#### Volúmenes nombrados

Los gestiona Docker.
No sabes dónde están, pero Docker se encarga por ti.

```bash
docker volume create mis_datos
```

Ejemplo de uso:

```bash
docker run -d \
  -v mis_datos:/var/lib/mysql \
  mysql:8
```

✔ Persistentes
✔ Portables
✔ Ideales para producción

#### Volúmenes anónimos

Se crean solos si no das un nombre.

Ejemplo:

```bash
docker run -v /var/lib/mysql mysql:8
```

Problema:
cuando eliminas el contenedor, los volúmenes quedan huérfanos.
⚠ Difícil de gestionar.

#### Bind Mounts

Perfectos para desarrollo.
Montas una carpeta de tu PC dentro del contenedor.

Ejemplo:

```bash
docker run -d \
  -p 8080:80 \
  -v $(pwd)/html:/usr/share/nginx/html \
  nginx
```

Todo lo que modifiques en `html/` aparece instantáneamente en el contenedor.

✔ Ideal para programar
✔ Puedes editar archivos desde tu IDE
✔ Sin reconstruir imágenes

### Qué pasa si NO usas volúmenes?

Ejemplo con PostgreSQL:

```bash
docker run -d --name pg postgres:16
```

Después, dentro de PostgreSQL creas tablas y metes datos.
Pero si borras el contenedor:

```bash
docker rm -f pg
```

**pierdes TODA la base de datos**.

### Comandos importantes para trabajar con volúmenes

### Crear un volumen:

```bash
docker volume create volumen1
```

### Ver los volúmenes:

```bash
docker volume ls
```

### Inspeccionar:

```bash
docker volume inspect volumen1
```

### Borrar un volumen (solo si no lo usa un contenedor):

```bash
docker volume rm volumen1
```

### EJEMPLOS PRÁCTICOS


#### Persistencia de una Base de Datos (PostgreSQL)

```bash
docker volume create pgdata

docker run -d \
  --name pg \
  -e POSTGRES_PASSWORD=1234 \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16
```
Podemos meter datos y tablas.

```bash
docker exec -it pg psql -U postgres
CREATE TABLE prueba (id SERIAL PRIMARY KEY, nombre VARCHAR(50));
INSERT INTO prueba (nombre) VALUES ('Hola Mundo');
```

Al reiniciar o borrar el contenedor:

```bash
docker rm -f pg
docker run -d \
  --name pg \
  -e POSTGRES_PASSWORD=1234 \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16
```

→ Los datos siguen ahí.


#### Servidor web Nginx con contenido persistente

```bash
docker volume create webdata

docker run -d \
  --name web \
  -p 8080:80 \
  -v webdata:/usr/share/nginx/html \
  nginx
```

Si entras:

```bash
docker exec -it web bash
echo "Hola" > /usr/share/nginx/html/index.html
```

→ La web se guarda en el volumen.

---

#### Desarrollo web con bind mounts

Si tienes:

```
proyecto/
 └─ index.html
```

Lanzas:

```bash
docker run -d \
  -p 8080:80 \
  -v $(pwd):/usr/share/nginx/html \
  nginx
```

Cada vez que guardas un archivo → se actualiza al instante en el navegador.

✔ Perfecto para proyectos de clase o prácticas rápidas.

## Redes en Docker

Una red (network) en Docker es un **espacio virtual** donde los contenedores pueden comunicarse entre sí.

Es como un **WiFi privado** que solo ven tus contenedores.

**A través de una red, un contenedor puede:**

* conocer a otro por su **nombre**
* compartir puertos internos
* enviar datos
* actuar como cliente/servidor dentro del ecosistema Docker

### ¿Por qué existen las redes en Docker?

Porque muchas aplicaciones reales funcionan así:

* Un backend necesita conectarse a una base de datos
* Un servidor web necesita hablar con un backend
* Un microservicio necesita comunicarse con otros
* Un contenedor quiere consumir una API del contenedor vecino

Estos contenedores **no deben exponerse a Internet**, pero sí deben verse entre ellos.

### Tipos de redes en Docker

Docker incluye tres **drivers** principales:


#### bridge (la red por defecto)

* Si no dices nada, Docker conecta tus contenedores a `bridge`.
* Permite comunicación interna entre contenedores *si están en la misma red personalizada*.

> Nota importante:
> Dentro de `bridge` por defecto, no puedes resolver nombres de contenedores a no ser que sea una red *creada por el usuario*.


#### host

El contenedor comparte la red del host.

Útil en Linux cuando:

* quieres máxima velocidad
* quieres que un servidor escuche sin NAT


#### none

El contenedor queda **aislado**.
Sin Internet, sin red, sin nada.

Útil para seguridad o experimentos.

### Redes creadas por el usuario

Cuando creas tú la red, Docker activa un **DNS propio**, lo que permite que los contenedores se encuentren por nombre.

### Crear tu propia red

```bash
docker network create red1
```

Listar redes:

```bash
docker network ls
```

#### Ejemplo simple: dos contenedores que se ven entre sí

* Crear red:

```bash
docker network create damnet
```

* Crear contenedor 1:

```bash
docker run -dit --name c1 --network damnet ubuntu sh
```

* Crear contenedor 2:

```bash
docker run -dit --name c2 --network damnet ubuntu sh
```

* Desde c1:

```bash
ping c2
```

✔ Pueden verse
✔ Docker resuelve automáticamente el nombre `c2`
✔ Esto demuestra el DNS interno de Docker

### Comandos esenciales de redes

Crear red:

```bash
docker network create red1
```

Ver redes:

```bash
docker network ls
```

Inspeccionar red:

```bash
docker network inspect red1
```

Conectar un contenedor a una red:

```bash
docker network connect red1 mi_contenedor
```

Desconectar:

```bash
docker network disconnect red1 mi_contenedor
```

## Dockerfiles

Un **Dockerfile** es un archivo de texto que contiene **instrucciones** que Docker sigue para construir una **imagen personalizada**.

### ¿Por qué existen los Dockerfiles?

Porque aunque puedes usar imágenes oficiales de Docker Hub, tarde o temprano necesitas:

* Añadir tu propio código
* Configurar algo extra
* Instalar dependencias
* Preparar tu backend o script
* Servir tus propios archivos web

**Todo eso se hace construyendo tu propia imagen** con un Dockerfile.

### Instrucciones esenciales

Hay muchas instrucciones, pero con estas **6** puedes construir el 90% de todo lo útil:

1. **FROM** → imagen base
2. **COPY** → copiar archivos a la imagen
3. **WORKDIR** → cambiar directorio de trabajo
4. **RUN** → ejecutar comandos durante la construcción
5. **CMD** → comando que se ejecutará cuando arranque el contenedor
6. **EXPOSE** → documentar puertos que usará el contenedor

#### Imagen base: `FROM`

El Dockerfile siempre empieza con la imagen base:

```Dockerfile
FROM python:3.12
```

O:

```Dockerfile
FROM nginx:alpine
```

#### Copiar archivos: `COPY`

Sirve para meter archivos dentro de la imagen:

```Dockerfile
COPY . /app
```

#### Directorio de trabajo: `WORKDIR`

Equivalente al “cd” dentro de la imagen:

```Dockerfile
WORKDIR /app
```

A partir de aquí, todos los comandos se ejecutan dentro de `/app`.

#### Ejecutar comandos al construir: `RUN`

Para instalar paquetes, crear carpetas, etc.

Ejemplo:

```Dockerfile
RUN pip install flask
```

Esto sucede **solo al crear la imagen**, no al ejecutarla.

#### Ejecutar comando final al arrancar el contenedor: `CMD`

Esto es lo que el contenedor hace cuando se ejecuta.

```Dockerfile
CMD ["python", "app.py"]
```

Solo puede haber un CMD en el Dockerfile.


#### Exponer puertos: `EXPOSE`

Solo documentación interna, no abre el puerto por sí mismo.

```Dockerfile
EXPOSE 8080
```

#### Ejemplo 1: Servidor web estático

Carpeta:

```
proyecto/
 ├─ html/
 │   └─ index.html
 └─ Dockerfile
```

**Dockerfile:**

```Dockerfile
FROM nginx:alpine
COPY html /usr/share/nginx/html
EXPOSE 80
```

**Construir la imagen:**

```bash
docker build -t miweb:v1 .
```

**Ejecutarla:**

```bash
docker run -d -p 8080:80 miweb:v1
```

Al abrir en navegador:
`http://localhost:8080`



#### Ejemplo 2: App Python simple

Estructura:

```
app/
 ├─ app.py
 └─ Dockerfile
```

`app.py`:

```python
print("Hola desde Docker")
```

`Dockerfile`:

```Dockerfile
FROM python:3.12
WORKDIR /app
COPY . .
CMD ["python", "app.py"]
```

Construir:

```bash
docker build -t hola:v1 .
```

Ejecutar:

```bash
docker run hola:v1
```

### Comandos esenciales relacionados con Dockerfile

Construir imagen:

```bash
docker build -t nombre:tag .
```

Construir sin cache:

```bash
docker build --no-cache -t nombre:latest .
```

Ver imágenes:

```bash
docker images
```

## Docker Compose

**Docker Compose** es una herramienta que permite **levantar varios contenedores a la vez**, usando un único archivo de configuración llamado:

```
docker-compose.yml
```

Es como tener un *guion* donde escribes:

* qué servicios quieres arrancar
* qué imágenes usan
* qué puertos exponen
* qué volúmenes necesitan
* qué redes usan
* qué variables de entorno requieren

y luego ejecutarlo todo con:

```
docker compose up
```

### ¿Para qué sirve realmente Docker Compose?

* Levantar una aplicación compuesta por varios servicios
  (por ejemplo: **backend + base de datos + web + cache**)
* Declarar infraestructura de forma reproducible
* Evitar escribir comandos largos y repetitivos
* Configurar redes y volúmenes automáticamente
* Desarrollar aplicaciones con dependencias complejas


### Sintaxis esencial del archivo `docker-compose.yml`

La estructura mínima es:

```yaml
version: "3.8"

services:
  nombre_servicio:
    image: imagen
    ports:
      - "host:contenedor"
    environment:
      - VARIABLE=valor
    volumes:
      - volumen:destino
```

Elementos clave:

| Campo          | Significado                      |
| -------------- | -------------------------------- |
| `services:`    | Lista de contenedores a levantar |
| `image:`       | Imagen para ese servicio         |
| `build:`       | Construye usando Dockerfile      |
| `ports:`       | Publicación de puertos           |
| `volumes:`     | Persistencia de datos            |
| `environment:` | Variables de entorno             |
| `depends_on:`  | Orden de arranque                |
| `networks:`    | Redes internas                   |

---

### Ejemplo 1 – Nginx simple

Archivo `docker-compose.yml`:

```yaml
version: "3.8"

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
```

Levantar:

```bash
docker compose up -d
```

Ver estado:

```bash
docker compose ps
```

Parar:

```bash
docker compose down
```

### Ejemplo 2 — Web + Base de Datos independientes**

```yaml
version: "3.8"

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"

  db:
    image: postgres:16
    environment:
      POSTGRES_USER: usuario
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: practica
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

Docker Compose creará automáticamente:

* Una red interna
* Un volumen persistente
* Dos contenedores funcionando juntos

### **Actividad práctica**

1. Crear carpeta `compose-test/`
2. Dentro, crear un archivo `docker-compose.yml` con este contenido:

```yaml
version: "3.8"

services:
  alpine1:
    image: alpine
    command: ["sh", "-c", "while true; do echo hola; sleep 1; done"]

  alpine2:
    image: alpine
    command: ["sh", "-c", "while true; do echo adios; sleep 1; done"]
```

3. Ejecutar:

```bash
docker compose up
```

4. Ver cómo los dos contenedores imprimen mensajes simultáneamente.


## [Instalar Docker en Windows](./instalar_docker.md)
## [Práctica: Contenedores Docker básicos](./practica_contenedores.md)