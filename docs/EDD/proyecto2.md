# Proyecto 2: Análisis y diseño con UML

## Contexto
Imagina que una empresa de software te ha encargado el **análisis y diseño preliminar de un sistema de gestión para una biblioteca municipal**.  
El sistema permitirá gestionar el préstamo de libros, el control de usuarios (socios) y la supervisión del catálogo por parte del personal bibliotecario.

Este proyecto se centra en las fases iniciales del **análisis y diseño orientado a objetos**, utilizando **UML** para representar los **casos de uso** y las **clases** del sistema.

---

## Objetivo
Aplicar los conocimientos de **análisis de requisitos y modelado UML** para diseñar los diagramas fundamentales de un sistema de información, garantizando coherencia, corrección formal y claridad estructural.

---

## Requisitos funcionales
El sistema de gestión de biblioteca deberá permitir:

1. **Gestión de usuarios (socios y personal bibliotecario)**
   - Alta, baja y modificación de socios.
   - Consulta de datos personales e historial de préstamos.
   - Roles: socio, bibliotecario y administrador.

2. **Gestión del catálogo**
   - Registro, modificación y eliminación de libros.
   - Búsqueda por título, autor, género o ISBN.
   - Control del stock (disponible / prestado / reservado).

3. **Gestión de préstamos**
   - Registro de préstamos y devoluciones.
   - Control de fechas de vencimiento y penalizaciones por retraso.
   - Renovación y reserva de ejemplares.

4. **Consultas e informes**
   - Historial de préstamos por usuario o por libro.
   - Listado de ejemplares más prestados.
   - Registro de incidencias o pérdidas.

5. **Acceso diferenciado por rol**
   - El socio consulta catálogo e historial propio.
   - El bibliotecario gestiona usuarios, préstamos y libros.
   - El administrador supervisa y genera informes.

---

## Pistas para el **diagrama de clases**

### A. Detectar clases (del lenguaje del dominio)
- Sustantivos candidatos en los requisitos: **Libro**, **Ejemplar**, **Autor**, **Socio**, **Bibliotecario**, **Administrador**, **Préstamo**, **Reserva**, **Penalización**, **Catálogo**, **Incidencia**.
- Distingue entre **concepto “Libro”** (obra) y **“Ejemplar”** (copia física con código/estado).

### B. Relaciones típicas y multiplicidades
- **Libro 1..*—contiene—> Ejemplar** (composición si el ejemplar no tiene sentido sin el libro).  
- **Libro *<—>* Autor** (muchos a muchos; considera clase asociativa **Autoría** si necesitas rol/orden).  
- **Socio 1..*—tiene—> Préstamo**; **Préstamo 1—1 Ejemplar**; **Préstamo 1—1 Socio**.  
- **Socio 0..*—realiza—> Reserva**; **Reserva 1—1 Ejemplar**.  
- **Penalización 0..*—afecta—> Socio** (opcional, depende del alcance).  
- **Bibliotecario/Admin** podrían **heredar** de **Usuario** (generalización con atributo `rol` o jerarquía).

### C. Atributos mínimos sugeridos
- **Libro**: `isbn`, `titulo`, `anio`, `genero`.  
- **Ejemplar**: `codigoInventario`, `estado` (disponible/prestado/reservado), `ubicacion`.  
- **Socio**: `idSocio`, `nombre`, `email`, `fechaAlta`.  
- **Préstamo**: `idPrestamo`, `fechaInicio`, `fechaVencimiento`, `fechaDevolucion`.  
- **Reserva**: `idReserva`, `fechaReserva`, `estado` (activa/caducada).  
- **Usuario** (si lo usas): `id`, `nombre`, `email`, `passwordHash`.

### D. Operaciones típicas
- **Catálogo / Repositorio**: `buscarPorTitulo()`, `buscarPorAutor()`, `buscarPorISBN()`.  
- **Préstamo**: `registrar()`, `devolver()`, `estaVencido()`.  
- **Reserva**: `crear()`, `cancelar()`, `convertirEnPrestamo()`.  
- **Socio**: `calcularPenalizaciones()`, `puedePedirPrestamo()`.

### E. Decisiones de diseño típicas (explícalas en la justificación)
- **Generalización**: `Usuario` ← `Socio` / `Bibliotecario` / `Administrador`, o un único `Usuario` con `rol`.  
- **Composición vs agregación**: `Libro` ♦► `Ejemplar` suele ser **composición** (un ejemplar no existe sin su libro).  
- **Cardinalidades**: sé explícito (`0..1`, `1`, `1..*`, `*`), evita dejar relaciones sin multiplicidad.

