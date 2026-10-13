# Guía de Instalación y Uso — Sistema Ferretería "EL FUERTE"

Este proyecto es un sistema de gestión comercial y punto de venta (POS) desarrollado en **Django** y **Python**. Incluye control de stock en tiempo real, catálogo de productos, facturación/recibos en PDF, arqueo de caja y reportes exportables a Excel.

---

## ⚡ Método 1: Inicio Rápido (En 1 minuto)

El proyecto ya incluye una base de datos local con datos de prueba cargados (productos, clientes, proveedores y usuario administrador) y un lanzador automático.

### Si estás en Windows:
1. Haz doble clic en el archivo **`iniciar_sistema.bat`**.
2. El script detectará si tienes el entorno virtual listo; si no, lo creará, instalará los paquetes necesarios y abrirá el sistema en tu navegador.

### Si usas Visual Studio Code:
1. Abre VS Code y selecciona **Archivo > Abrir carpeta** (elige la carpeta del proyecto).
2. Abre la terminal (`Ctrl + Shift + \`` o menú *Terminal > Nueva terminal*).
3. Escribe:
   ```powershell
   .\iniciar_sistema.bat
   ```
   *(O simplemente presiona **F5**, ya que el archivo `.vscode/launch.json` está preconfigurado).*

4. Abre tu navegador en: **`http://127.0.0.1:8000/`**

---

## 🔑 Credenciales de Acceso

| Rol | Usuario | Contraseña | Acceso |
| :--- | :--- | :--- | :--- |
| **Administrador General** | `admin` | `admin` | Acceso total al sistema |

> **Nota:** La cuenta está vinculada tanto a la autenticación de Django como al módulo interno de vendedores, por lo que puedes registrar ventas y movimientos de almacén de inmediato.

---

## 🛠️ Método 2: Instalación Manual Paso a Paso

Si prefieres configurar el entorno manualmente desde la consola:

### 1. Requisitos
* Python 3.10 o superior ([python.org](https://www.python.org/))  
  *(Al instalar en Windows, marca la opción **"Add python.exe to PATH"**).*

### 2. Crear y activar el entorno virtual
En la raíz del proyecto ejecuta:

**Windows (PowerShell o CMD):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar librerías
```bash
pip install -r requirements.txt
```

### 4. Base de datos y datos iniciales
El sistema utiliza **SQLite** por defecto para desarrollo local (no necesitas instalar ningún servidor adicional):

```bash
# Aplicar migraciones
python manage.py migrate

# Cargar datos de prueba (si no usas el db.sqlite3 incluido)
python init_db.py
```

### 5. Iniciar el servidor
```bash
python manage.py runserver
```

Ingresa a [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en tu navegador.

---

## 🗄️ Configuración para Producción (PostgreSQL)

Si deseas conectar el sistema a un servidor PostgreSQL en lugar de SQLite:

1. Crea la base de datos en PostgreSQL:
   ```sql
   CREATE DATABASE bd_elfuerte;
   CREATE USER elfuerte_user WITH PASSWORD 'tu_contraseña';
   GRANT ALL PRIVILEGES ON DATABASE bd_elfuerte TO elfuerte_user;
   ```

2. Configura las variables de entorno (o defínelas en tu archivo de configuración):
   * `DJANGO_DB_ENGINE=postgresql`
   * `DB_NAME=bd_elfuerte`
   * `DB_USER=elfuerte_user`
   * `DB_PASSWORD=tu_contraseña`
   * `DB_HOST=localhost`
   * `DB_PORT=5432`

3. Ejecuta las migraciones:
   ```bash
   python manage.py migrate
   python init_db.py
   ```

---

## 📦 Módulos Principales del Sistema

* **Dashboard (`/`):** Indicadores del día (ingresos, transacciones, productos con bajo stock, gráfico de ventas semanales).
* **Punto de Venta (`/venta/nueva/`):** Carrito dinámico, selección de clientes, cálculo de vueltos, aplicación de descuentos promocionales y emisión de recibos en PDF.
* **Inventario y Stock (`/stock/`):** Registro de entradas por compra con proveedor y salidas por merma/ajuste con validación de stock disponible.
* **Catálogo de Productos (`/productos/gestion/`):** Gestión de precios de costo vs. venta, cálculo automático de códigos (ej. `HER-001`), marcas y categorías.
* **Reportes (`/reportes/`):** Filtros por rango de fechas, arqueo de caja por método de pago (Efectivo, QR, Tarjeta), top productos y exportación nativa a **Excel (.xlsx)** con formato estilizado.
* **Administración (`/usuarios/`, `/roles/`, `/configuracion/`):** Control de acceso por permisos granulares y datos fiscales de la empresa.

---

## ❓ Preguntas Frecuentes / Solución de Problemas

#### 1. "python no se reconoce como un comando interno o externo"
Python no se agregó a las variables de entorno de Windows durante la instalación. Reinstala Python asegurándote de marcar la casilla **"Add python.exe to PATH"** en la primera pantalla del instalador.

#### 2. "Error: That port is already in use"
El puerto 8000 está ocupado por otra aplicación. Puedes iniciar el servidor en otro puerto indicándolo al final:
```bash
python manage.py runserver 8080
```
Y luego ingresar a `http://127.0.0.1:8080/`.

#### 3. ¿Cómo restauro la base de datos con los datos de ejemplo?
Si modificaste o borraste datos durante tus pruebas y quieres volver al estado original:
```bash
python init_db.py
```
