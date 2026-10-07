# Ejercicios de clase UT3: Listas

## Contexto

Las listas son una de las estructuras de datos más utilizadas en Python. Permiten almacenar múltiples elementos en una sola variable y son muy versátiles. En este ejercicio, se te presentarán varios problemas que requieren el uso de listas para resolverlos. Asegúrate de entender cada problema y de implementar una solución adecuada utilizando listas.

## Ejercicio 1 - Sumar elementos de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas y calcule la suma de todos los elementos de la lista. El programa debe imprimir el resultado.

## Ejercicio 2 - Contar elementos de una lista

Escribe un programa que pida al usuario una lista de palabras separadas por comas y cuente cuántas palabras hay en la lista. El programa debe imprimir el resultado.

## Ejercicio 3 - Mayor y menor elemento de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas y encuentre el mayor y el menor elemento de la lista. El programa debe imprimir ambos resultados.

## Ejercicio 4 - Sumar dos listas de igual longitud

Escribe un programa que pida al usuario dos listas de números enteros separados por comas y sume los elementos de ambas listas. El programa debe imprimir la lista resultante. Si las listas no tienen la misma longitud, el programa debe imprimir un mensaje de error.

## Ejercicio 5 - Invertir una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas y la invierta. El programa debe imprimir la lista invertida.

## Ejercicio 6 - Dias de la semana

Escribe un programa que reciba números hasta la introducción de un 0. Por cada número, suponiendo que el 1 representa el lunes, el 2 el martes, etc., imprime el nombre del día correspondiente.

Ejemplo:

```text
Ingrese un número (0 para salir): 1
Lunes
Ingrese un número (0 para salir): 3
Miércoles
Ingrese un número (0 para salir): 8
Lunes
Ingrese un número (0 para salir): 0
```

## Ejercicio 7 - Crear una matriz de ceros

Escribe un programa que pida al usuario el número de filas y columnas de una matriz. El programa debe crear una lista de dos dimensiones con esas medidas, inicializada con ceros, y mostrarla por pantalla.

Ejemplo:

```text
Ingrese el número de filas: 3
Ingrese el número de columnas: 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

## Ejercicio 8 - Sumar todos los elementos de una matriz

Escribe un programa que tenga una matriz de números enteros definida en el código y calcule la suma de todos sus elementos. El programa debe imprimir el resultado final.

Ejemplo de matriz:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## Ejercicio 9 - Sumar cada fila de una matriz

Escribe un programa que tenga una matriz de números enteros definida en el código y calcule la suma de cada una de sus filas. El programa debe imprimir la suma de cada fila indicando su número.

Ejemplo:

```text
Fila 0: 6
Fila 1: 15
Fila 2: 24
```

## Ejercicio 10 - Buscar un valor en una matriz

Escribe un programa que tenga una matriz de números enteros definida en el código y pida al usuario un número. El programa debe buscar el número dentro de la matriz e indicar si se ha encontrado. Si aparece, debe mostrar también la fila y la columna donde se encuentra.

Ejemplo:

```text
Ingrese un número: 8
El número 8 está en la fila 2, columna 1.
```

## Ejercicio 11 - Modificar un elemento de una matriz

Escribe un programa que tenga una matriz de números enteros definida en el código. El programa debe pedir al usuario una fila, una columna y un nuevo valor. Después, debe modificar el elemento correspondiente de la matriz y mostrar la matriz actualizada.

Ejemplo:

```text
Ingrese la fila: 1
Ingrese la columna: 2
Ingrese el nuevo valor: 99
[[1, 2, 3], [4, 5, 99], [7, 8, 9]]
```

## Ejercicio 12 - Mini hundir la flota

Escribe un programa que simule una versión sencilla del juego hundir la flota. El programa debe tener un tablero de 5 filas y 5 columnas representado con una lista de dos dimensiones.

Coloca un barco en una posición fija del tablero, por ejemplo en la fila 2 y columna 3. Después, pide al usuario una fila y una columna. Si acierta la posición del barco, el programa debe mostrar `Tocado`. Si no acierta, debe mostrar `Agua`.

Ejemplo:

```text
Ingrese una fila: 2
Ingrese una columna: 3
Tocado
```

Puedes representar el tablero usando:

- `"~"` para el agua.
- `"B"` para el barco.
- `"X"` para un disparo acertado.
- `"O"` para un disparo fallado.

## Ejercicio 13 - Buscador de tesoros

Escribe un programa que tenga un mapa de 4 filas y 4 columnas representado con una lista de dos dimensiones. En una de las posiciones debe haber un tesoro oculto, representado con la letra `"T"`.

El usuario debe introducir una fila y una columna para intentar encontrar el tesoro. Si acierta, el programa debe mostrar `Has encontrado el tesoro`. Si falla, debe indicar si el tesoro está en una fila mayor, una fila menor, una columna mayor o una columna menor.

Ejemplo:

```text
Ingrese una fila: 1
Ingrese una columna: 1
El tesoro está en una fila mayor.
El tesoro está en una columna mayor.
```

El objetivo es practicar el acceso a posiciones concretas de una lista de dos dimensiones y el uso de condiciones.
