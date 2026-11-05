# Ejercicios de clase UT4: Creación y uso de módulos

## Contexto

En muchos programas de consola repetimos las mismas tareas: imprimir títulos, construir menús, mostrar mensajes de error o solicitar al usuario números válidos. Si programamos estas operaciones cada vez que las necesitamos, duplicamos código y complicamos su mantenimiento.

En esta práctica vas a crear **dos módulos de utilidades en Python** que podrás importar desde otros programas:

- `salida.py`: para presentar información por consola de manera ordenada y con colores.
- `entrada.py`: para solicitar y validar datos introducidos por el usuario.

Los dos módulos serán **independientes** y después los utilizarás juntos en una pequeña demostración. **No debes crear un nuevo programa de gestión completo**; el objetivo es desarrollar funciones útiles y reutilizables, que podrás incorporar posteriormente a tu proyecto.

### Objetivos

Al finalizar la práctica deberías ser capaz de:

- Organizar funciones relacionadas en diferentes archivos `.py`.
- Importar y utilizar funciones creadas en otros módulos.
- Diseñar funciones con parámetros y valores por defecto.
- Distinguir entre funciones que **muestran información** y funciones que **devuelven datos**.
- Reutilizar funciones para evitar repetir código.
- Utilizar una biblioteca externa, `colorama`.
- Validar entradas sin que el programa finalice ante datos incorrectos.
- Comprobar y documentar el funcionamiento de las funciones desarrolladas.

### Estructura del trabajo

Crea una carpeta con esta estructura:

```text
utilidades_consola/
├── salida.py
├── entrada.py
├── demo_salida.py
├── demo_entrada.py
└── demo_integracion.py
```

Las funciones de los módulos se desarrollan dentro de `salida.py` y `entrada.py`. Los archivos `demo_*.py` se emplearán únicamente para probarlas.

---

## Ejercicio 1. Biblioteca de salida formateada con Colorama

### Situación

Queremos que distintas aplicaciones de consola puedan compartir el mismo aspecto visual sin copiar continuamente instrucciones `print()` y código de formato.

Para ello, vas a desarrollar un módulo llamado **`salida.py`**. Sus funciones permitirán mostrar mensajes, títulos, menús y datos estructurados.

### Preparación

1. Instala la biblioteca externa con el siguiente comando:

   ```bash
   pip install colorama
   ```

2. Investiga cómo funcionan `Fore`, `Style` y `Style.RESET_ALL` de `colorama`.
3. Crea el archivo `salida.py`.
4. Crea `demo_salida.py` para importar el módulo y comprobar cada función.

**Importante:** cuando una función aplique colores o estilos, el formato de la consola debe volver al estado normal al finalizar, para que los mensajes posteriores no hereden accidentalmente el color anterior.

### Funciones obligatorias

#### 1. `mostrar_mensaje(texto, color="blanco")`

Muestra por pantalla el texto recibido con el color indicado.

**Requisitos:**

- El primer parámetro será el texto a mostrar.
- El segundo parámetro será opcional y permitirá elegir como mínimo entre `rojo`, `verde`, `amarillo`, `azul`, `cian` y `blanco`.
- Si se utiliza el color por defecto, la salida debe mantener el aspecto normal de la terminal.
- Después de mostrar un mensaje coloreado, debe restablecer el formato de la consola.
- No devolverá ningún valor.

**Ejemplos de uso:**

```python
mostrar_mensaje("Operación completada", "verde")
mostrar_mensaje("Se ha producido un error", "rojo")
mostrar_mensaje("Bienvenido al programa")
```

Comprueba que el tercer mensaje aparece con el formato normal, no con el color utilizado anteriormente.

#### 2. `mostrar_titulo(texto, ancho=50)`

Imprime un título destacado y centrado entre separadores.

**Requisitos:**

