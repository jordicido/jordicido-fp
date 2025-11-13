# UT7: Conectividad y Datos

## Introducción

En esta unidad, exploraremos cómo Python puede interactuar con servicios web y manejar datos en formatos comunes como JSON y CSV. Aprenderemos a utilizar módulos estándar para realizar solicitudes HTTP, así como a leer y escribir datos en estos formatos. Estos conocimientos son esenciales para trabajar con APIs y manejar datos en aplicaciones del mundo real.

Las solicitudes HTTP son fundamentales para la comunicación entre clientes y servidores en la web. Python ofrece varias bibliotecas para realizar estas solicitudes de manera sencilla. Los diferentes métodos HTTP que utilizaremos incluyen:

- **GET**: Se utiliza para solicitar datos de un servidor.
- **POST**: Se utiliza para enviar datos a un servidor.
- **PUT**: Se utiliza para actualizar datos existentes en un servidor.
- **DELETE**: Se utiliza para eliminar datos en un servidor.

La información intercambiada a través de estas solicitudes a menudo se encuentra en formatos estructurados como JSON (JavaScript Object Notation) y CSV (Comma-Separated Values). Estos formatos son ampliamente utilizados debido a su simplicidad y facilidad de uso.

## Conectividad HTTP con el módulo `requests`

El módulo `requests` es una biblioteca popular en Python para realizar solicitudes HTTP de manera sencilla. Nos permite enviar solicitudes GET, POST, y otras, así como manejar respuestas de manera eficiente.

### Instalación del módulo `requests`

Para utilizar el módulo `requests`, primero debemos instalarlo. Podemos hacerlo utilizando pip:

```bash
pip install requests
```

### Realizar una solicitud GET

Las solicitudes GET se utilizan para obtener datos de un servidor. Aquí hay un ejemplo básico de cómo realizar una solicitud GET utilizando el módulo `requests`:

```python
import requests

response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
``` 

Cuando un servidor responde a una solicitud GET, podemos verificar el código de estado para asegurarnos de que la solicitud fue exitosa (código 200) y luego procesar los datos recibidos.

La próxima sección cubrirá cómo manejar datos en formatos JSON y CSV.

### Realizar una solicitud POST

Las solicitudes POST se utilizan para enviar datos a un servidor. Aquí hay un ejemplo básico de cómo realizar una solicitud POST utilizando el módulo `requests`:

```python
import requests

data = {
    'key1': 'value1',
    'key2': 'value2'
}
response = requests.post('https://api.example.com/data', json=data)
if response.status_code == 201:
    print("Datos enviados exitosamente.")
else:
    print(f"Error: {response.status_code}")
```

En este ejemplo, enviamos un diccionario como datos JSON al servidor. Al igual que con las solicitudes GET, verificamos el código de estado para asegurarnos de que la solicitud fue exitosa (código 201 para creación).

### Realizar una solicitud PUT

Las solicitudes PUT se utilizan para actualizar datos existentes en un servidor. Aquí hay un ejemplo básico de cómo realizar una solicitud PUT utilizando el módulo `requests`:

```python
import requests

data = {
    'key1': 'new_value1',
    'key2': 'new_value2'
}
response = requests.put('https://api.example.com/data/1', json=data)
if response.status_code == 200:
    print("Datos actualizados exitosamente.")
else:
    print(f"Error: {response.status_code}")
```

En este ejemplo, enviamos un diccionario como datos JSON para actualizar un recurso específico en el servidor. Verificamos el código de estado para asegurarnos de que la solicitud fue exitosa (código 200).

### Realizar una solicitud DELETE

Las solicitudes DELETE se utilizan para eliminar datos en un servidor. Aquí hay un ejemplo básico de cómo realizar una solicitud DELETE utilizando el módulo `requests`:

```python
import requests

response = requests.delete('https://api.example.com/data/1')
if response.status_code == 204:
    print("Datos eliminados exitosamente.")
else:
    print(f"Error: {response.status_code}")
```

En este ejemplo, realizamos una solicitud DELETE para eliminar un recurso específico en el servidor. Verificamos el código de estado para asegurarnos de que la solicitud fue exitosa (código 204 para eliminación).

### Respuestas de las solicitudes HTTP

Cuando realizamos una solicitud HTTP, el servidor responde con un objeto de respuesta que contiene varios atributos útiles. Algunos de los atributos más comunes incluyen:

- `status_code`: El código de estado HTTP de la respuesta (por ejemplo, 200, 404, 500).
- `headers`: Un diccionario que contiene los encabezados de la respuesta.
- `text`: El contenido de la respuesta como una cadena de texto.
- `json()`: Un método que convierte el contenido de la respuesta en un objeto JSON (si el contenido es JSON).

Se pueden consultar los diferentes estados HTTP en el siguiente enlace: [Códigos de estado HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Status).

## Ejemplo práctico: Consumo de una API pública

En este ejemplo, consumiremos una API pública que proporciona información sobre países. Utilizaremos el módulo `requests` para realizar una solicitud GET y obtener datos en formato JSON.

Vamos a usar la PokeAPI, que es una API pública que proporciona información sobre Pokémon.

```python
import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
if response.status_code == 200:
    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"Altura: {data['height']}")
    print(f"Peso: {data['weight']}")
else:
    print(f"Error: {response.status_code}")
```

## Manejo de datos en formato JSON

El formato JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos que es fácil de leer y escribir tanto para humanos como para máquinas. En Python, podemos trabajar con datos JSON utilizando el módulo `json`, que nos permite convertir entre objetos Python y cadenas JSON.

### Ejemplo de uso del módulo `json`

```python
import json

# Convertir un objeto Python a una cadena JSON
data = {
    'key1': 'value1',
    'key2': 'value2'
}
json_string = json.dumps(data)
print(json_string)

# Convertir una cadena JSON a un objeto Python
data = json.loads(json_string)
print(data)
```

Los objetos json se componen de pares clave-valor y pueden incluir listas y otros objetos JSON anidados. El módulo `json` facilita la serialización y deserialización de estos datos en Python.

## Manejo de datos en formato CSV

El formato CSV (Comma-Separated Values) es un formato común para almacenar datos tabulares en texto plano. En Python, podemos trabajar con archivos CSV utilizando el módulo `csv`, que nos permite leer y escribir datos en este formato de manera sencilla.

### Ejemplo de uso del módulo `csv`

```python
import csv

# Escribir datos en un archivo CSV
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
# Leer datos de un archivo CSV
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Los archivos CSV consisten en filas de datos, donde cada fila contiene valores separados por comas. El módulo `csv` facilita la lectura y escritura de estos archivos en Python.

La función `reader` devuelve un objeto iterable que puede ser recorrido para acceder a cada fila del archivo CSV. Cada fila se representa como una lista de valores. Se le puede indicar un delimitador diferente si los valores no están separados por comas, utilizando el parámetro `delimiter` al crear el objeto `reader`.

La función `next` se puede utilizar para saltar la fila de encabezado si es necesario. En ciertos casos, puede ser útil convertir cada fila en un diccionario para facilitar el acceso a los valores por nombre de columna. Esto se puede lograr utilizando `csv.DictReader`.

## Ejercicios de clase: [Llamadas a APIs](proyecto_cli_app_tiempo.md)