# Ejercicios de clase UT6: Programación orientada a objetos

Estos ejercicios son enunciados, no soluciones completas. Escribe código
legible, prueba primero los casos normales y después los errores, y separa la
lógica de las clases de la entrada y salida por pantalla. Salvo que se indique
lo contrario, utiliza únicamente la biblioteca estándar y nombres en español
coherentes.

## Normas de trabajo

1. Crea una carpeta o módulo por ejercicio y añade un pequeño bloque de uso
   protegido por `if __name__ == "__main__":`.
2. Los métodos que calculan o consultan deben devolver valores; no bases las
   pruebas en leer texto impreso por pantalla.
3. Valida los datos antes de modificar el estado. Documenta con una excepción
   apropiada qué entradas se rechazan.
4. Añade pruebas manuales o con `unittest` para cada caso solicitado.
5. No copies una solución completa de Internet: explica en comentarios las
   decisiones que no sean evidentes.

## Nivel 1 — Clases e instancias

### 1. Mascota virtual

**Objetivo:** practicar atributos de instancia, constructor, métodos que
modifican estado y límites.

Crea `Mascota` con `nombre`, `especie` y `energia`. La energía inicial será 50.
Implementa:

- `comer()`, que suma 15 sin superar 100;
- `jugar()`, que resta 20 sin bajar de 0;
- `mostrar_estado()`, que devuelve una cadena con nombre, especie y energía.

Crea dos mascotas, juega con una y comprueba que la energía de la otra sigue
siendo 50. Comprueba una mascota con energía 95 al comer y con energía 10 al
jugar. Decide qué ocurre con nombres vacíos y documenta tu validación.

**Comprobaciones esperadas:** `Mascota("Luna", "gato")` empieza en 50; después
de comer queda en 65; al jugar cinco veces no baja de 0; comer varias veces no
sube de 100.

**Reflexión:** ¿por qué `energia` debe ser un atributo de instancia y no una
lista o valor compartido en el cuerpo de la clase?

### 2. Semáforo

**Objetivo:** representar estados finitos y transiciones controladas.

Crea `Semaforo` con estado inicial `"rojo"`. El método `siguiente()` debe rotar
en este orden: `rojo → verde → amarillo → rojo`. `puede_pasar()` devuelve
`True` únicamente cuando el estado es `"verde"`.

Rechaza estados iniciales que no pertenezcan a la colección válida. Comprueba
la secuencia completa, varias vueltas y que dos semáforos sean independientes.

**Casos esperados:** el primer estado es rojo; tras una llamada es verde y
`puede_pasar()` es verdadero; tras dos llamadas es amarillo y es falso; tras
tres vuelve a rojo.

**Reflexión:** ¿te convendría permitir asignar el estado directamente desde
fuera o es más seguro obligar a pasar por `siguiente()`?

### 3. Producto de tienda

**Objetivo:** practicar validación, invariantes, métodos de modificación y
`__str__()`.

Define `Producto` con `nombre`, `precio` y `stock`. Implementa:

- `vender(cantidad)`, que reduce el stock si hay existencias;
- `reponer(cantidad)`, que incrementa el stock;
- `valor_inventario()`, que devuelve `precio * stock`;
- `__str__()`, que resume nombre, precio y stock.

Rechaza nombres vacíos, precios negativos, cantidades no positivas y ventas
superiores al stock. En cualquier error el stock debe permanecer intacto.

**Escenario:** crea `Producto("Cuaderno", 2.50, 10)`, vende 3, repone 5 y
comprueba stock 12 y valor 30.00. Prueba vender 20 y verifica que el stock no
cambia.

**Reflexión:** ¿qué diferencia hay entre que `vender()` devuelva `True` y que
lance `ValueError` cuando la venta no se puede realizar?

### 4. Rectángulos

**Objetivo:** combinar objetos, cálculos y listas de instancias.

Crea `Rectangulo` con dimensiones positivas `ancho` y `alto`. Implementa
`area()`, `perimetro()`, `es_cuadrado()` y `__str__()`.

Construye una lista con al menos cuatro rectángulos, recórrela y selecciona el
que tenga mayor área. No ordenes la lista original salvo que lo necesites.
Prueba dimensiones decimales, un cuadrado y dimensiones inválidas.

**Salida orientativa:** para ancho 4 y alto 3, el área es 12, el perímetro 14 y
`es_cuadrado()` es falso.

**Reflexión:** ¿qué solución elegirías si hubiera empate en el área mayor?

## Nivel 2 — Encapsulación y colaboración

