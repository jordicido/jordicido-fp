# Guía docente propuesta — UT6: Programación orientada a objetos

## 1. Sentido del cambio

La UT6 anterior trataba automatización de tareas del sistema (`os`, `sys`,
`datetime` y programación de scripts). Se sustituye por una unidad monográfica
de POO porque, después de funciones, módulos, archivos y excepciones, el grupo
está en condiciones de organizar estado y comportamiento en clases. El cambio
permite conectar directamente con un proyecto más rico y reutilizable sin
introducir paquetes externos.

Esta es una planificación didáctica propuesta para el repositorio. No pretende
identificar resultados de aprendizaje ni criterios de evaluación oficiales del
módulo optativo valenciano. La referencia conceptual al currículo histórico
DAM de Cataluña (clases, objetos, constructores, composición, herencia,
visibilidad, métodos estáticos y sobrescritura) se utiliza únicamente como
orientación pedagógica; no se presenta como normativa vigente aplicable a este
módulo.

## 2. Prerrequisitos y objetivos observables

Se presupone que el alumnado ha trabajado en UT1–UT5: expresiones, condicionales,
bucles, colecciones, funciones, módulos, archivos, JSON básico y excepciones.

Al finalizar, cada estudiante debería poder:

- explicar clase, instancia, estado, atributo y método con un ejemplo propio;
- escribir un constructor que valide y guarde el estado en `self`;
- distinguir atributos de instancia, de clase e identidad de igualdad;
- encapsular un valor cuando exista una invariante que proteger;
- modelar composición y justificar una relación de herencia;
- implementar polimorfismo sin inspecciones repetidas de `type()`;
- separar módulos y mantener la entrada/salida fuera de la lógica;
- escribir pruebas de casos normales, límites y excepciones;
- serializar y reconstruir objetos simples con JSON.

## 3. Secuencia propuesta de 10 sesiones

Cada sesión puede durar 55–60 minutos. La columna “evidencia” sugiere un
producto pequeño que permite comprobar aprendizaje sin esperar al proyecto.

| Sesión | Explicación | Práctica guiada | Evidencia |
|---:|---|---|---|
| 1 | Motivación, clase, instancia, atributos, estado y métodos. | Convertir un diccionario de mascota en `Mascota`. | Dos instancias con estados independientes y explicación escrita. |
| 2 | `self`, `__init__`, parámetros, retorno y límites. | `Rectangulo` y `Producto`. | Pruebas de constructor, cálculo y error sin estado parcial. |
| 3 | Atributos de clase, identidad/igualdad y mutables compartidos. | Corregir el carrito con lista de clase. | Diagnóstico del error y test que demuestra independencia. |
| 4 | Encapsulación, `_atributo`, `@property`, invariantes y `__str__`. | Cuenta bancaria segura. | Transferencia válida y fallida con saldos intactos. |
| 5 | Composición y responsabilidades. | `Biblioteca`/`Libro` o `Equipo`/`Jugador`. | Diagrama pequeño y clase contenedora con búsqueda. |
| 6 | Herencia, `super()`, sobrescritura y composición frente a herencia. | Vehículos y personajes del ejercicio 10. | Lista mixta procesada mediante operación común. |
| 7 | Polimorfismo, duck typing, métodos de clase y estáticos. | Entradas de concierto. | Fábrica `desde_texto`, contador y validación de booleanos. |
| 8 | Módulos, punto de entrada y dependencias. | Esqueleto de Arena de héroes. | Importaciones limpias y menú mínimo separado. |
| 9 | Excepciones, `unittest`, JSON y reconstrucción. | Pruebas de aceptación y `to_dict()`. | Suite ejecutable con casos normales y errores. |
| 10 | Integración, revisión y metacognición. | Inicio del proyecto, revisión por parejas y demo. | Diagrama, checklist y presentación breve del diseño. |

### Adaptaciones de tiempo

- En 6 sesiones: combinar 1–2, 3–4, 5–6, 7, 8–9 y dedicar la última al
  proyecto y pruebas.
- En 8 sesiones: conservar separadas las sesiones 1, 2, 3–4, 5, 6, 7, 8 y
  9–10.
- Para ampliar: añadir persistencia JSON, una nueva subclase y pruebas de
  mutabilidad, sin adelantar patrones de diseño ni frameworks.

## 4. Correspondencia entre materiales

La teoría presenta cada abstracción antes de usarla en una actividad:

| Concepto | Teoría | Actividad | Proyecto |
|---|---|---|---|
| Clase, instancia, `self` | Secciones 2–4 | 1–4 | `Personaje` |
| Invariantes y errores | 6–7, 14 | 3, 5 | Vida, daño y nombres |
| Composición | 9 | 6–7 | `Arena` y `Combate` |
| Herencia y sobrescritura | 10 | 9–10 | Guerrero y Mago |
| Polimorfismo | 11 | 9–10, 12 | Lista de personajes |
| Clase/estático | 12 | 8 | Ampliaciones posibles |
| Módulos y entrada | 13 | 11–12 | `main.py` separado |
| Pruebas y JSON | 14–15 | reto opcional | tests y README |

