# Ejercicios UT2: Extras

## Ejercicio 1

Escribe un programa que pida al usuario un número entero y determine si es par o impar. El programa debe imprimir un mensaje indicando el resultado.

??? Summary "Solución"
    ```python
    numero = int(input("Introduce un número entero: "))
    if numero % 2 == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")
    ```

## Ejercicio 2

Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero. El programa debe imprimir un mensaje indicando el resultado.

??? Summary "Solución"
    ```python
    numero = int(input("Introduce un número entero: "))
    if numero > 0:
        print(f"{numero} es positivo.")
    elif numero < 0:
        print(f"{numero} es negativo.")
    else:
        print("El número es cero.")
    ```

## Ejercicio 3

Escribe un programa que pida al usuario un número entero y determine si es divisible por 3 y 5. El programa debe imprimir un mensaje indicando el resultado.

??? Summary "Solución"
    ```python
    numero = int(input("Introduce un número entero: "))
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"{numero} es divisible por 3 y 5.")
    else:
        print(f"{numero} no es divisible por 3 y 5.")
    ```

## Ejercicio 4

Escribe un programa que pida una nota (0-10) y muestre:

- "Suspenso" si es menor de 5
- "Aprobado" si es entre 5 y 6
- "Notable" si es entre 7 y 8
- "Sobresaliente" si es 9 o 10

??? Summary "Solución"
    ```python
    nota = float(input("Introduce una nota (0-10): "))
    if nota < 5:
        print("Suspenso")
    elif 5 <= nota < 7:
        print("Aprobado")
    elif 7 <= nota < 9:
        print("Notable")
    elif 9 <= nota <= 10:
        print("Sobresaliente")
    else:
        print("Nota no válida.")
    ```

## Ejercicio 5

Escribe un programa que pida el nombre de un día de la semana y muestre si es "laborable" o "fin de semana".

??? Summary "Solución"
    ```python
    dia = input("Introduce el nombre de un día de la semana: ").lower()
    if dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
        print(f"{dia.capitalize()} es un día laborable.")
    elif dia in ["sábado", "domingo"]:
        print(f"{dia.capitalize()} es fin de semana.")
    else:
        print("Día no válido.")
    ```

## Ejercicio 6

Escribe un porgrama que pida un año y muestra si es bisiesto. Un año es bisiesto si es divisible por 4, pero no por 100, o si es divisible por 400.

??? Summary "Solución"
    ```python
    año = int(input("Introduce un año: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"{año} es un año bisiesto.")
    else:
        print(f"{año} no es un año bisiesto.")
    ```

## Ejercicio 7

Escribe un programa que pida dos números y un operador (+, -, *, /) y muestre el resultado de la operación.

??? Summary "Solución"
    ```python
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operador = input("Introduce un operador (+, -, *, /): ")

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: División por cero."
    else:
        resultado = "Operador no válido."

    print(f"Resultado: {resultado}")
    ```

## Ejercicio 8

Escribe un programa que pida el nombre de un mes y muestre cuántos días tiene (puedes simplificar febrero a 28 días siempre).

??? Summary "Solución"
    ```python
    mes = input("Introduce el nombre de un mes: ").lower()
    if mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]:
        dias = 31
    elif mes in ["abril", "junio", "septiembre", "noviembre"]:
        dias = 30
    elif mes == "febrero":
        dias = 28
    else:
        dias = "Mes no válido."

    print(f"{mes.capitalize()} tiene {dias} días.")
    ```

La función lower() convierte la cadena a minúsculas para evitar problemas de mayúsculas y minúsculas al comparar el mes ingresado por el usuario. Puedes usar upper() si prefieres trabajar con mayúsculas.

## Ejercicio 9

Escribe un programa que pida el precio de un producto y, si supera los 100€, aplique un descuento del 10%. Muestra el precio final.

??? Summary "Solución"
    ```python
    precio = float(input("Introduce el precio del producto: "))
    if precio > 100:
        descuento = precio * 0.10
        precio_final = precio - descuento
    else:
        precio_final = precio

    print(f"El precio final es: {precio_final}€")
    ```

## Ejercicio 10