- Recibir el texto del título y una anchura opcional.
- Mostrar una línea separadora arriba y otra abajo.
- Centrar el texto con relación a la anchura indicada.
- Utilizar algún color o estilo para destacar el título.
- Evitar que un título largo se corte: si no cabe en la anchura indicada, adaptar el formato para mostrarlo completo.

**Ejemplo orientativo de salida:**

```text
==================================================
                 GESTOR DE TAREAS
==================================================
```

#### 3. `mostrar_menu(titulo, opciones)`

Imprime un menú utilizando un título y una lista de opciones.

**Requisitos:**

- Recibir un título y una lista de cadenas de texto.
- Reutilizar `mostrar_titulo()` para presentar la cabecera.
- Numerar automáticamente las opciones comenzando por `1`.
- Añadir al final la opción `0. Salir`.
- Destacar visualmente el título y/o la opción de salida utilizando Colorama.
- Funcionar con listas de distintas longitudes.
- **No solicitar una opción al usuario:** esta función solo debe **mostrar** el menú.

**Ejemplo de uso:**

```python
mostrar_menu(
    "Gestión de alumnos",
    ["Añadir alumno", "Consultar alumnos", "Eliminar alumno"]
)
```

**Ejemplo orientativo de salida:**

```text
==================================================
                GESTIÓN DE ALUMNOS
==================================================
1. Añadir alumno
2. Consultar alumnos
3. Eliminar alumno
0. Salir
```

#### 4. `mostrar_lista(elementos, titulo="Listado")`

Muestra los elementos de una lista con numeración y un título.

**Requisitos:**

- Admitir listas con cadenas de texto o números.
- Mostrar un título y numerar los elementos a partir de `1`.
- Informar claramente cuando la lista esté vacía.
- No modificar la lista recibida.

**Ejemplo de uso:**

```python
mostrar_lista(["Python", "Java", "JavaScript"], "Lenguajes disponibles")
```

**Ejemplo orientativo de salida:**

```text
LENGUAJES DISPONIBLES
1. Python
2. Java
3. JavaScript
```

#### 5. `mostrar_ficha(datos, titulo="Información")`

Muestra la información de un diccionario de forma legible.

**Requisitos:**

- Recibir un diccionario con parejas clave-valor.
- Mostrar un título y presentar una línea por cada dato.
- Alinear los valores para facilitar la lectura, aunque las claves tengan longitudes diferentes.
- Funcionar con cualquier número de elementos.
- Mostrar un aviso si el diccionario está vacío.
- No modificar el diccionario recibido.

**Ejemplo de uso:**

```python
mostrar_ficha(
    {"Nombre": "Laura", "Edad": 21, "Curso": "2º DAM"},
    "Ficha del alumno"
)
```

**Ejemplo orientativo de salida:**

```text
FICHA DEL ALUMNO
Nombre : Laura
Edad   : 21
Curso  : 2º DAM
```

### Prueba del módulo

En `demo_salida.py`, importa el módulo `salida` y realiza las siguientes comprobaciones:

1. Muestra mensajes con diferentes colores y comprueba que la consola recupera su formato normal.
2. Imprime dos títulos con anchuras diferentes.
3. Genera dos menús con diferentes cantidades de opciones.
4. Muestra una lista con elementos y otra vacía.
5. Muestra una ficha con al menos cuatro campos.

### Requisitos generales del ejercicio

- Todas las funciones obligatorias estarán definidas en `salida.py`.
- Reutiliza otras funciones del propio módulo cuando tenga sentido.
- Documenta cada función con un *docstring* que explique su objetivo y sus parámetros.
- Importar `salida.py` **no debe ejecutar automáticamente las pruebas**.
- El formato visual debe ser coherente entre las distintas funciones.

---

## Ejercicio 2. Biblioteca de entrada y validación de datos

### Situación

Cuando una aplicación pide una edad, una cantidad o una puntuación, no puede dar por supuesto que la persona introducirá siempre un valor correcto. Debe comprobar el dato y, si es necesario, solicitarlo nuevamente.