Ninguna actividad exige clases abstractas, metaclases, patrones o bibliotecas
externas. El ejercicio 11 muestra errores deliberados y debe presentarse como
material de reparación, no como código válido.

## 5. Orientaciones didácticas

### Explicar `self`

Conviene dibujar dos cajas con la misma estructura y valores distintos. Al
llamar `luna.jugar()`, `self` es `luna`, no `toby`. Pedir al alumnado que
traduzca mentalmente `objeto.metodo(x)` a “llama al método pasando el objeto
como primer receptor” ayuda a comprender el mensaje de error sin convertir la
explicación en una regla mecánica.

### Atributos de clase

Mostrar una lista compartida y hacer que dos instancias la modifiquen suele ser
la demostración más eficaz. Después, distinguir un contador realmente compartido
de una colección que debe ser independiente. Pregunta útil: “¿qué objeto debe
ver este dato cambiado por todas las instancias?”.

### Validación

Usar una transferencia bancaria fallida: primero comprobar las dos cuentas,
después hacer las dos modificaciones. Pedir una prueba que compare el estado
antes y después del error. El objetivo no es memorizar `ValueError`, sino
entender la garantía de no dejar el objeto inconsistente.

### Composición frente a herencia

Formular dos frases: “un mago es un personaje” y “una arena tiene personajes”.
Si ambas frases no son naturales, evitar herencia. Pedir que el alumnado añada
una nueva clase y compruebe si puede utilizar la misma operación sin cambiar el
contenedor.

### Polimorfismo

Empezar con `atacar()` y mostrar primero la cadena de `if type(...)`, para luego
eliminarla. Recalcar que el contrato común puede ser informal en Python y que
duck typing no significa renunciar a validaciones ni a nombres claros.

## 6. Errores habituales y preguntas de discusión

Errores previsibles:

- confundir el parámetro `nombre` con `self.nombre`;
- olvidar `self` al declarar un método;
- usar una lista de clase para datos de cada instancia;
- devolver `None` porque se imprimió en lugar de usar `return`;
- modificar saldo, vida o stock antes de comprobar la operación;
- hacer heredar `Arena` de `Personaje` por compartir un nombre;
- repetir `if type(...)` en lugar de definir una operación común;
- importar `main` y ejecutar el menú durante una prueba;
- guardar una instancia directamente con `json.dump()` sin convertirla;
- probar solo el camino feliz.

Preguntas breves:

1. ¿Cuándo una función normal es mejor que una clase?
2. ¿Qué estado sería peligroso hacer público?
3. ¿Qué debe ocurrir si falla la segunda mitad de una operación compuesta?
4. ¿Qué puede probarse sin usar `input()`?
5. ¿Qué diferencia hay entre “el objeto está derrotado” y “el combate ha
   terminado”?

## 7. Mini-evaluación de salida

En los últimos diez minutos, pedir individualmente:

1. escribir una clase `Libro` con un atributo y un método que devuelva texto;
2. explicar por qué `self.lista = []` no debe sustituirse por `lista = []` en
   el cuerpo de la clase;
3. identificar si `Equipo`/`Jugador` es composición o herencia;
4. escribir una prueba que espere `ValueError`;
5. describir cómo reconstruir un objeto desde un diccionario JSON.

Se puede corregir con “conseguido / parcialmente / necesita apoyo” y usar las
respuestas para agrupar la práctica de la siguiente sesión.

## 8. Evaluación orientativa

Esta rúbrica es una herramienta didáctica propuesta, no un listado oficial de
criterios normativos:

| Nivel | Modelo y estado | Diseño | Pruebas y comunicación |
|---|---|---|---|
| Inicial | Clases incompletas o estado inconsistente. | Mezcla responsabilidades y usa herencia sin justificar. | Solo demuestra un caso y apenas documenta. |
| En progreso | Funciona en casos habituales con algunos errores límite. | Distingue parte de la composición y la herencia. | Tiene pruebas básicas y README parcial. |
| Adecuado | Mantiene invariantes y separa lógica de interfaz. | Usa polimorfismo y módulos con responsabilidades claras. | Cubre normales, límites y errores; comunica decisiones. |
| Avanzado | Diseño extensible, validaciones atómicas y código legible. | Justifica trade-offs y evita abstracciones innecesarias. | Tests completos, persistencia cuidada y documentación reproducible. |

## 9. Diferenciación y trabajo individual

Para apoyo, entregar una plantilla con firmas de métodos, un diagrama parcial y
casos de prueba guiados. Para alumnado que avanza rápido, pedir una subclase
nueva, persistencia JSON o una prueba de independencia de dos arenas, siempre
después de terminar los requisitos base.

El trabajo puede ser individual. Si se trabaja por parejas, alternar roles de
implementación y revisión, conservar autoría de cada decisión y exigir que
cada persona explique una prueba. Evitar que el menú absorba todo el tiempo:
el aprendizaje central está en las clases y sus contratos.