Escribe un programa que pida día, mes y año. Comprueba si la fecha introducida es válida. Recuerda que, en los años bisiestos, febrero tiene 29 días. Puedes usar el algoritmo del ejercicio 6 para determinar si un año es bisiesto.

??? Summary "Solución"
    ```python
    dia = int(input("Introduce el día: "))
    mes = int(input("Introduce el mes (1-12): "))
    año = int(input("Introduce el año: "))

    if mes < 1 or mes > 12:
        print("Mes no válido.")
    elif dia < 1 or (mes == 2 and ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0) and dia > 29)) or (mes == 2 and dia > 28) or (mes in [4, 6, 9, 11] and dia > 30) or (mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31):
        print("Fecha no válida.")
    else:
        print(f"La fecha {dia}/{mes}/{año} es válida.")
    ```

??? warning "Recuerda"
    Recuerda que este ejercicio es un poco más complicado porque tienes que tener en cuenta los días de cada mes y los años bisiestos. No solo tienes que comprobar si el mes es válido, sino también si el día es válido para ese mes y año. Por ejemplo, febrero tiene 29 días en años bisiestos y 28 en años no bisiestos. Además, abril, junio, septiembre y noviembre tienen 30 días, mientras que enero, marzo, mayo, julio, agosto, octubre y diciembre tienen 31 días.

## Ejercicio 11

Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente. El primer número siempre será menor que el segundo.

**Ejemplo:**

El usuario introduce 2 y 5.

El programa debe imprimir:

```plain
2
3
4
5
```

??? Summary "Solución"
    ```python
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    for i in range(num1, num2 + 1):
        print(i)
    ```

??? warning "Recuerda"
    Recuerda que el rango en Python es exclusivo en el límite superior, por lo que debes sumar 1 al segundo número para incluirlo en la secuencia.

## Ejercicio 12

Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente. Si el primer número es mayor que el segundo, imprime la secuencia en orden descendente. Debes imprimir la secuencia de números en una sola línea, separados por espacios.

**Ejemplo:**

El usuario introduce 5 y 2.

El programa debe imprimir:

```plain
5 4 3 2
```

??? Summary "Solución"
    ```python
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    if num1 < num2:
        for i in range(num1, num2 + 1):
            print(i, end=" ")
    else:
        for i in range(num1, num2 - 1, -1):
            print(i, end=" ")
    ```

??? warning "Recuerda"
    RAdemás, el argumento `end=" "` en la función `print()` se utiliza para imprimir los números en la misma línea, separados por espacios. Si no se especifica, `print()` por defecto añade un salto de línea al final de cada impresión. Por lo tanto, al usar `end=" "`, estamos indicando que queremos que el siguiente número se imprima en la misma línea, separado por un espacio.

## Ejercicio 13

Escribe un programa que pida al usuario un número entero positivo e imprima la tabla de multiplicar de ese número (del 1 al 10).

??? Summary "Solución"
    ```python
    numero = int(input("Introduce un número entero positivo: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    ```

## Ejercicio 14

Escribe un programa que pida al usuario un número entero positivo e imprima la suma de los números pares por un lado y la suma de los números impares por otro. El programa debe imprimir ambos resultados.

??? Summary "Solución"
    ```python
    numero = int(input("Introduce un número entero positivo: "))
    suma_pares = 0
    suma_impares = 0

    for i in range(1, numero + 1):
        if i % 2 == 0:
            suma_pares += i
        else:
            suma_impares += i

    print(f"Suma de números pares: {suma_pares}")
    print(f"Suma de números impares: {suma_impares}")
    ```

## Ejercicio 15

Escribe un programa que pida al usuario un número entero positivo y calcules la suma de la potencia de 3 de cada número desde 1 hasta el número introducido. El programa debe imprimir el resultado.

Para que se entienda mejor, si el usuario introduce 3, el programa debe calcular:

```plain
1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
```

??? Summary "Solución"
    ```python
    numero = int(input("Introduce un número entero positivo: "))
    suma = 0

    for i in range(1, numero + 1):
        suma += i ** 3

    print(f"La suma de la potencia de 3 de los números desde 1 hasta {numero} es: {suma}")
    ```

## Ejercicio 16

