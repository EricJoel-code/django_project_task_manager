# 📋 Sistema de Gestión de Proyectos y Tareas

Aplicación web desarrollada con **Django** para la gestión de proyectos y tareas, que implementa un **CRUD completo**, autenticación de usuarios y una interfaz gráfica funcional.

El sistema permite a los usuarios registrarse, iniciar sesión y acceder a un **dashboard** desde donde pueden administrar su perfil, proyectos y tareas, haciendo uso del **ORM de Django** y una base de datos **SQLite** por defecto.

---

## 🚀 Características Principales

* Registro e inicio de sesión de usuarios
* Autenticación y cierre de sesión
* Dashboard principal para el usuario
* Gestión de perfil:

  * Avatar por defecto
  * Actualización de datos personales
  * Carga de foto de perfil
* Gestión de proyectos (CRUD completo)
* Gestión de tareas asociadas a proyectos (CRUD completo)
* Uso del ORM de Django para la persistencia de datos
* Interfaz gráfica basada en templates HTML
* Base de datos SQLite (configuración por defecto)

---

## 🛠️ Tecnologías Utilizadas

* Python
* Django
* HTML (Django Templates)
* CSS
* JavaScript
* SQLite
* Django ORM
* Git & GitHub

---

## 🧱 Estructura del Proyecto

```text
myweb/                  # Proyecto principal
│
├── users/               # App de gestión de usuarios
│   ├── templates/       # Templates HTML
│   ├── static/
│   │   ├── icons/       # Íconos SVG
│   │   ├── js/          # Archivos JavaScript
│   │   └── styles/      # Archivos CSS
│   └── ...
│
├── myapp/               # App de proyectos y tareas
│   ├── templates/       # Templates HTML
│   ├── static/
│   │   ├── icons/       # Íconos SVG
│   │   ├── js/          # Archivos JavaScript
│   │   └── styles/      # Archivos CSS
│   └── ...
│
├── db.sqlite3           # Base de datos
├── manage.py
└── README.md
```

---

## 👤 Gestión de Usuarios

* Registro de nuevos usuarios
* Inicio y cierre de sesión
* Gestión de perfil
* Uso de lógica condicional en templates, por ejemplo:

```django
{% if user.first_name %}
  <p>Bienvenido, {{ user.first_name }}</p>
{% endif %}
```

---

## ▶️ Ejecución del Proyecto

### 1️⃣ Crear y activar entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar migraciones

```bash
python manage.py migrate
```

### 4️⃣ Iniciar servidor de desarrollo

```bash
python manage.py runserver
```

Accede desde el navegador a:

```text
http://127.0.0.1:8000/
```

---

## 📌 Estado del Proyecto

El proyecto se encuentra funcional, aunque aún se contemplan **mejoras futuras**, como:

* Mejoras en la interfaz de usuario
* Roles y permisos avanzados
* Optimización de vistas y consultas
* Migración a otra base de datos (PostgreSQL / MySQL)

---

## ⚠️ Nota

Este proyecto fue desarrollado con fines educativos y de práctica, aplicando conceptos fundamentales de Django, autenticación, ORM y arquitectura MVT.

---

⭐ Si te resulta útil o interesante, ¡no olvides darle una estrella al repositorio!
