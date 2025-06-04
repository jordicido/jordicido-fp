# Ejercicios UT2: Extras

## Ejercicio 1 - Contar la frecuencia de un número en una lista

Escribe un programa que pida al usuario una lista de números enteros separados por espacios y un número entero. El programa debe contar cuántas veces aparece el número en la lista y luego imprimir el resultado.

??? Summary "Solución"
    ```python
    numeros = input("Ingrese una lista de números enteros separados por espacios: ").split()
    numeros = [int(num) for num in numeros]
    numero_a_contar = int(input("Ingrese un número entero: "))
    frecuencia = numeros.count(numero_a_contar)
    print(f"El número {numero_a_contar} aparece {frecuencia} veces en la lista.")
    ```

!!! warning "Explicación"
    Cuando usas el método `split()` sin argumentos, separa la cadena en por espacios. Igualmente, podemos usar `split(" ")` para separar la cadena en por espacios.

!!! warning "Explicación"
    El método `count()` cuenta cuántas veces aparece un elemento en una lista. En este caso, cuenta cuántas veces aparece el número ingresado por el usuario.

## Ejercicio 2 - Multiplicar todos los elementos de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por espacios y un número entero. El programa debe multiplicar todos los elementos de la lista por el número dado y luego imprimir la lista resultante.

??? Summary "Solución"
    ```python
    numeros = input("Ingrese una lista de números enteros separados por espacios: ").split()
    numeros = [int(num) for num in numeros]
    numero_a_multiplicar = int(input("Ingrese un número entero: "))
    for i in range(len(numeros)):
        numeros[i] *= numero_a_multiplicar
    print("Lista resultante:", numeros_multiplicados)
    ```

!!! warning "Explicación"
    La forma [int(num) for num in numeros] convierte cada elemento de la lista de cadenas a enteros. Esto es necesario porque el método `split()` devuelve una lista de cadenas.

## Ejercicio 3 - Filtrar elementos de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas y filtre los números pares de la lista. El programa debe imprimir la lista de números pares.

??? Summary "Solución"
    ```python
    numeros = input("Ingrese una lista de números enteros separados por comas: ").split(",")
    numeros = [int(num) for num in numeros]
    numeros_pares = []
    for num in numeros:
        if num % 2 == 0:
            numeros_pares.append(num)
    print("Lista de números pares:", numeros_pares)
    ```

## Ejercicio 4 - Sumar dos listas de diferente longitud

Escribe un programa que pida al usuario dos listas de números enteros separados por comas y sume los elementos de ambas listas. Si las listas no tienen la misma longitud, el programa debe sumar los elementos de la lista más corta con los elementos correspondientes de la lista más larga y el resto de los elementos de la lista más larga deben ser sumados a cero. El programa debe imprimir la lista resultante.

??? Summary "Solución"
    ```python
    lista1 = input("Ingrese la primera lista de números enteros separados por comas: ").split(",")
    lista2 = input("Ingrese la segunda lista de números enteros separados por comas: ").split(",")
    lista1 = [int(num) for num in lista1]
    lista2 = [int(num) for num in lista2]
    longitud_maxima = max(len(lista1), len(lista2))
    suma_listas = []

    for i in range(longitud_maxima):
        num1 = lista1[i] if i < len(lista1) else 0
        num2 = lista2[i] if i < len(lista2) else 0
        suma_listas.append(num1 + num2)
    
    print("Lista resultante:", suma_listas)
    ``` 

## Ejercicio 5 - Eliminar todos los elementos de una lista que sean mayores a un número dado

Escribe un programa que pida al usuario una lista de números enteros separados por comas y un número entero. El programa debe eliminar todos los elementos de la lista que sean mayores al número dado y luego imprimir la lista resultante.

??? Summary "Solución"
    ```python
    numeros = input("Ingrese una lista de números enteros separados por comas: ").split(",")
    numeros = [int(num) for num in numeros]
    numero_a_eliminar = int(input("Ingrese un número entero: "))
    numeros_filtrados = []
    for num in numeros:
        if num <= numero_a_eliminar:
            numeros_filtrados.append(num)
    print("Lista resultante:", numeros_filtrados)
    ```

## Ejercicio 6 - Encontrar el segundo valor más grande en una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas. El programa debe encontrar el segundo valor más grande en la lista y luego imprimirlo. Si no hay un segundo valor más grande, el programa debe imprimir un mensaje indicando que no se encontró. Se asegura que la lista no contiene duplicados.

??? Summary "Solución"
    ```python
    numeros = input("Ingrese una lista de números enteros separados por comas: ").split(",")
    numeros = [int(num) for num in numeros]
    numeros.sort()

    if len(numeros) < 2:
        print("No se encontró un segundo valor más grande.")
    else:
        segundo_mayor = numeros[-2]
        print("El segundo valor más grande es:", segundo_mayor)
    ```

## Ejercicio 7 - Eliminar elementos duplicados consecutivos de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas. El programa debe eliminar los elementos duplicados consecutivos de la lista y luego imprimir la lista resultante.

Ejemplo:

```
Entrada: 1, 2, 2, 3, 3, 3, 4
Salida: 1, 2, 3, 4
```

??? Summary "Solución"
    ```python
    numeros = input("Ingrese una lista de números enteros separados por comas: ").split(",")
    numeros = [int(num) for num in numeros]
    numeros_filtrados = []

    for i in range(len(numeros)):
        if i == 0 or numeros[i] != numeros[i - 1]:
            numeros_filtrados.append(numeros[i])
    
    print("Lista resultante:", numeros_filtrados)
    ```

## Ejercicio 8 - Eliminar elementos duplicados de una lista

Escribe un programa que pida al usuario una lista de números enteros separados por comas. El programa debe eliminar los elementos duplicados de la lista y luego imprimir la lista resultante.

Ejemplo:

```
Entrada: 1, 2, 2, 3, 3, 3, 4, 3, 4, 1
Salida: 1, 2, 3, 4
```

??? Summary "Solución"
    ```python
    numeros = input("Ingrese una lista de números enteros separados por comas: ").split(",")
    numeros = [int(num) for num in numeros]
    numeros_unicos = []

    for num in numeros:
        if num not in numeros_unicos:
            numeros_unicos.append(num)
    print("Lista resultante:", numeros_unicos)
    ```