Escribe un programa que pida al usuario un número entero positivo e imprima la lista de divisores de ese número. Un divisor de un número `n` es un número entero que divide a `n` sin dejar residuo. El programa debe imprimir todos los divisores del número introducido.

??? Summary "Solución"
    ```python
    numero = int(input("Introduce un número entero positivo: "))

    print(f"Los divisores de {numero} son: ", end=" ")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i, end=" ")
    print()
    ```

??? warning "¿Por qué ponemos ese último print()?"
    El último `print()` se utiliza para añadir un salto de línea después de imprimir todos los divisores, para que la salida sea más legible. Sin él, el cursor quedaría al final de la lista de divisores en la misma línea.

## Ejercicio 17

Escribe un programa que reciba un número entero positivo y una letra. El programa debe imprimir la letra tantas veces como el número introducido.

??? Summary "Solución"
    ```python
    numero = int(input("Introduce un número entero positivo: "))
    letra = input("Introduce una letra: ")

    for i in range(numero):
        print(letra, end="")
    print()
    ```

## Ejercicio 18

Escribe un programa que dado una serie de números introducidos por el usuario, hasta que introduzca un -1, imprima el número introducido sumándole 1. El programa debe imprimir todos los números introducidos, menos el -1, sumándoles 1.

```plain
Entrada:
1
2
3
-1

Salida:
2
3
4
```

??? Summary "Solución"
    ```python
    while True:
        numero = int(input("Introduce un número (-1 para salir): "))
        if numero == -1:
            break
        print(numero + 1)
    ```

## Ejercicio 19

Escribe un programa que dado una serie de notas introducidas por el usuario, hasta que introduzca un -1, imprima el número de notas correctas introducidas, la media de las notas y cuantas de estas notas son 10. El programa debe imprimir la media de todas las notas introducidas, menos el -1.

!!! tip
    Una nota es correcta si está entre 0 y 10, ambos incluidos. Si el usuario introduce una nota fuera de este rango, el programa no la tendrá en cuenta para calcular la media ni el número de notas correctas.

```plain
Entrada:
1
6
10
11
8
-1

Salida:
Número de notas correctas: 4
Media de notas: 6.25
Número de dieces: 1
```

??? Summary "Solución"
    ```python
    suma_notas = 0
    contador_notas = 0
    contador_diez = 0

    while True:
        nota = float(input("Introduce una nota (-1 para salir): "))
        if nota == -1:
            break
        if 0 <= nota <= 10:
            suma_notas += nota
            contador_notas += 1
            if nota == 10:
                contador_diez += 1

    if contador_notas > 0:
        media = suma_notas / contador_notas
        print(f"Número de notas correctas: {contador_notas}")
        print(f"Media de notas: {media:.2f}")
        print(f"Número de dieces: {contador_diez}")
    else:
        print("No se introdujeron notas válidas.")
    ```

## Ejercicio 20

Escribe un programa que dado una serie de números introducidos por el usuario, hasta que introduzca un -1, cuente cuántos de estos números son pares y cuántos son impares. El programa debe imprimir el número de pares e impares introducidos, menos el -1.

??? Summary "Solución"
    ```python
    contador_pares = 0
    contador_impares = 0

    while True:
        numero = int(input("Introduce un número (-1 para salir): "))
        if numero == -1:
            break
        if numero % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1

    print(f"Número de pares: {contador_pares}")
    print(f"Número de impares: {contador_impares}")
    ```

!!! tip
    Vigilad con el uso de `while True:`. Este bucle se ejecutará indefinidamente hasta que se encuentre una instrucción `break` dentro de él. Asegúrate de que haya una condición que permita salir del bucle, como en este caso, cuando el usuario introduce -1. Además, es importante para la legibilidad del código, no abusar de este tipo de bucles y utilizar estructuras de control más específicas cuando sea posible.
    En este caso, el uso de `while True:` es adecuado porque estamos esperando una entrada del usuario que puede ser indefinida. Sin embargo, en otros casos, podrías considerar usar un bucle `for` o un bucle `while` con una condición más específica.

## Ejercicio 21

