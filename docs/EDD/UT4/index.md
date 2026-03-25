# Conceptos básicos de Git

Git es un sistema de control de versiones distribuido que permite a los desarrolladores rastrear cambios en el código fuente a lo largo del tiempo. A continuación se presentan algunos conceptos básicos de Git:

- **Repositorio (repo)**: Un repositorio es un espacio de almacenamiento donde se guarda el código fuente y su historial de cambios. Puede ser local (en tu máquina) o remoto (en un servidor).
- **Commit**: Un commit es una instantánea del estado del código en un momento dado. Cada commit tiene un mensaje que describe los cambios realizados.
- **Branch**: Una rama es una línea de desarrollo independiente dentro de un repositorio. Permite trabajar en diferentes características o correcciones de errores sin afectar la rama principal (generalmente llamada `main` o `master`).
- **Merge**: Un merge es el proceso de combinar dos ramas diferentes en una sola. Esto se utiliza para integrar cambios de una rama a otra.
- **Clone**: Clonar un repositorio significa crear una copia local de un repositorio remoto. Esto te permite trabajar en el código sin necesidad de estar conectado a Internet.
- **Push**: Hacer un push significa enviar tus commits locales a un repositorio remoto. Esto actualiza el repositorio remoto con tus cambios.
- **Pull**: Hacer un pull significa descargar los cambios del repositorio remoto a tu copia local. Esto actualiza tu repositorio local con los últimos cambios realizados por otros desarrolladores.

## Acciones básicas de Git

### Crear un repositorio local

Para crear un nuevo repositorio local, sigue estos pasos:

1. Abre la terminal o línea de comandos.
2. Navega hasta el directorio donde deseas crear el repositorio.
3. Ejecuta el siguiente comando:

   ```bash
   git init nombre_del_repositorio
   ```

   Esto creará un nuevo directorio llamado `nombre_del_repositorio` y lo inicializará como un repositorio Git.
4. Navega al nuevo directorio:

   ```bash
   cd nombre_del_repositorio
   ```

5. Crea un archivo README.md para describir tu proyecto:

   ```bash
   echo "# Mi Proyecto" > README.md
   ```

6. Agrega el archivo README.md al área de preparación (staging area):

   ```bash
   git add README.md
   ```

7. Realiza tu primer commit:

   ```bash
   git commit -m "Primer commit: agregar README.md"

   ```

8. Ahora tienes un repositorio local con un commit inicial.

### Crear un repositorio remoto

Para crear un repositorio remoto, puedes utilizar plataformas como GitHub, GitLab o Bitbucket. A continuación se muestra cómo crear un repositorio en GitHub:

1. Inicia sesión en tu cuenta de GitHub.
2. Haz clic en el botón "New" o "Crear nuevo repositorio".
3. Completa el formulario con el nombre del repositorio, la descripción y la visibilidad (público o privado).
4. Haz clic en "Create repository" para crear el repositorio.
5. Una vez creado, GitHub te proporcionará una URL para clonar el repositorio. Copia esta URL.
6. Vuelve a la terminal y navega al directorio de tu repositorio local.
7. Agrega el repositorio remoto utilizando el siguiente comando:

   ```bash
   git remote add origin URL_DEL_REPOSITORIO
   ```

   Reemplaza `URL_DEL_REPOSITORIO` con la URL que copiaste de GitHub.
8. Ahora puedes hacer un push de tu commit inicial al repositorio remoto:

   ```bash
   git push -u origin main
   ```

   Esto enviará tus cambios al repositorio remoto y establecerá la rama `main` como la rama de seguimiento.

### Clonar un repositorio remoto

Para clonar un repositorio remoto, sigue estos pasos:

1. Abre la terminal o línea de comandos.
2. Navega hasta el directorio donde deseas clonar el repositorio.
3. Ejecuta el siguiente comando:

   ```bash
   git clone URL_DEL_REPOSITORIO
   ```

   Reemplaza `URL_DEL_REPOSITORIO` con la URL del repositorio remoto que deseas clonar.
4. Esto creará una copia local del repositorio remoto en tu máquina.
5. Navega al directorio del repositorio clonado:

   ```bash
   cd nombre_del_repositorio
   ```

6. Ahora puedes trabajar en el código y realizar commits como lo harías en un repositorio local.

### Push y Pull

Para enviar tus cambios al repositorio remoto, utiliza el comando `git push`:

```bash
git push origin main
```

Esto enviará tus commits locales a la rama `main` del repositorio remoto.
Para descargar los cambios del repositorio remoto, utiliza el comando `git pull`:

```bash
git pull origin main
```

Esto actualizará tu repositorio local con los últimos cambios realizados por otros desarrolladores.

### Crear una rama

Para crear una nueva rama, utiliza el siguiente comando:

```bash
git branch nombre_de_la_rama
```

Reemplaza `nombre_de_la_rama` con el nombre que desees para la nueva rama. Esto creará una nueva rama basada en la rama actual.
Para cambiar a la nueva rama, utiliza el siguiente comando:

```bash
git checkout nombre_de_la_rama
```

Esto cambiará tu entorno de trabajo a la nueva rama.

### Hacer un merge

Para combinar los cambios de una rama en otra, primero asegúrate de estar en la rama a la que deseas fusionar los cambios. Luego, utiliza el siguiente comando:

```bash
git merge nombre_de_la_rama
```

Reemplaza `nombre_de_la_rama` con el nombre de la rama que deseas fusionar. Esto combinará los cambios de la rama especificada en la rama actual.

## Comandos utilizados

```bash
# Inicializar un nuevo repositorio
git init nombre_del_repositorio
# Navegar al directorio del repositorio
cd nombre_del_repositorio
# Crear un archivo README.md
echo "# Mi Proyecto" > README.md
# Agregar el archivo al área de preparación
git add README.md
# Realizar un commit
git commit -m "Primer commit: agregar README.md"
# Agregar el repositorio remoto
git remote add origin URL_DEL_REPOSITORIO
# Hacer un push al repositorio remoto
git push -u origin main
# Clonar un repositorio remoto
git clone URL_DEL_REPOSITORIO
# Cambiar a una rama
git checkout nombre_de_la_rama
# Crear una nueva rama
git branch nombre_de_la_rama
# Hacer un merge de una rama
git merge nombre_de_la_rama
# Hacer un pull del repositorio remoto
git pull origin main
# Hacer un push al repositorio remoto
git push origin main
```

## Ejercicios propuestos

[Práctica 1: Crear un nuevo repositorio local y realizar un commit inicial.](introduccion_git_prac1.md)

[Práctica 2: Crear un repositorio remoto en GitHub y hacer un push de tu commit inicial.](introduccion_git_prac2.md)

[Práctica 3: Clonar un repositorio remoto y realizar cambios en el código.](introduccion_git_prac3.md)

[Práctica 4: Crear una nueva rama, realizar cambios y hacer un merge con la rama principal.](introduccion_git_prac4.md)

## Conclusión

Git es una herramienta poderosa para el control de versiones y la colaboración en proyectos de software. Con estos conceptos básicos, puedes comenzar a utilizar Git para gestionar tu código y colaborar con otros desarrolladores. A medida que te familiarices con Git, podrás explorar características más avanzadas como rebase, cherry-pick y resolución de conflictos.

## Recursos adicionales

- [Documentación oficial de Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Git Immersion](http://gitimmersion.com/)
- [Learn Git Branching](https://learngitbranching.js.org/)