En este ejercicio desarrollarás un módulo independiente llamado **`entrada.py`**, con funciones para pedir datos de forma segura y devolverlos ya convertidos al tipo adecuado.

Este módulo **no necesita Colorama**. Puedes usar `print()` e `input()` y centrarte en las funciones y las validaciones.

### Preparación

1. Crea el archivo `entrada.py`.
2. Crea `demo_entrada.py` para importar y probar sus funciones.
3. Investiga el funcionamiento de `try`, `except` y `ValueError` para evitar errores al convertir una entrada a `int` o `float`.

### Funciones obligatorias

#### 1. `pedir_texto(mensaje, obligatorio=True)`

Solicita una cadena de texto al usuario y la devuelve.

**Requisitos:**

- Mostrar el mensaje recibido como parámetro.
- Eliminar los espacios sobrantes al principio y al final.
- Si `obligatorio` es `True`, rechazar textos vacíos o formados únicamente por espacios.
- Si `obligatorio` es `False`, permitir una cadena vacía.
- Cuando la entrada no sea válida, informar del problema y volver a solicitarla.
- Devolver una cadena (`str`).

**Ejemplos de uso:**

```python
nombre = pedir_texto("Introduce tu nombre: ")
comentario = pedir_texto("Comentario opcional: ", False)
```

#### 2. `pedir_entero(mensaje)`

Solicita un número entero al usuario.

**Requisitos:**

- Permitir enteros positivos, negativos y el cero.
- Comprobar que el texto puede convertirse a `int`.
- Si no puede convertirse, mostrar un error y solicitar de nuevo el dato, sin finalizar el programa.
- Devolver un `int`.

**Ejemplo de interacción:**

```text
Introduce tu edad: hola
Error: debes introducir un número entero.
Introduce tu edad: 23
```

La función devolverá el número entero `23`.

#### 3. `pedir_decimal(mensaje)`

Solicita un valor numérico y lo devuelve como decimal.

**Requisitos:**

- Aceptar valores positivos y negativos, con o sin parte decimal.
- Admitir tanto `.` como `,` como separador decimal.
- Volver a pedir el dato si no es válido.
- Devolver siempre un `float`.

**Ejemplos de entradas válidas:** `12.5`, `12,5`, `-3.75`, `10`.

**Ejemplo de uso:**

```python
precio = pedir_decimal("Introduce el precio: ")
```

#### 4. `pedir_entero_rango(mensaje, minimo, maximo)`

Solicita un número entero dentro de un intervalo determinado.

**Requisitos:**

- Recibir un mensaje, un valor mínimo y un valor máximo.
- Reutilizar **obligatoriamente** `pedir_entero()` para obtener el valor.
- Comprobar que el número está entre `minimo` y `maximo`, **incluidos ambos límites**.
- Si el número no pertenece al intervalo, mostrar un aviso y repetir la solicitud.
- Devolver un `int` válido.

**Ejemplo de interacción:**

```text
Introduce una edad (18-65): 80
Error: el valor debe estar entre 18 y 65.
Introduce una edad (18-65): 30
```

La función devolverá `30`.

#### 5. `pedir_decimal_rango(mensaje, minimo, maximo)`

Solicita un número decimal dentro de un intervalo.

**Requisitos:**

- Recibir el mensaje y los límites mínimo y máximo.
- Reutilizar **obligatoriamente** `pedir_decimal()`.
- Comprobar que el número está dentro del intervalo, incluidos los límites.
- Informar del error y repetir la solicitud mientras no se introduzca un valor permitido.
- Devolver un `float` válido.

**Ejemplo de uso:**

```python
nota = pedir_decimal_rango("Introduce la nota: ", 0, 10)
```

**Ejemplos:**