Escribe un programa que te introduzca un número entero positivo que corresponde al número de casos a tratar. Seguidamente te introducen un número entero positivo que corresponde a una serie de números. Después debes recibir ese total de números e imprimirlos en la misma linea de la terminal, separados por un espacio y habiéndoles sumado 1 a cada uno de ellos.

```plain
Entrada:
3
4
5 0 99 2
1
45
2 
-1 -3

Salida:
5 1 100 3
46
0 -2
```

??? Summary "Solución"
    ```python
    casos = int(input("Introduce el número de casos: "))
    for _ in range(casos):
        numeros = int(input("Cuántos números vas a introducir? "))
        for _ in range(numeros):
            numero = int(input())
            print(int(numero) + 1, end=" ")
        print()
    ```

??? tip
    En este caso, el uso de `for _ in range(casos):` es adecuado porque estamos iterando un número fijo de veces, que es el número de casos introducido por el usuario. El guion bajo (`_`) se utiliza como una convención para indicar que la variable de iteración no se va a utilizar dentro del bucle. Esto es útil para mejorar la legibilidad del código y evitar advertencias de variables no utilizadas.
    En el segundo bucle, `for _ in range(numeros):`, también se utiliza el guion bajo porque no necesitamos el valor de la variable de iteración, solo queremos repetir el bloque de código un número específico de veces.

## Ejercicio 22

Escribe un programa que inicialmente te indique el número de casos a tratar. Después, para cada caso, te introduzca un número entero positivo del qual debes imprimir todos los divisores. Un divisor de un número `n` es un número entero que divide a `n` sin dejar residuo. El programa debe imprimir todos los divisores del número introducido en una sola línea, separados por espacios.

```plain
Entrada:
3
4
2
10

Salida:
1 2 4
1 2
1 2 5 10
```

??? Summary "Solución"
    ```python
    casos = int(input("Introduce el número de casos: "))
    for _ in range(casos):
        numero = int(input("Introduce un número entero positivo: "))
        print(f"Los divisores de {numero} son: ", end=" ")
        for i in range(1, numero + 1):
            if numero % i == 0:
                print(i, end=" ")
        print()
    ```

## Ejercicio 23

Escribe un programa que vaya recibiendo cadenas de texto hasta que el usuario introduzca "fin". El programa debe contar cuántas vocales se han introducido e imprimir el resultado. Las vocales son: a, e, i, o, u (tanto mayúsculas como minúsculas). El programa debe imprimir el número total de vocales introducidas sin contar la palabra "fin".

```plain
Entrada:
Hola
como estan los maquinas
fin

Salida:
Número total de vocales: 11
```

??? Summary "Solución"
    ```python
    contador_vocales = 0

    while True:
        cadena = input("Introduce una cadena de texto (o 'fin' para salir): ")
        if cadena.lower() == "fin":
            break
        for letra in cadena:
            if letra.lower() in "aeiou":
                contador_vocales += 1

    print(f"Número total de vocales: {contador_vocales}")
    ```

??? tip
    Analiza el condicional que hemos utilizado para comprobar si la letra es una vocal. En este caso, hemos utilizado `letra.lower() in "aeiou"` para comprobar si la letra en minúscula está en la cadena de vocales. Esto nos permite contar tanto las vocales mayúsculas como las minúsculas sin necesidad de duplicar el código. En lenguaje natural estaría así: "Si la letra en minúscula está en la cadena de vocales, entonces es una vocal". Esto es una forma eficiente de comprobar si una letra es una vocal sin necesidad de utilizar múltiples condicionales.

??? tip
    El bucle `for letra in cadena:` itera sobre cada letra de la cadena introducida por el usuario. En cada iteración, se comprueba si la letra es una vocal y, si lo es, se incrementa el contador de vocales. Al final del programa, se imprime el total de vocales encontradas. Este tipo de for se le llama "for-each" porque itera sobre cada elemento de una colección (en este caso, la cadena de texto).

## Ejercicio 24

Escribe un programa que reciba un número `n` entero positivo y que escriba esta secuencia de números: un uno, dos doses, tres treses... hasta `n` enes. Por ejemplo, si el usuario introduce 5, el programa debe imprimir:

```plain
122333444455555
```

??? Summary "Solución"
    ```python
    n = int(input("Introduce un número entero positivo: "))
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="")
    print()
    ```