### F. Buenas prácticas UML
- Nombres en **PascalCase** para clases y **camelCase** para atributos/métodos.  
- Marca visibilidad: `+` público, `-` privado, `#` protegido.  
- Mantén **consistencia** entre casos de uso y clases: cada caso de uso debe estar soportado por colaboraciones plausibles de clases.

---

## Tareas a realizar

### 1) Diagrama de casos de uso (**40%**)
- Identifica los actores principales del sistema.  
- Define los casos de uso y sus relaciones (**include**, **extend**, **generalización**).  
- Representa el diagrama con **notación UML correcta**.  
- Acompaña el diagrama con una **breve descripción** de los casos de uso principales.

### 2) Diagrama de clases (**60%**)
- Identifica las clases relevantes a partir del análisis anterior.  
- Define **atributos, métodos y relaciones** (asociación, agregación, composición, herencia).  
- Representa el diagrama con **notación UML** (visibilidad, multiplicidades, nombres significativos).  
- Añade una **justificación del diseño** (decisiones clave y trazabilidad con casos de uso).

---

## Criterios de evaluación y ponderación

| **Aspecto evaluado** | **Peso** | **Indicadores de logro** |
|-----------------------|----------|---------------------------|
| **1. Diagrama de casos de uso** | **40%** | - Identificación correcta de actores y casos de uso.<br>- Uso adecuado de relaciones (include, extend, generalización).<br>- Claridad y limpieza visual del diagrama.<br>- Corrección del lenguaje UML.<br>- Coherencia con el enunciado. |
| **2. Diagrama de clases** | **60%** | - Identificación adecuada de clases y relaciones.<br>- Corrección en el uso de asociaciones, agregaciones y composiciones.<br>- Atributos y métodos coherentes con la funcionalidad.<br>- Aplicación correcta del lenguaje UML.<br>- Presentación clara y estructurada del modelo. |

---

## Rúbrica detallada de evaluación

| **Criterio** | **Peso** | **Básico (1)** | **Medio (2)** | **Avanzado (3)** | **Experto (4)** |
|---------------|-----------|----------------|----------------|------------------|-----------------|
| **1. Identificación de actores y casos de uso** | 10% | Identifica pocos actores o casos; hay errores conceptuales. | Identifica la mayoría, aunque faltan algunos relevantes. | Identifica correctamente casi todos los actores y casos principales. | Identifica todos los actores y casos relevantes; refleja bien las interacciones del sistema. |
| **2. Uso de relaciones (include, extend, generalización)** | 10% | No usa relaciones o las aplica incorrectamente. | Usa algunas relaciones básicas, pero con errores o sin justificación. | Usa relaciones adecuadas y mayormente correctas. | Usa correctamente las relaciones UML con justificación lógica y coherente. |
| **3. Corrección formal y claridad del diagrama de casos de uso** | 20% | El diagrama es confuso o incumple las normas UML. | Presenta errores menores en la notación o disposición. | Cumple la notación UML y es comprensible. | Cumple perfectamente la notación UML, es claro, limpio y profesional. |
| **4. Identificación de clases y relaciones** | 20% | Faltan clases clave o las relaciones son incorrectas. | Incluye las clases principales pero hay algunas omisiones o errores. | Clases y relaciones adecuadas y coherentes con el sistema. | Clases y relaciones perfectamente justificadas y completas, coherentes con los casos de uso. |
| **5. Uso correcto de asociaciones, agregaciones, composiciones y herencia** | 15% | No aplica o confunde los tipos de relaciones. | Aplica algunas correctamente, pero con errores. | Usa adecuadamente la mayoría de las relaciones UML. | Usa todos los tipos de relaciones con precisión y justificación conceptual. |
| **6. Definición de atributos y métodos** | 10% | Atributos o métodos incorrectos o irrelevantes. | Incluye algunos adecuados, pero faltan o sobran varios. | La mayoría son apropiados y coherentes con el sistema. | Todos los atributos y métodos son precisos, coherentes y bien seleccionados. |
| **7. Corrección formal y legibilidad del diagrama de clases** | 15% | Desorganizado, difícil de leer o con errores de notación. | Presenta algunos errores formales o visuales. | Claramente estructurado y casi sin errores. | Estructura limpia, notación UML impecable, disposición visual profesional. |

---

### Total ponderado
- **Diagrama de casos de uso:** 40% (criterios 1–3)  
- **Diagrama de clases:** 60% (criterios 4–7)

---

## Recomendaciones de entrega
- Herramientas sugeridas: **StarUML, Visual Paradigm, Draw.io, PlantUML**.  
- Entrega en **PDF** con rotulado, multiplicidades y leyenda si procede.  
- Incluye una **página de justificación** (½–1 página) explicando decisiones clave del diseño.
