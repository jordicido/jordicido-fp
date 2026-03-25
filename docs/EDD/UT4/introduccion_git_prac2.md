# Introducción a Git: Práctica 2

Crear un repositorio remoto en GitHub y hacer un push de tu commit inicial.

## Objetivos

- Crear un repositorio remoto en GitHub.
- Hacer un push de tu commit inicial al repositorio remoto.
- Comprender la diferencia entre repositorios locales y remotos.

## Requisitos

- Tener Git instalado en tu sistema.
- Tener una cuenta en GitHub.
- Conocimientos básicos de comandos de terminal.
- Conocimientos básicos de Git.
- Haber completado la Práctica 1: Crear un nuevo repositorio local y realizar un commit inicial.

## Pasos a seguir

1. **Crea un nuevo repositorio remoto en GitHub**

    ??? summary "Solución"
        - Inicia sesión en tu cuenta de GitHub.
        - Haz clic en el botón "New" o "Crear repositorio" en la parte superior derecha de la página.
        - Asigna un nombre a tu repositorio y selecciona si deseas que sea público o privado.
        - Haz clic en "Crear repositorio".
  
2. **Copia la URL del repositorio remoto**

    ??? summary "Solución"
        - Una vez creado el repositorio, GitHub te proporcionará una URL para clonar el repositorio. Copia esta URL.
        - La URL tendrá un formato similar a `https://github.com/nombreUsuario/nombreRepositorio.git`
        - Si deseas usar SSH, la URL tendrá un formato similar a `git@github.com:nombreUsuario/nombreRepositorio.git`

3. **Configura el repositorio remoto en tu repositorio local**

    ??? summary "Solución"
        - Abre la terminal y navega hasta el directorio de tu repositorio local.
        - Usa el siguiente comando para agregar el repositorio remoto:
          ```bash
          git remote add origin <URL del repositorio remoto>
          ```
        - Reemplaza `<URL del repositorio remoto>` con la URL que copiaste en el paso anterior.

4. **Verifica que el repositorio remoto se ha agregado correctamente**

    ??? summary "Solución"
        - Usa el siguiente comando para verificar que el repositorio remoto se ha agregado correctamente:
          ```bash
          git remote -v
          ```
        - Deberías ver la URL del repositorio remoto en la salida del comando.
        - La salida debería ser similar a:
          ```
          origin
          ```

5. **Renombra la rama principal a `main` (opcional)**

    ??? summary "Solución"
        - Si tu repositorio remoto usa `main` como la rama principal, puedes renombrar tu rama local a `main` usando el siguiente comando:
          ```bash
          git branch -m main
          ```
        - Luego, actualiza el nombre de la rama en el repositorio remoto:
          ```bash
          git push -u origin main
          ```

6. **Haz un push de tu commit inicial al repositorio remoto**

    ??? summary "Solución"
        - Usa el siguiente comando para hacer un push de tu commit inicial al repositorio remoto:
          ```bash
          git push -u origin main
          ```
        - Si estás usando una rama diferente a `main`, reemplaza `main` con el nombre de tu rama actual.
        - Si es la primera vez que haces un push a este repositorio, es posible que se te pida que ingreses tus credenciales de GitHub.

7. **Verifica que el push se ha realizado correctamente**

    ??? summary "Solución"
        - Ve a tu repositorio en GitHub y verifica que tu commit inicial se ha subido correctamente.
        - Deberías ver el commit en la pestaña "Commits" del repositorio.

## Configura un certificado de seguridad (opcional)

Si estás usando HTTPS y tienes problemas de autenticación, puedes configurar un certificado de seguridad para evitar tener que ingresar tus credenciales cada vez que hagas un push. Puedes seguir las instrucciones en la [documentación oficial de GitHub](https://docs.github.com/es/authentication/keeping-your-account-and-data-secure/working-with-ssh-key-passphrases) para configurar un certificado de seguridad.

## Profundizando conceptos

En esta práctica, hemos aprendido a crear un repositorio remoto en GitHub y a hacer un push de nuestro commit inicial. Es importante entender la diferencia entre repositorios locales y remotos:

- **Repositorio local**: Es el repositorio que tienes en tu máquina local. Aquí es donde haces tus cambios y commits.
- **Repositorio remoto**: Es el repositorio que está alojado en un servidor (en este caso, GitHub). Aquí es donde compartes tu trabajo con otros y colaboras en proyectos.

![Esquema repositorios local y remoto](https://www.git-tower.com/learn/media/pages/git/ebook/en/command-line/remote-repositories/introduction/ca91d7d832-1741963922/basic-remote-workflow.png "Esquema repositorios local y remoto")
