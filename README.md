# Agenda de Django

Este es un proyecto de agenda desarrollado en Django que permite gestionar contactos, tareas, reuniones, itinerarios de viajes y usuarios.

## Características

- **Gestión de Contactos**: Permite crear, ver, editar y eliminar contactos. Cada contacto puede tener un nombre, apellido, dirección, número de teléfono y correo electrónico.

- **Gestión de Tareas**: Permite crear, ver, editar y eliminar tareas pendientes. Cada tarea puede tener un título, descripción, fecha estimada de finalización y nivel de prioridad.

- **Gestión de Reuniones**: Permite crear, ver, editar y eliminar reuniones. Cada reunión puede tener un título, descripción, fecha y hora de inicio y finalización, y lista de participantes.

- **Gestión de Itinerarios de Viajes**: Permite crear, ver, editar y eliminar itinerarios de viajes. Cada itinerario puede tener una lista de actividades, checklist de hora de salida y de regreso, destino y duración.

- **Gestión de Usuarios**: Permite registrar usuarios, modificar sus datos, realizar inicio de sesión y cierre de sesión, y agregarles un avatar.

## Organización del Proyecto

El proyecto está organizado en varias aplicaciones:

1. **Contactos**: Gestiona la información de contactos.
   - Archivos relevantes: `models.py`, `views.py`, `forms.py`, `urls.py`, `templates/contact`.

2. **Tareas**: Gestiona las tareas pendientes.
   - Archivos relevantes: `models.py`, `views.py`, `forms.py`, `urls.py`, `templates/todo`.

3. **Reuniones**: Gestiona las reuniones programadas.
   - Archivos relevantes: `models.py`, `views.py`, `forms.py`, `urls.py`, `templates/meetings`.

4. **Itinerarios de Viajes**: Gestiona los itinerarios de viajes.
   - Archivos relevantes: `models.py`, `views.py`, `forms.py`, `urls.py`, `templates/travels`.

5. **Usuarios**: Gestiona el registro de usuarios y la autenticación.
   - Archivos relevantes: `models.py`, `views.py`, `forms.py`, `urls.py`, `templates/users`.

Otros archivos importantes incluyen:

- `settings.py`: Configuración del proyecto Django.
- `urls.py`: Definición de las URL del proyecto.
- `templates/`: Plantillas HTML para las vistas.

## Backend vs. Frontend

Este proyecto se enfoca principalmente en el backend, con una mínima parte del frontend. La mayoría de las funcionalidades y lógica están implementadas en el backend utilizando Django y Python, mientras que el frontend consiste principalmente en plantillas HTML simples para representar los datos.

## Instalación y Uso

1. Clona este repositorio: `git clone https://ruta/a/tu/repositorio.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Realiza las migraciones de la base de datos: `python manage.py migrate`
4. Inicia el servidor de desarrollo: `python manage.py runserver`

**Nota**: El usuario administrador es `admin` y la contraseña es `prueba123`.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras para este proyecto, no dudes en abrir un issue o enviar un pull request.