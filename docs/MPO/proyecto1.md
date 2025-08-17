# Proyecto 1: Generador de Cuestionarios Interactivo

## **Objetivo del proyecto**

Desarrollar una aplicación de consola en Python que permita realizar cuestionarios tipo test. El usuario podrá responder a una serie de preguntas, y el programa corregirá automáticamente las respuestas, mostrando la puntuación obtenida al finalizar.

---

## **Requisitos funcionales mínimos**

Tu aplicación deberá permitir:

1. Implementar un menú que se ejecute indefinidamente hasta que el usuario finalice, que permita las siguientes opciones:
```
### MENÚ ###
1 - Empezar cuestionario
2 - Ranking (opcional)
3 - Salir
```
2. **Mostrar una serie de preguntas** una a una al usuario.
3. Cada pregunta debe tener:
    * Enunciado de la pregunta.
    * Cuatro opciones de respuesta.
    * Una única opción correcta.
4. El usuario debe poder introducir su respuesta (por ejemplo: A, B, C o D).
5. El programa debe indicar si la respuesta es correcta o incorrecta.
6. Al finalizar el test, debe mostrar:
    * Número total de preguntas.
    * Número de aciertos.
    * Porcentaje de aciertos.
    * Una valoración final (por ejemplo: “¡Muy bien!”, “Necesitas practicar”, etc.).

---

## **Contenidos del módulo que se aplican**

* Tipos de datos primitivos y estructuras complejas (listas, diccionarios).
* Control de flujo (`if`, `elif`, `else`).
* Bucles (`for`, `while`).
* Funciones con parámetros y retorno.
* Entrada/salida de datos por consola.

---

## **Estructura sugerida del programa**

Puedes organizar tu programa en funciones como:

* `cargar_preguntas()` → Devuelve una lista de preguntas (pueden estar "hardcodeadas" al principio).
* `mostrar_pregunta(pregunta)` → Muestra la pregunta y sus opciones.
* `obtener_respuesta()` → Pide al usuario su respuesta y la valida.
* `corregir_respuesta(respuesta, correcta)` → Comprueba si es correcta.
* `mostrar_resultados(aciertos, total)` → Muestra el resumen final.

---

## **Ejemplo de estructura de una pregunta (diccionario)**

```python
{
    "pregunta": "¿Cuál es la capital de Francia?",
    "opciones": ["A. Madrid", "B. Roma", "C. París", "D. Berlín"],
    "respuesta_correcta": "C"
}
```

---

## **Extras (para subir nota o como ampliación)**

* Leer las preguntas desde un archivo `.json` o `.txt` (puedes usar el módulo `json` para leer la información `.json` y la función `open()` para los archivos `.txt`).
* Guardar los resultados del usuario (nombre y puntuación) en un fichero.
* Permitir elegir entre distintos temas o niveles de dificultad.
* Tiempo límite para cada pregunta.
* Sistema de ranking de usuarios.

---

## **Fases de trabajo sugeridas**

1. **Diseño del modelo de datos**: ¿Cómo guardarás las preguntas?
2. **Estructura básica del programa**: Flujo general y funciones principales.
3. **Implementación**: Desarrollo progresivo de funciones.
4. **Pruebas y validación**: Comprobar que todo funcione correctamente.
5. **Mejoras y presentación**: Añadir extras, limpiar código, comentarios, etc.

---

## **Rúbrica de evaluación (orientativa)**

| Criterio                            | Puntos |
| ----------------------------------- | ------ |
| Funcionalidad básica completa       | 4      |
| Uso correcto de funciones           | 2      |
| Uso adecuado de listas/diccionarios | 2      |
| Legibilidad y buenas prácticas      | 2      |
| **Total**                           | **10** |

---

## **Consejos finales**

* Comienza por lo básico y ve añadiendo funcionalidades poco a poco.
* Prueba tu código frecuentemente para detectar errores a tiempo.
* Utiliza comentarios para explicar partes complejas del código.
* No dudes en pedir ayuda si te atascas en algún punto.
