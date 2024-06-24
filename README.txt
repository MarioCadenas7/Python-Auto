# Conversor de Monedas

Este proyecto es un conversor de monedas que permite convertir cantidades entre diferentes monedas utilizando tasas de cambio en tiempo real. La interfaz gráfica fue creada con `tkinter` y los datos de las tasas de cambio son obtenidos de la API de Exchange Rate API.

## Características

- Conversión de monedas en tiempo real.
- Interfaz gráfica de usuario intuitiva y fácil de usar.
- Soporte para múltiples monedas (USD, EUR, GBP, JPY, AUD).

## Requisitos

- Python 3.6 o superior
- Librería `requests`

## Instalación

1. Clona el repositorio o descarga los archivos del proyecto:

    ```sh
    git clone https://github.com/tu-usuario/conversor-de-monedas.git
    cd conversor-de-monedas
    ```

2. Crea un entorno virtual (opcional pero recomendado):

    ```sh
    python -m venv env
    ```

3. Activa el entorno virtual:

    - En Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - En macOS/Linux:
        ```sh
        source env/bin/activate
        ```

4. Instala las dependencias:

    ```sh
    pip install requests
    ```

## Ejecución

Para ejecutar la aplicación, simplemente usa el siguiente comando:

```sh
python currency_converter.py