### 5. Cuenta bancaria segura

**Objetivo:** proteger estado con una propiedad de solo lectura y hacer una
operación entre objetos de forma atómica.

Crea `CuentaBancaria` con `titular` y `_saldo`. Expón `saldo` mediante una
propiedad de lectura. Implementa `ingresar(cantidad)`, `retirar(cantidad)` y
`transferir(destino, cantidad)`.

Rechaza titulares vacíos, cantidades no positivas, retiradas sin fondos y
destinos que no sean otra cuenta válida. En una transferencia, valida destino,
cantidad y fondos de la cuenta origen **antes** de modificar ninguna cuenta.

**Caso obligatorio:** dos cuentas comienzan con 100 € y 25 €; se transfieren
30 € de la primera a la segunda y terminan con 70 € y 55 €. Prueba también una
transferencia fallida y verifica ambos saldos.

**Pruebas:** intenta asignar `cuenta.saldo = 0`; comprueba que la propiedad no
permite saltarse las reglas. Añade una prueba de ingreso y otra de retirada.

**Reflexión:** ¿por qué es peligroso exponer `_saldo` para que cualquier código
lo cambie directamente?

### 6. Biblioteca

**Objetivo:** practicar composición y reparto de responsabilidades.

Crea `Libro` con `titulo`, `autor` y estado `prestado`. Implementa en el libro
`prestar()` y `devolver()`, rechazando un doble préstamo o una devolución de un
libro disponible.

Crea `Biblioteca` con una lista **propia** de libros e implementa:

- `agregar(libro)`;
- `buscar_por_titulo(texto)`, sin distinguir mayúsculas y minúsculas;
- `disponibles()`, que devuelva los libros no prestados.

Prueba una biblioteca vacía, una búsqueda sin resultados, un préstamo correcto
y un doble préstamo. Devuelve listas nuevas cuando sea razonable para evitar
que el llamador modifique directamente la colección interna.

**Reflexión:** ¿debe ser responsabilidad de `Biblioteca` cambiar el estado
`prestado` o de cada `Libro`? Justifica tu decisión.

### 7. Equipo de jugadores

**Objetivo:** colaborar entre objetos y ordenar resultados sin efectos laterales.

Crea `Jugador` con `nombre` y `puntos`, y `Equipo` con una colección propia de
jugadores. Implementa:

- agregar jugadores sin duplicar nombres;
- `total_puntos()`;
- `mejor_jugador()`, que devuelve `None` si el equipo está vacío;
- `ranking()`, que devuelve jugadores ordenados por puntos descendentes sin
  alterar innecesariamente el orden interno.

Valida nombres no vacíos y puntos no negativos. Decide cómo resolver empates y
escribe esa regla en el README del ejercicio.

**Casos:** equipo vacío; dos jugadores con el mismo nombre; tres jugadores con
puntos 8, 15 y 10; comprobar que el ranking es 15, 10, 8 y que la colección
original conserva su orden.

**Reflexión:** ¿qué parte debe pertenecer a `Jugador` y cuál a `Equipo`?

### 8. Entradas de concierto

**Objetivo:** utilizar atributos de clase, `@classmethod` y `@staticmethod`.

Crea `EntradaConcierto` con un contador de clase `siguiente_id`. Cada instancia
recibe un identificador consecutivo y guarda concierto y precio. Implementa:

- `@staticmethod precio_valido(precio)`, que acepte números no negativos pero
  rechace booleanos;
- `@classmethod desde_texto(texto)`, que interprete
  `"Concierto;29.50"`;
- `__str__()` con identificador, concierto y precio.

Rechaza texto sin separador, concierto vacío y precios mal formados. Comprueba
que tres entradas reciben identificadores consecutivos y que una entrada
creada desde texto también participa en la secuencia.

**Reflexión:** ¿por qué `desde_texto` es un método de clase y no un método de
instancia? ¿Cuándo bastaría una función externa?

## Nivel 3 — Herencia, polimorfismo y diseño

### 9. Vehículos de alquiler

**Objetivo:** modelar herencia y sobrescritura mediante una operación común.

Crea `Vehiculo` con matrícula o identificador y un método
`coste_alquiler(dias)`. Crea `Coche`, con 35 € por día, y `Moto`, con 20 € por
día. Puedes hacer que la clase base valide el identificador y los días.

Los días deben ser enteros positivos y `bool` no debe aceptarse como entero.
Recorre una lista mixta de coches y motos calculando el coste sin usar
condiciones `if` que inspeccionen el tipo.

