import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferreteria_sys.settings')
django.setup()

from django.contrib.auth.models import User, Group, Permission
from administracion.models import Usuario, EmpresaConfig
from producto.models import Categoria, Marca, Proveedor, Producto
from venta.models import TipoPago, Cliente, Descuento
from django.utils import timezone
from datetime import timedelta

print("==> Inicializando datos del sistema...")

# 1. Grupo Administrador
admin_group, _ = Group.objects.get_or_create(name="Administrador")
vendedor_group, _ = Group.objects.get_or_create(name="Vendedor")

# Asignar permisos a Admin
todos_los_permisos = Permission.objects.exclude(
    content_type__app_label__in=['admin', 'contenttypes', 'sessions']
)
admin_group.permissions.set(todos_los_permisos)

# 2. Superusuario Django
admin_user = User.objects.filter(username="admin").first()
if not admin_user:
    admin_user = User.objects.create_superuser("admin", "admin@elfuerte.com", "admin")
    print("  Superusuario 'admin' creado (password: admin).")
else:
    admin_user.set_password("admin")
    admin_user.email = "admin@elfuerte.com"
    admin_user.save()
    print("  Superusuario 'admin' actualizado.")

admin_user.groups.add(admin_group)

# 3. Usuario interno Ferretería
usuario_interno = Usuario.objects.filter(correo="admin@elfuerte.com").first()
if not usuario_interno:
    usuario_interno = Usuario(
        nombre="Administrador General",
        correo="admin@elfuerte.com",
        contrasena="admin",
        rol=admin_group
    )
    usuario_interno.save()
    print("  Usuario interno ferretería 'admin@elfuerte.com' creado.")
else:
    usuario_interno.rol = admin_group
    usuario_interno.save()
    print("  Usuario interno ferretería ya existente.")

# 4. Configuración de Empresa
empresa = EmpresaConfig.objects.first()
if not empresa:
    empresa = EmpresaConfig.objects.create(
        nombre="Ferretería EL FUERTE",
        nit="1234567015",
        telefono="+591 70000000",
        direccion="Av. Principal #500, Santa Cruz de la Sierra",
        actualizado_por=usuario_interno
    )
    print("  Configuración de empresa creada.")

# 5. Tipos de Pago
for tipo_nombre in ["Efectivo", "Transferencia QR", "Tarjeta de Débito/Crédito"]:
    TipoPago.objects.get_or_create(nombre=tipo_nombre)
print("  Tipos de pago verificados.")

# 6. Categorías
cat_herramientas, _ = Categoria.objects.get_or_create(nombre="Herramientas", defaults={"descripcion": "Herramientas manuales y eléctricas"})
cat_pintura, _ = Categoria.objects.get_or_create(nombre="Pinturas", defaults={"descripcion": "Pinturas, barnices y selladores"})
cat_plomeria, _ = Categoria.objects.get_or_create(nombre="Plomería", defaults={"descripcion": "Tuberías, grifos y accesorios"})
cat_electricidad, _ = Categoria.objects.get_or_create(nombre="Electricidad", defaults={"descripcion": "Cables, tomacorrientes e iluminación"})

# 7. Marcas
marca_stanley, _ = Marca.objects.get_or_create(nombre="Stanley", defaults={"descripcion": "Herramientas de alta calidad"})
marca_bosch, _ = Marca.objects.get_or_create(nombre="Bosch", defaults={"descripcion": "Herramientas eléctricas profesionales"})
marca_monopol, _ = Marca.objects.get_or_create(nombre="Monopol", defaults={"descripcion": "Pinturas bolivianas"})
marca_tigre, _ = Marca.objects.get_or_create(nombre="Tigre", defaults={"descripcion": "Tuberías y conexiones"})

