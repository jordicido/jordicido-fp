# **Práctica: Contenedores**

## Objetivo general

Comprender cómo ejecutar diferentes tipos de contenedores Docker y manipularlos con los comandos fundamentales:
`run`, `pull`, `exec`, `logs`, `stop`, `rm`, `ps`, `images`, `rmi`.

## Contenedores que lanzaremos

1. Linux Alpine o Ubuntu → **contendor interactivo**
2. PostgreSQL o MySQL → **base de datos real**
3. Nginx → **servidor web estático**

Cada uno enseña una habilidad distinta y no dependen entre sí.

---

# **Bloque 1 — Contenedor Linux (sistema operativo mínimo)**

Ideal para practicar `run -it`, comandos dentro del contenedor y la idea de “entorno aislado”.

### 🔹 1. Descargar imagen

```bash
docker pull ubuntu
```

### 🔹 2. Lanzar contenedor interactivo

```bash
docker run -it --name linux1 ubuntu sh
```

En este comando podemos ver los siguientes parámetros:
- `-it`: modo interactivo con terminal
- `--name linux1`: asigna el nombre “linux1” al contenedor
- `ubuntu`: imagen base
- `sh`: comando a ejecutar (shell)

Esto hace que entremos dentro del contenedor y podamos ejecutar comandos Linux.

### 🔹 3. Dentro del contenedor

```bash
ls
pwd
echo "hola docker" > saludo.txt
cat saludo.txt
```

### 🔹 4. Salir y comprobar que el contenedor sigue existiendo

```bash
docker ps -a
docker start -i linux1
```

---

# **Bloque 2 — Base de datos real**

No conectan nada, simplemente ven cómo funciona un servicio dentro de un contenedor.

### 🔹 1. Descargar imagen

```bash
docker pull postgres:16
```

### 🔹 2. Ejecutar un PostgreSQL básico

```bash
docker run -d \
  --name pg1 \
  -e POSTGRES_PASSWORD=1234 \
  -e POSTGRES_DB=practica \
  -p 5432:5432 \
  postgres:16
```

En este comando encontramos:
- `-d`: modo “desapegado” (detached), el contenedor se ejecuta en segundo plano
- `--name pg1`: nombre del contenedor
- `-e POSTGRES_PASSWORD=1234`: variable de entorno para la contraseña del usuario
- `-e POSTGRES_DB=practica`: variable de entorno para crear una base de datos llamada “practica”
- `-p 5432:5432`: mapeo de puertos (host:contenedor)
- `postgres:16`: imagen base

### 🔹 3. Ver logs

```bash
docker logs pg1
```

Los logs nos muestran que PostgreSQL está funcionando y escuchando en el puerto 5432. 

### 🔹 4. Entrar al intérprete SQL

```bash
docker exec -it pg1 psql -U postgres -d practica
```

Podemos entrar en el intérprete SQL de PostgreSQL mediante el comando `docker exec -it` para ejecutar comandos dentro del contenedor en ejecución.

Dentro pueden ejecutar:

```sql
SELECT version();
CREATE TABLE test(id SERIAL PRIMARY KEY, msg TEXT);
INSERT INTO test(msg) VALUES ('Hola desde la BBDD en Docker');
SELECT * FROM test;
\q
```

Si queremos salir del intérprete SQL, usamos `\q`.

Podemos ver, si abrimos un gestor de bases de datos como DBeaver o pgAdmin, que la base de datos `practica` existe y contiene la tabla `test` con los datos insertados.

---

# **Bloque 3 — Servidor web (Nginx)**

Ahora vamos a lanzar un servidor web estático con Nginx. Nginx es un servidor web muy popular y ligero.

### 🔹 1. Descargar e iniciar servidor web

```bash
docker pull nginx
docker run -d --name web1 -p 8080:80 nginx
```

El mecanismo es similar al de los otros contenedores anteriores.

### 🔹 2. Abrir navegador

Ir a:

```
http://localhost:8080
```

Verán la página de bienvenida de Nginx.

### 🔹 3. Ver logs

```bash
docker logs web1
```

### 🔹 4. Sustituir la página web dentro del contenedor

```bash
docker exec -it web1 bash
echo "<h1>Servidor Docker Nginx funcionando</h1>" > /usr/share/nginx/html/index.html
```

Con este comando entramos en el contenedor y modificamos la página web por defecto y podemos ver el cambio en el navegador.

Recargar navegador → **cambia la página**.

---

# **Bloque 4 — Gestión del ciclo de vida**

Clásicos que deben practicar sí o sí.

### 🔹 1. Mostrar imágenes

```bash
docker images
```

### 🔹 2. Mostrar contenedores

```bash
docker ps -a
```

### 🔹 3. Parar contenedores

```bash
docker stop linux1 pg1 web1
```

### 🔹 4. Arrancarlos de nuevo

```bash
docker start linux1
docker start web1
```

### 🔹 5. Borrar contenedores

```bash
docker rm linux1 pg1 web1
```

### 🔹 6. Borrar imágenes (si procede)

```bash
docker rmi ubuntu postgres:16 nginx
```

# **Bloque 5 — Contenedores extra**

## ** Un servidor Python ya preparado (sin programar, pero ven el backend funcionando)**

Imagen útil y simple: **Python Flask de ejemplo**

### Lanzarlo:

```bash
docker run -d -p 5000:5000 tiangolo/uwsgi-nginx-flask:python3.9
```

Ahora abre en navegador:

```
http://localhost:5000
```

Da una pequeña API que responde automáticamente.

Pueden entrar:

```bash
docker logs <id>
```

---

# **Un Portainer (GUI para gestionar Docker)**

### Lanzarlo:

```bash
docker run -d \
  -p 9000:9000 \
  --name portainer \
  -v /var/run/docker.sock:/var/run/docker.sock \
  portainer/portainer-ce
```

Abrir en navegador:

```
http://localhost:9000
```

---

# **Bloque 6 — Preguntas para reflexionar**


* ¿Qué es una imagen?
* ¿Qué es un contenedor?
* ¿Qué diferencia hay entre “parar” y “eliminar”?
* ¿Qué comando usarías para ver los contenedores activos?
* ¿Cómo entrarías en un contenedor en ejecución?