**Casos:** coche durante 2 días cuesta 70 €; moto durante 3 días cuesta 60 €;
0, -1, 2.5 y `True` son entradas inválidas.

**Reflexión:** explica qué método se sobrescribe y qué código común aprovecha
`super()`.

### 10. Personajes con habilidades distintas

**Objetivo:** practicar polimorfismo, estado específico de una subclase y
validación de daño.

Crea `Personaje` con nombre, vida no negativa, `esta_vivo()` y
`recibir_danio(cantidad)`. Crea `Guerrero`, cuyo `atacar()` devuelve 12, y
`Mago`, que comienza con 10 de maná. El mago consume 3 de maná y devuelve 18
por ataque mágico; si no dispone de maná suficiente, realiza un ataque básico
de 2 sin consumir maná.

Estas cifras pertenecen a este ejercicio y **no** son las del proyecto final.
La vida nunca puede bajar de 0 y el daño negativo debe rechazarse. Recorre una
lista de personajes y llama a `atacar()` sin comprobar tipos. Añade
opcionalmente `Arquero` con otra regla compatible.

**Casos:** cuatro ataques de un mago con 10 de maná producen 18, 18, 18, 2 y
dejan maná 1; un daño de 500 deja vida 0; daño negativo produce excepción.

**Reflexión:** ¿qué contrato común necesitan todas las clases para formar la
lista polimórfica?

### 11. Detectives de errores POO

**Objetivo:** diagnosticar fallos reales y explicar su causa, no solo corregir
la línea marcada. Para cada fragmento crea una prueba que falle antes de la
corrección y otra que funcione después.

**A. Método sin `self`**

```python
class Temporizador:
    def __init__(self, segundos):
        self.segundos = segundos

    def reiniciar():
        self.segundos = 0
```

**B. Atributo no guardado en la instancia**

```python
class Alumno:
    def __init__(self, nombre):
        nombre = nombre.strip()

    def presentarse(self):
        return f"Soy {self.nombre}"
```

**C. Lista mutable compartida**

```python
class Carrito:
    productos = []

    def agregar(self, producto):
        self.productos.append(producto)
```

**D. `print()` en vez de `return`**

```python
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        print(self.ancho * self.alto)
```

Corrige sin cambiar el objetivo de cada clase, identifica la excepción o el
resultado incorrecto original y explica por qué tu prueba demuestra el error.

### 12. Liga de cartas

**Objetivo:** diseñar un pequeño dominio con composición, reglas y pruebas.

Diseña `Jugador`, `Partida` y `Liga`. Una victoria da 3 puntos, un empate 1 y
una derrota 0. La liga debe impedir:

- jugar contra uno mismo;
- registrar jugadores que no pertenezcan a la liga;
- duplicar el mismo registro de partida.

La clasificación se ordena por puntos descendentes y, en empate, por nombre.
Decide cómo se representa el resultado, documenta el modelo con un diagrama de
clases y evita que `Liga` conozca detalles innecesarios de `Jugador`.

**Entrega mínima:** cuatro jugadores, tres partidas, clasificación, al menos
seis pruebas y un ejemplo de uso. Incluye un caso de empate y un intento
inválido.

**Reflexión:** ¿qué objeto debería calcular los puntos de una partida y cuál
debería acumular la clasificación?

## Reto opcional: persistencia JSON

Adapta `Biblioteca`, `Equipo` o `Liga` para guardar y cargar sus datos en JSON.
Define `to_dict()` y `from_dict()` donde sean necesarios y reconstruye
instancias al cargar: JSON no conserva clases ni métodos de Python.

Trata al menos estos casos:

- archivo inexistente;
- archivo JSON mal formado;
- dato obligatorio ausente;
- colección vacía;
- archivo válido con varios objetos.

Escribe una prueba que guarde objetos, los cargue en una colección nueva y
compruebe que los valores y tipos se han reconstruido.

## Criterios de corrección

| Criterio | Evidencia |
|---|---|
| Modelo | Clases y responsabilidades comprensibles. |
| Estado | Atributos de instancia independientes e invariantes mantenidas. |
| Métodos | Nombres claros, retornos útiles y sin efectos ocultos. |
| Validación | Errores detectados antes de modificar el objeto. |
| Diseño | Composición/herencia justificadas y sin comprobaciones de tipo innecesarias. |
| Pruebas | Casos normales, límites y errores reproducibles. |
| Comunicación | Código, comentarios y README legibles. |

Cuando termines, revisa el [proyecto final Arena de héroes](proyecto_poo.md),
que combina estas técnicas en una aplicación de consola.
