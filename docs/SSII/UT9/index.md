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

## Dockerfiles

Un Dockerfile es un archivo de texto que contiene una serie de instrucciones para construir una imagen de Docker personalizada. Cada instrucción en el Dockerfile define un paso en el proceso de construcción de la imagen.



## [Instalar Docker en Windows](./instalar_docker.md)
## [Práctica: Contenedores Docker básicos](./practica_contenedores.md)