- `-1,5` → No válido: fuera del intervalo.
- `12` → No válido: fuera del intervalo.
- `7,5` → Válido.
- `10` → Válido.

### Prueba del módulo

En `demo_entrada.py`, importa las funciones del módulo y crea una demostración que solicite:

1. Un nombre obligatorio.
2. Un comentario opcional.
3. Una edad entera.
4. Un precio decimal.
5. Una cantidad de unidades comprendida entre 1 y 100.
6. Una valoración decimal entre 0 y 10.

Al finalizar, muestra un resumen con los datos obtenidos.

Durante la prueba, introduce **intencionadamente valores incorrectos** para comprobar que el programa solicita de nuevo los datos y no termina con una excepción.

### Requisitos generales del ejercicio

- Define todas las funciones obligatorias en `entrada.py`.
- Las funciones deben **devolver el dato validado**; no es suficiente con imprimirlo.
- El código que utiliza estas funciones no debe tener que convertir nuevamente los datos a números.
- Reutiliza funciones cuando corresponda, en especial en las validaciones de rangos.
- Documenta las funciones mediante *docstrings*.
- No utilices variables globales para almacenar las entradas.
- Importar `entrada.py` **no debe iniciar automáticamente preguntas al usuario**.

---

## Actividad final. Integración de ambos módulos

Crea un archivo llamado **`demo_integracion.py`** en el que importes `salida` y `entrada` y compruebes que funcionan juntos.

El programa debe:

1. Mostrar un pequeño menú mediante `salida.mostrar_menu()`.
2. Solicitar una opción válida mediante una función de `entrada`.
3. Si se elige la opción de registrar información, solicitar un nombre y una puntuación entre 0 y 100.
4. Mostrar los datos registrados mediante `salida.mostrar_ficha()`.
5. Mostrar un mensaje de confirmación en verde con `salida.mostrar_mensaje()`.
6. Permitir salir con la opción `0`.

No es necesario desarrollar un sistema completo de almacenamiento de registros. **Esta actividad solo sirve para comprobar que los dos módulos pueden importarse y utilizarse conjuntamente.**

### Ejemplo orientativo de utilización de los módulos

El siguiente fragmento muestra cómo deberían poder utilizarse las funciones que has creado (no incluye la implementación de dichas funciones):

```python
import salida
import entrada

opciones = ["Registrar puntuación", "Consultar información"]
salida.mostrar_menu("Panel de control", opciones)

opcion = entrada.pedir_entero_rango(
    "Selecciona una opción: ", 0, len(opciones)
)

if opcion == 1:
    nombre = entrada.pedir_texto("Nombre: ")
    puntuacion = entrada.pedir_decimal_rango(
        "Puntuación (0-100): ", 0, 100
    )

    salida.mostrar_ficha({
        "Nombre": nombre,
        "Puntuación": puntuacion
    }, "Resultado")

    salida.mostrar_mensaje(
        "Datos registrados correctamente", "verde"
    )
```

El fragmento es **orientativo**: en tu demostración debes gestionar también las otras opciones del menú y la salida.

### Ampliación opcional

Implementa en `entrada.py` una función adicional:

**`pedir_opcion(mensaje, numero_opciones)`**

Esta función debe reutilizar `pedir_entero_rango()` para solicitar y devolver una opción válida desde `0` hasta `numero_opciones`, ambos incluidos. Después úsala en `demo_integracion.py`.

---

## Entrega

Entrega la carpeta `utilidades_consola` con:

- Los dos módulos `salida.py` y `entrada.py`.
- Los tres programas de demostración `demo_salida.py`, `demo_entrada.py` y `demo_integracion.py`.

Las funciones deben estar documentadas, tener nombres y parámetros adecuados y poder importarse sin ejecutar de inmediato las demostraciones.

**Recuerda:** el propósito es crear herramientas reutilizables que puedas incorporar a otros programas, especialmente al proyecto que ya estás desarrollando en clase.
