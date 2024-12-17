# Fortigate Automation Scripts

Este proyecto es una aplicación web que permite generar scripts para crear objetos direcciones MAC, usuarios y direcciones IPv4 en un firewall Fortigate.

## Requisitos

- Python 3.7 o superior
- Flask
- Flask-WTF

## Instalación

1. Clona este repositorio en tu máquina local:
    ```sh
    git clone https://github.com/tu-usuario/fortigate-automation-scripts.git
    cd fortigate-automation-scripts
    ```

2. Crea un entorno virtual y actívalo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias necesarias:
    ```sh
    pip install -r requirements.txt
    ```

## Ejecución

1. Asegúrate de que el entorno virtual esté activado:
    ```sh
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

2. Ejecuta la aplicación:
    ```sh
    flask run
    ```

3. Abre tu navegador web y navega a `http://127.0.0.1:5000` para acceder a la aplicación.

## Uso

1. **Generar Script MAC**:
    - Ingresa un listado de direcciones MAC separadas por comas o líneas.
    - Haz clic en el botón "Generar Script MAC".

2. **Generar Script Usuarios**:
    - Ingresa un listado de usuarios y contraseñas, uno por línea en el formato `nombre_usuario contraseña`.
    - Haz clic en el botón "Generar Script Usuarios".

3. **Generar Script IP**:
    - Ingresa un listado de direcciones IPv4 separadas por comas o líneas.
    - Haz clic en el botón "Generar Script IP".

4. El script generado se mostrará en la siguiente página. Puedes copiar el script haciendo clic en el botón "Copy".

## Estructura del Proyecto

- [app](http://_vscodecontentref_/0)
  - `__init__.py`: Inicializa la aplicación Flask.
  - `forms.py`: Define los formularios para ingresar datos.
  - `routes.py`: Define las rutas y la lógica para generar los scripts.
  - `templates/`
    - `base.html`: Plantilla base para la aplicación.
    - [form.html](http://_vscodecontentref_/1): Plantilla para el formulario de entrada.
    - `result.html`: Plantilla para mostrar el script generado.
  - `static/`
    - `styles.css`: Archivo de estilos CSS.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
