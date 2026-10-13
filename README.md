# Sistema de Gestión - Ferretería EL FUERTE
## Guía de Instalación y Configuración

Este documento detalla los pasos necesarios para instalar, configurar y ejecutar el sistema en un entorno local o de producción.

---

### 1. Requisitos Previos

Asegúrese de tener instaladas las siguientes herramientas en su equipo:

- **Python**: Versión 3.10 o superior (verificar con `python --version`).
- **PostgreSQL**: Versión 13 o superior con servicio activo.
- **Git** o descompresor de archivos (.zip).

---

### 2. Entorno Virtual e Instalación de Dependencias

Abra una terminal en la carpeta principal del proyecto y ejecute:

#### En Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

#### En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Configuración de la Base de Datos (PostgreSQL)

1. Ingrese a la consola de PostgreSQL (`psql`) o mediante **pgAdmin**.
2. Cree la base de datos y el usuario correspondiente:

```sql
CREATE DATABASE bd_elfuerte;
CREATE USER elfuerte_user WITH PASSWORD 'tu_password_aqui';
GRANT ALL PRIVILEGES ON DATABASE bd_elfuerte TO elfuerte_user;
```

3. Revise el archivo `ferreteria_sys/settings.py` en la sección `DATABASES` para verificar que las credenciales coincidan con las de su servidor PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bd_elfuerte',
        'USER': 'elfuerte_user',
        'PASSWORD': 'tu_password_aqui',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 4. Migraciones de la Base de Datos

Con el entorno virtual activo y la base de datos creada en PostgreSQL, ejecute:

```bash
python manage.py makemigrations
python manage.py migrate
```

Esto generará automáticamente todas las tablas del sistema (productos, categorías, ventas, stock, clientes, usuarios, etc.).

---

### 5. Creación del Usuario Administrador (Superusuario)

Para crear el usuario administrador inicial con acceso completo:

```bash
python manage.py createsuperuser
```

Ingrese los datos solicitados:
- **Username**: `admin`
- **Email**: `admin@elfuerte.com`
- **Password**: `admin` (si solicita confirmación por longitud, presione `y`)

*Alternativamente, puede ejecutar este comando directo:*
```bash
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@elfuerte.com', 'admin') if not User.objects.filter(username='admin').exists() else None"
```

---

### 6. Ejecución del Servidor

Inicie el servidor de desarrollo con el siguiente comando:

```bash
python manage.py runserver
```

---

### 7. Acceso al Sistema

Abra su navegador web e ingrese a:
- **URL**: `http://127.0.0.1:8000/` o `http://localhost:8000/`
- **Usuario**: `admin`
- **Contraseña**: `admin`
