# Travel en Python 🌍

Este proyecto es una aplicación interactiva que permite visualizar rutas entre países en un mapa mundial utilizando el algoritmo de Dijkstra. La aplicación está construida con Flask en el backend y JavaScript en el frontend.

## Características

- **Mapa interactivo**: Escribe dos países y visualiza la ruta más corta entre ellos.
- **Algoritmo de Dijkstra**: Calcula la distancia más corta entre dos países.
- **Interfaz amigable**: Utiliza Bootstrap para un diseño moderno y responsivo.
- **Notificaciones**: Alertas interactivas con SweetAlert para errores y confirmaciones.

## Estructura del proyecto

- **Backend**: Flask para manejar las rutas y la lógica del servidor.
- **Frontend**: HTML, CSS, JavaScript y Bootstrap para la interfaz de usuario.
- **Algoritmo**: Implementación del algoritmo de Dijkstra para calcular rutas.

## Instalación

1. Clona este repositorio:
   ```bash
    git clone https://github.com/Prusia117/Travel-en-Python.git
    cd travel-en-python
   ```

2. Instala las dependencias del backend:
   ```bash
    cd api
    python -m venv .venv
    .venv\Scripts\activate
    pip install Flask
    pip install flask-cors
   ```

3. Inicia la api:
   ```bash
    python app.py
   ```

4. Abre el archivo index.html de la carpeta app en el navegador.

## Uso

1. Escribe el nombre en ingles de dos países en los campos de texto.
2. Haz clic en el botón 'Enviar' para calcular la ruta más corta.
3. Visualiza la ruta y la distancia en el mapa.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

