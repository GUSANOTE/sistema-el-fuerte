# Sistema de Gestión y POS — Ferretería EL FUERTE

Sistema web integral para la administración comercial, control de inventario y punto de venta (POS) para ferreterías y negocios de retail. Desarrollado con **Python**, **Django**, arquitectura modular y exportaciones a PDF y Excel.

---

## 🚀 Inicio Rápido (En 1 paso)

### Opción A: Con PowerShell (Descargar y ejecutar directamente)
Si quieres probarlo en cualquier equipo con Windows y Python instalado:

```powershell
irm https://github.com/GUSANOTE/sistema-el-fuerte/archive/refs/heads/main.zip -OutFile repo.zip; Expand-Archive repo.zip -DestinationPath . -Force; cd sistema-el-fuerte-main; .\iniciar_sistema.bat
```

### Opción B: Si ya clonaste o descargaste la carpeta
Simplemente haz doble clic sobre:
```
iniciar_sistema.bat
```
El script creará el entorno virtual, instalará las dependencias necesarias y levantará el sistema abriendo tu navegador en `http://127.0.0.1:8000/`.

---

## 🔑 Credenciales de Acceso

* **URL:** `http://127.0.0.1:8000/`
* **Usuario:** `admin`
* **Contraseña:** `admin`

---

## 💻 Uso en Visual Studio Code

1. Abre Visual Studio Code.
2. Abre la carpeta del proyecto (**Archivo > Abrir carpeta**).
3. Presiona **F5** para iniciar en modo depuración (el archivo `.vscode/launch.json` ya viene listo), o abre una terminal con `Ctrl + Shift + \`` y corre:
   ```powershell
   .\iniciar_sistema.bat
   ```

---

## 📋 Características Principales

* **Punto de Venta (POS):** Búsqueda de productos, carrito dinámico, validación de stock antes de vender, cálculo de vuelto, descuentos por fechas y emisión de recibos en formato PDF.
* **Control de Inventario:**
  * Registro de entradas de mercadería asociadas a proveedores.
  * Registro de salidas por merma, rotura o ajuste interno.
  * Alertas visuales de stock bajo y productos agotados en tiempo real.
* **Catálogo Maestro:** CRUD de productos, categorías, marcas y proveedores, con sugerencia automática de códigos correlativos (`HER-001`, `HER-002`, etc.).
* **Reportes y Analítica:**
  * Ventas por rango de fechas.
  * Inventario valorizado a precio de venta.
  * Ranking de productos más vendidos.
  * Rendimiento por vendedor.
  * Arqueo de caja por método de pago (Efectivo, Transferencia QR, Tarjeta).
  * **Exportación a Excel (.xlsx)** con formato profesional y encabezados congelados.
* **Seguridad y Permisos:** Control de acceso por roles (Administrador, Vendedor, Almacenero) y permisos granulares por acción.

---

## 🛠️ Tecnologías

* **Backend:** Python 3.10+ & Django 6.0
* **Base de datos:** SQLite (desarrollo/pruebas rápidas) y PostgreSQL (producción)
* **Generación de Documentos:** `xhtml2pdf` / `reportlab` (PDF) y `openpyxl` (Excel)
* **Frontend:** Plantillas HTML con diseño responsivo y componentes dinámicos

Para consultar la guía detallada de configuración manual y despliegue con PostgreSQL, revisa el archivo [GUIA_INSTALACION.md](GUIA_INSTALACION.md).