# 8. Proveedores
prov1, _ = Proveedor.objects.get_or_create(
    nombre_empresa="Importadora Ferretera del Oriente",
    defaults={
        "contacto": "Carlos Mendez",
        "telefono": "+591 71234567",
        "direccion": "Av. Banzer 4to Anillo"
    }
)
prov2, _ = Proveedor.objects.get_or_create(
    nombre_empresa="Distribuidora Industrial S.R.L.",
    defaults={
        "contacto": "Maria Perez",
        "telefono": "+591 72345678",
        "direccion": "Parque Industrial Mz. 12"
    }
)

# 9. Clientes
Cliente.objects.get_or_create(
    documento_identidad="0",
    defaults={
        "nombre": "Consumidor Final",
        "telefono": "70000000",
        "direccion": "Santa Cruz",
        "activo": True
    }
)
Cliente.objects.get_or_create(
    documento_identidad="6543210",
    defaults={
        "nombre": "Juan Pérez Constructora",
        "telefono": "71112233",
        "direccion": "Av. Cristo Redentor",
        "activo": True
    }
)

# 10. Productos de prueba
productos_demo = [
    {
        "codigo": "HER-001",
        "nombre": "Martillo de Uña 16oz Stanley",
        "descripcion": "Martillo ergonómico con mango de fibra",
        "precio_compra": Decimal("35.00"),
        "precio_venta": Decimal("55.00"),
        "stock_actual": 25,
        "stock_minimo": 5,
        "categoria": cat_herramientas,
        "marca": marca_stanley,
        "proveedor": prov1,
    },
    {
        "codigo": "HER-002",
        "nombre": "Taladro Percutor Bosch 650W",
        "descripcion": "Taladro percutor reversible GSB 13 RE",
        "precio_compra": Decimal("320.00"),
        "precio_venta": Decimal("450.00"),
        "stock_actual": 12,
        "stock_minimo": 3,
        "categoria": cat_herramientas,
        "marca": marca_bosch,
        "proveedor": prov1,
    },
    {
        "codigo": "PIN-001",
        "nombre": "Pintura Látex Lavable Blanco 18L Monopol",
        "descripcion": "Pintura mate para interiores y exteriores",
        "precio_compra": Decimal("180.00"),
        "precio_venta": Decimal("260.00"),
        "stock_actual": 18,
        "stock_minimo": 4,
        "categoria": cat_pintura,
        "marca": marca_monopol,
        "proveedor": prov2,
    },
    {
        "codigo": "PLO-001",
        "nombre": "Tubo PVC Presión 1/2 pulgada Tigre",
        "descripcion": "Tubo de PVC para agua potable 6 metros",
        "precio_compra": Decimal("18.00"),
        "precio_venta": Decimal("28.00"),
        "stock_actual": 60,
        "stock_minimo": 10,
        "categoria": cat_plomeria,
        "marca": marca_tigre,
        "proveedor": prov2,
    },
    {
        "codigo": "ELE-001",
        "nombre": "Cinta Aislante Negra 20m 3M",
        "descripcion": "Cinta aisladora de vinilo de alta resistencia",
        "precio_compra": Decimal("6.00"),
        "precio_venta": Decimal("12.00"),
        "stock_actual": 4,  # Stock bajo para probar alertas del dashboard
        "stock_minimo": 10,
        "categoria": cat_electricidad,
        "marca": marca_stanley,
        "proveedor": prov1,
    }
]

for prod in productos_demo:
    if not Producto.objects.filter(codigo=prod["codigo"]).exists():
        Producto.objects.create(**prod)
        print(f"  Producto {prod['codigo']} - {prod['nombre']} creado.")

# 11. Descuento de prueba
ahora = timezone.now()
Descuento.objects.get_or_create(
    nombre="Descuento Promocional 10%",
    defaults={
        "porcentaje": Decimal("10.00"),
        "fecha_inicio": ahora - timedelta(days=1),
        "fecha_fin": ahora + timedelta(days=30),
    }
)

print("==> ¡Inicialización completada con éxito!")
