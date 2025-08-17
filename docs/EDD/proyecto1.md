# Proyecto 1: Profesionaliza tu proyecto Java

## Objetivo

Aplicar herramientas y prácticas profesionales del desarrollo de software sobre un proyecto Java ya desarrollado en el módulo de Programación o uno que yo os proveeré. El objetivo no es modificar la funcionalidad, sino estructurar, documentar, versionar y testear el proyecto como si fuera software profesional.

---

## Tareas a realizar

Tu trabajo consistirá en preparar el entorno del proyecto Java aplicando los siguientes aspectos:

---

### 1. **Control de versiones con Git**

* Crear un repositorio en **GitHub** (puede ser privado o público, aunque si es privado deberás invitarme al mismo).
* Subir correctamente el proyecto Java al repositorio, con estructura clara:

  ```
  /src/
  /test/
  /docs/
  README.md
  ```

* Aplicar una **estrategia de ramas**, como mínimo:
    * `main`: versión estable.
    * `dev`: desarrollo activo.
    * `feature/<nombre>`: ramas para mejoras o tareas.
* Realizar al menos **5 commits significativos** con mensajes descriptivos (no usar "subida", "commit 1", etc.).
* Crear un `.gitignore` que excluya archivos de compilación, temporales o IDEs.

---

### 2. **README.md en Markdown**

* Crear un archivo `README.md` en la raíz del repositorio con:
    * Nombre del proyecto.
    * Breve descripción funcional.
    * Requisitos para compilar y ejecutar.
    * Instrucciones de uso.
    * Autoría y licencia.

---

### 3. **Documentación técnica con Javadoc**

* Comentar las **clases y sus métodos públicos** usando la sintaxis estándar de **Javadoc**:

  ```java
  /**
   * Representa un producto en el inventario.
   * @author Nombre
   * @version 1.0
   */
  public class Producto {
      /**
       * Devuelve el precio con IVA.
       * @return precio final
       */
      public double calcularPrecioFinal() { ... }
  }
  ```

* Generar la documentación HTML con Javadoc y colocarla en la carpeta `/docs/`.

---

### 4. **Testing automático con JUnit**

* Añadir al proyecto **al menos 2 clases de test JUnit** en el paquete `/test`.
* Crear **métodos de prueba** para comprobar el funcionamiento de los métodos principales (casos positivos y negativos).
* Usar anotaciones como `@Test`, `@BeforeEach`, `@AfterEach`.

Ejemplo básico:

```java
@Test
void testCalcularPrecio() {
    Producto p = new Producto("Pan", 1.0, 10);
    assertEquals(1.1, p.calcularPrecioFinal(), 0.01);
}
```

---

### 5. **Gestión de dependencias con Maven o Gradle**

* Convertir el proyecto Java en un proyecto gestionado por **Maven** o **Gradle**:
    * Si usas **Maven**, incluir un `pom.xml`.
    * Si usas **Gradle**, incluir un `build.gradle`.
* Declarar como mínimo las dependencias necesarias para:
    * **JUnit 5**.
    * Cualquier otra librería adicional que uses (opcional).

---

## Entregables

* Enlace al repositorio con:
    * Estructura clara de carpetas.
    * README.md completo.
    * Código Java documentado con Javadoc.
    * Estructura de proyecto con Maven o Gradle.
    * Carpeta `docs/` con la documentación HTML generada.
    * Carpeta `test/` con pruebas JUnit funcionales.
    * Historial de commits y ramas en Git.

---

## Rúbrica de evaluación (EDD)

| Criterio                                         | Puntos |
| ------------------------------------------------ | ------ |
| Uso correcto de Git y estructura del repositorio | 2      |
| Commits claros y estrategia de ramas             | 2      |
| README en Markdown bien elaborado                | 1      |
| Documentación con Javadoc y carpeta `/docs/`     | 1      |
| Pruebas unitarias con JUnit                      | 2      |
| Configuración de Maven o Gradle funcional        | 2      |
| **Total**                                        | **10** |

