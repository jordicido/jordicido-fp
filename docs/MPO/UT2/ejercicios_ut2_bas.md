# Ejercicios UT2: Nivel básico

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

    ```plaintext
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

    ```plaintext
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

    ```plaintext
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
