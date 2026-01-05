🚀 Django Project:
Este es un proyecto de práctica desarrollado para dominar las funcionalidades principales de Django Web Framework. El objetivo es construir una aplicación funcional mientras se exploran conceptos desde el ORM hasta la autenticación y el despliegue.

📋 Funcionalidades Implementadas
En este proyecto he puesto en práctica los siguientes pilares de Django:

Manejo de Modelos y ORM: Creación de bases de datos relacionales, migraciones y consultas complejas.

Sistema de Plantillas (Django Templates): Uso de herencia de bloques, filtros y etiquetas lógicas.

Vistas Basadas en Funciones (FBV) y Clases (CBV): Implementación de lógica de negocio y CRUD completo.

Autenticación de Usuarios: Registro, inicio de sesión y gestión de permisos/grupos.

Formularios (Django Forms): Validación de datos y formularios vinculados a modelos (ModelForm).

Panel de Administración: Personalización de admin.py para gestionar los datos visualmente.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.12.2

Framework: Django 6.0

Base de Datos: SQLite (Desarrollo) / PostgreSQL (Opcional)

Frontend: Bootstrap / CSS puro (opcional)

⚙️ Instalación y Configuración
Sigue estos pasos para ejecutar el proyecto localmente:

Clona el repositorio:

Bash

git clone https://github.com/EricJoel-code/Django-Project.git
cd Django-Project
Crea y activa un entorno virtual:

Bash

python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
Instala las dependencias:

Bash

pip install -r requirements.txt
Realiza las migraciones:

Bash

python manage.py makemigrations
python manage.py migrate
Crea un superusuario (para el panel admin):

Bash

python manage.py createsuperuser
Inicia el servidor de desarrollo:

Bash

python manage.py runserver
Visita http://127.0.0.1:8000 en tu navegador.

📂 Estructura del Proyecto
/core: Configuración principal del proyecto (settings.py, urls.py).

/apps: Carpeta contenedora de las diferentes aplicaciones del proyecto.

/templates: Plantillas HTML globales y específicas.

/static: Archivos CSS, JS e imágenes.

/media: Archivos subidos por los usuarios.

🧠 Aprendizajes Clave
Durante el desarrollo de este proyecto, aprendí a:

Configurar rutas dinámicas mediante urls.py.

Utilizar el contexto para pasar datos de la base de datos a la interfaz.

Proteger rutas para que solo usuarios autenticados puedan acceder.

✒️ Autor
Eric Cacuango - https://github.com/EricJoel-code