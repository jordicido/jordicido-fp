# Proyecto Final: Weather CLI — Aplicación de Consulta Meteorológica

## 1. Descripción general del proyecto

En este proyecto desarrollarás una **aplicación de consola (CLI)** en Python que permitirá consultar el **tiempo actual y las previsiones meteorológicas** de cualquier ciudad del mundo utilizando **servicios web gratuitos (APIs públicas)**.

La aplicación no tendrá interfaz gráfica, sino que funcionará directamente desde el **terminal o la consola de comandos**, solicitando información al usuario y mostrando los resultados formateados en texto.

El objetivo es integrar en un proyecto completo los conocimientos básicos de **programación estructurada**, **manejo de ficheros**, **control de errores**, y **consumo de datos desde Internet (JSON)**.

Este proyecto está pensado para un nivel introductorio, pero con margen para que los estudiantes más avanzados puedan ampliar funcionalidades.

---

## 2. Funcionamiento general del programa

La aplicación se ejecutará desde consola, mostrando un **menú interactivo** con opciones como:

```python
=== Weather CLI ===
1) Consultar ciudad (1 día)
2) Consultar ciudad (3 días)
3) Ver último resultado
4) Ver historial (últimas consultas)
0) Salir
```

Cuando el usuario elija la opción “Consultar ciudad”, el programa:

1. Solicitará el nombre de la ciudad.
2. Consultará una API de geolocalización para obtener su **latitud y longitud**.
3. Con esas coordenadas, llamará a una API meteorológica para obtener la **temperatura actual, máxima y mínima, amanecer, atardecer y probabilidad de lluvia**.
4. Mostrará los resultados en pantalla y los guardará en un archivo local (`ultimo.json`).
5. Además, añadirá los datos a un historial de consultas (`historial.json`).

El programa debe ser capaz de **manejar errores comunes** (ciudad no encontrada, falta de conexión, formato erróneo del JSON, etc.) y funcionar incluso en **modo offline** usando un archivo local de ejemplo.

---

## 3. APIs utilizadas en el proyecto

