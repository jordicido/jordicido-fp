# Ejercicios UT1 - Nivel básico

## Ejercicio 1

Escribe un programa en Python que pida al usuario su nombre y edad, y luego imprima un mensaje de bienvenida customizado indicando ambos datos.

??? summary "Solución"
    ```python
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    print("Hola, " + nombre + "! Tienes " + edad + " años.")
    ```

Sabías que hay una forma más sencilla de concatenar cadenas en Python? Puedes usar la función `f-string` para formatear cadenas de manera más legible.

Intenta buscar como usar `f-string` y modifica el código anterior para usarlo.

??? warning "Explicación"
    ```python
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    print(f"Hola, {nombre}! Tienes {edad} años.")
    ```

No te parece mucho más senzillo?

## Ejercicio 2

Escribe un programa en Python que pida al usuario dos números y luego imprima la suma, resta, multiplicación y división de ambos números.

??? summary "Solución"
    ```python
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
    ```

En este ejercicio, hemos utilizado la función `float()` para convertir la entrada del usuario en un número decimal. Esto nos permite realizar operaciones matemáticas con los números ingresados. Es importante recordar que la división en Python puede dar como resultado un número decimal, por lo que es recomendable usar `float()` para evitar errores de tipo.

## Ejercicio 3

Escribe un programa que, dados dos números enteros, imprima True si son iguales y False si no lo son.

??? summary "Solución"
    ```python
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    print(num1 == num2)
    ```

Fíjate que en este ejercicio hemos utilizado la función `int()` para convertir la entrada del usuario en un número entero. Esto es importante porque queremos comparar dos números enteros, no cadenas de texto. La comparación se realiza utilizando el operador `==`, que devuelve `True` si los números son iguales y `False` si no lo son.

## Ejercicio 4

Escribe un programa que pida al usuario dos números enteros e imprima True si el primero es divisible por el segundo.

??? summary "Solución"
    ```python
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    print(num1 % num2 == 0)
    ```

En este ejercicio, hemos utilizado el operador `%` para calcular el resto de la división entre los dos números. Si el resto es cero, significa que el primer número es divisible por el segundo. La comparación se realiza utilizando el operador `==`, que devuelve `True` si el resto es cero y `False` si no lo es.

Por si no lo sabías, el operador `%` se llama "módulo" y se utiliza para obtener el resto de una división. Por ejemplo, `10 % 3` devuelve `1`, porque al dividir `10` entre `3`, el resto es `1`. Si el primer número es divisible por el segundo, el resultado del módulo será `0`.

## Ejercicio 5

Nunca me ha gustado que Python no disponga de una manera rápida de aumentar un contador. Haz un programa que pida al usuario un número entero e imprima el siguiente número.

??? summary "Solución"
    ```python
    num = int(input("Introduce un número entero: "))
    num = num + 1
    print(f"El siguiente número es: {num}")
    ```

En este ejercicio, hemos utilizado el operador `+` para sumar `1` al número ingresado por el usuario. Esto nos permite obtener el siguiente número entero de manera sencilla. Sin embargo, hay una forma más corta de hacerlo utilizando el operador `+=`, que es un operador de asignación. Este operador permite aumentar el valor de una variable en una cantidad específica. Cómo quedaría el código si utilizamos `+=`?

??? warning "Explicación"
    ```python
    num = int(input("Introduce un número entero: "))
    num += 1
    print(f"El siguiente número es: {num}")
    ```

    En este caso, `num += 1` es equivalente a `num = num + 1`, pero es más conciso y fácil de leer. Este tipo de operadores de asignación son muy útiles para simplificar el código y hacerlo más legible.

## Ejercicio 6

Escribe un programa que pida al usuario un número entero e imprima:

- Su doble
- Su triple
- Su mitad
- Su cuadrado
- Su raíz cuadrada

??? summary "Solución"
    ```python
    import math

    num = int(input("Introduce un número entero: "))

    doble = num * 2
    triple = num * 3
    mitad = num / 2
    cuadrado = num ** 2
    raiz_cuadrada = math.sqrt(num)

    print(f"Doble: {doble}")
    print(f"Triple: {triple}")
    print(f"Mitad: {mitad}")
    print(f"Cuadrado: {cuadrado}")
    print(f"Raíz cuadrada: {raiz_cuadrada}")
    ```

En este ejercicio, hemos utilizado la función `math.sqrt()` para calcular la raíz cuadrada del número ingresado. La función `math.sqrt()` es parte del módulo `math`, que proporciona funciones matemáticas adicionales. Asegúrate de importar el módulo `math` al principio de tu programa para poder utilizar esta función.

## Ejercicio 7

Escribe un programa que pida al usuario tres números enteros e imprima True si todos ellos son mayores que cero, False en caso contrario.

??? summary "Solución"
    ```python
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))

    print(num1 > 0 and num2 > 0 and num3 > 0)
    ```

## Ejercicio 8

Escribe un programa que pida al usuario tres nombres e immprima True si alguno de los nombres es "Juan", False en caso contrario.

??? summary "Solución"
    ```python
    nombre1 = input("Introduce el primer nombre: ")
    nombre2 = input("Introduce el segundo nombre: ")
    nombre3 = input("Introduce el tercer nombre: ")

    print(nombre1 == "Juan" or nombre2 == "Juan" or nombre3 == "Juan")
    ```

## Ejercicio 9

Escribe un programa que pida al usuario un número entero e imprima True si éste es mayor o igual que 18 y menor que 65, False en caso contrario.

??? summary "Solución"
    ```python
    num = int(input("Introduce un número entero: "))

    print(num > 18 and num < 65)
    ```

## Ejercicio 10

Escribe un programa que, dados dos números enteros, imprima su división decimal, si división entera y su resto. El segundo número no puede ser cero.

??? summary "Solución"
    ```python
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    division_decimal = num1 / num2
    division_entera = num1 // num2
    resto = num1 % num2

    print(f"División decimal: {division_decimal}")
    print(f"División entera: {division_entera}")
    print(f"Resto: {resto}")
    ```

En este ejercicio, hemos utilizado el operador `//` para realizar la división entera. La división entera devuelve el cociente sin decimales.
