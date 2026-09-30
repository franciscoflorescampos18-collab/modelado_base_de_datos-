from django.contrib import admin

from .models import (
    Rol, Empleado, TipoMovCaja, Cliente, MetodoPago,
    Proveedor, Categoria, Unidad, TipoMovInventario, OrdCompra, Caja,
    Producto, MovCaja, Venta, Compra, MovInventario,
    HistorialDevolucion, HistorialGarantia, DetInventario,
    DetVenta, DetCompra, DetOrdCompra, EmpleadoRol,
    VentaMetodoPago, CompraMetodoPago, ProveedorProducto, Comprobante
)

admin.site.register(Rol)
admin.site.register(Empleado)
admin.site.register(TipoMovCaja)
admin.site.register(Cliente)
admin.site.register(MetodoPago)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Unidad)
admin.site.register(TipoMovInventario)
admin.site.register(OrdCompra)
admin.site.register(Caja)
admin.site.register(Producto)
admin.site.register(MovCaja)
admin.site.register(Venta)
admin.site.register(Compra)
admin.site.register(MovInventario)
admin.site.register(HistorialDevolucion)
admin.site.register(HistorialGarantia)
admin.site.register(DetInventario)
admin.site.register(DetVenta)
admin.site.register(DetCompra)
admin.site.register(DetOrdCompra)
admin.site.register(EmpleadoRol)
admin.site.register(VentaMetodoPago)
admin.site.register(CompraMetodoPago)
admin.site.register(ProveedorProducto)
admin.site.register(Comprobante)


# Register your models here.