El proyecto utiliza **dos APIs públicas** de la plataforma **[Open-Meteo](https://open-meteo.com/)**, que no requieren registro ni autenticación.

### 3.1. API de Geocoding (para obtener coordenadas)

**URL base:**
`https://geocoding-api.open-meteo.com/v1/search`

**Ejemplo de uso:**

```python
https://geocoding-api.open-meteo.com/v1/search?name=Valencia&count=1
```

**Respuesta típica (formato JSON):**

```json
{
  "results": [
    {
      "name": "Valencia",
      "latitude": 39.4702,
      "longitude": -0.3768,
      "country": "Spain"
    }
  ]
}
```

A partir de este JSON, el programa extraerá:

* `name` → nombre normalizado de la ciudad
* `latitude` y `longitude` → coordenadas para la segunda API

---

### 3.2. API de Previsión Meteorológica

**URL base:**
`https://api.open-meteo.com/v1/forecast`

**Ejemplo de uso:**

```python
https://api.open-meteo.com/v1/forecast?latitude=39.47&longitude=-0.37&hourly=temperature_2m,precipitation_probability&daily=sunrise,sunset,temperature_2m_max,temperature_2m_min&timezone=auto
```

**Respuesta típica:**

```json
{
  "latitude": 39.47,
  "longitude": -0.37,
  "daily": {
    "temperature_2m_max": [23.5],
    "temperature_2m_min": [14.2],
    "sunrise": ["2025-11-12T07:34"],
    "sunset": ["2025-11-12T17:49"]
  },
  "hourly": {
    "temperature_2m": [18.0, 19.1, 20.3, ...],
    "precipitation_probability": [10, 20, 30, ...]
  }
}
```

De aquí se extraerán los valores de:

* Temperatura actual (primer valor horario)
* Temperatura máxima y mínima del día
* Hora de amanecer y atardecer (últimos 5 caracteres: `HH:MM`)
* Probabilidad de precipitación

---

## 4. Estructura de archivos del proyecto

El proyecto se dividirá en varios **módulos de Python**, cada uno con una función clara y bien delimitada.
Esta separación facilita la comprensión y el mantenimiento del código, y ayuda a los alumnos a entender cómo se organizan los programas reales.

```python
weather_cli/
  main.py           # Programa principal: menú, flujo general y coordinación
  cli.py            # Interfaz de línea de comandos: menús e interacción con el usuario
  services.py       # Conexión con las APIs (geocoding y meteorología)
  storage.py        # Lectura y escritura de archivos JSON (persistencia)
  formatter.py      # Presentación y formato del resultado en texto
```

### Descripción de cada archivo:

* **`main.py`**
  Es el **punto de entrada** del programa. Contiene el bucle principal que muestra el menú, llama a las funciones adecuadas y coordina el flujo entre los demás módulos.

* **`cli.py`**
  Gestiona la **interacción con el usuario**: mostrar el menú, pedir opciones y textos, validar entradas y devolverlas al programa principal.

* **`services.py`**
  Contiene las funciones encargadas de **conectarse a las APIs**.
  Define cómo construir las URLs, enviar las peticiones y extraer los datos útiles del JSON.
  También puede incluir un pequeño control de errores de red (por ejemplo, `requests.exceptions.Timeout`).

* **`storage.py`**
  Se encarga de la **persistencia de datos**.
  Permite guardar el último resultado en `ultimo.json`, mantener un historial en `historial.json`.

* **`formatter.py`**
  Define cómo se **muestran los resultados** al usuario: formato de texto, etiquetas, redondeos, alineación, etc.

---

## 5. Funcionalidades obligatorias

Las siguientes características forman parte del **núcleo del proyecto**.
Todo alumno deberá implementarlas correctamente para considerar la práctica completa:

1. **Menú principal interactivo** con opciones numeradas y control básico de errores.
2. **Consulta meteorológica por ciudad:**

   * Solicitar nombre de la ciudad al usuario.
   * Obtener sus coordenadas mediante la API de Geocoding.
   * Obtener los datos del tiempo mediante la API de Forecast.
   * Mostrar un resumen claro con:

     * Ciudad y coordenadas
     * Temperatura actual
     * Temperaturas máxima y mínima del día
     * Amanecer y atardecer
     * Probabilidad de precipitación
3. **Persistencia de datos:**

   * Guardar el último resultado (`ultimo.json`).
   * Registrar todas las consultas en un archivo de historial (`historial.json`).
4. **Visualización de historial:** mostrar las últimas 5 consultas realizadas.
5. **Manejo de errores y robustez:**

   * Validar entradas del usuario (no vacías, sin números en el nombre de ciudad).
   * Controlar errores de red (sin conexión, ciudad inexistente).
   * Evitar que el programa se cierre inesperadamente.

---

## 6. Posibles ampliaciones (para quienes quieran ir más allá)

Estas ampliaciones son opcionales, pensadas para los alumnos que deseen profundizar:

| Nivel         | Ampliación                             | Descripción                                                                                      |
| ------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 🟢 Fácil      | Limitar el historial                   | Mostrar solo las últimas N consultas o filtrarlas por ciudad                                     |
| 🟢 Fácil      | Mostrar fecha y hora de la consulta    | Añadir un campo `timestamp` (fecha/hora ISO) al guardar datos                                    |
| 🟠 Intermedio | Cachear resultados                     | Si se consulta la misma ciudad en menos de 10 minutos, leer de `ultimo.json` sin llamar a la API |
| 🟠 Intermedio | Permitir días personalizados           | Pasar el número de días como parámetro (`--dias N`) desde la línea de comandos                   |
| 🟠 Intermedio | Mejorar formato de salida              | Mostrar las temperaturas en tabla o con colores usando ANSI                                      |
| 🔵 Avanzado   | Exportar datos a CSV o JSON comprimido | Generar un informe con todas las consultas                                                       |
| 🔵 Avanzado   | Gráfica ASCII                          | Dibujar una gráfica de temperaturas por hora con caracteres en texto                             |
| 🔵 Avanzado   | Tests unitarios                        | Probar funciones puras con `pytest` (por ejemplo, formateo o parsing de JSON)                    |


---

## 7. Temporización

* Sesión 1: Creación del proyecto, estructura de archivos, menú principal y conexión a las API.
* Sesión 2: Implementación de las diferentes consultas meteorológicas, presentación de resultados, manejo de datos JSON.
* Sesión 3: Persistencia de datos, historial de consultas, configuración de localización por defecto.
* Extras: Opciones de elección de datos a visualizar.