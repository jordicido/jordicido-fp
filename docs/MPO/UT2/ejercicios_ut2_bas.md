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
