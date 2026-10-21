from django.contrib import admin

from .models import (
    Rol, Empleado, Usuario, UsuarioRol,
    TipoMovCaja, Caja, Proveedor, MetodoPago, OrdCompra, Compra,
    Categoria, Unidad, Producto, TipoMovInventario,
    Cliente, Venta, DetVenta, VentaMetodoPago, Comprobante,
    MovCaja, DetCompra, CompraMetodoPago, ProveedorProducto,
    DetOrdCompra, MovInventario, DetInventario,
    HistorialDevolucion, HistorialGarantia
)

admin.site.register(Rol)
admin.site.register(Empleado)
admin.site.register(Usuario)
admin.site.register(UsuarioRol)
admin.site.register(TipoMovCaja)
admin.site.register(Caja)
admin.site.register(Proveedor)
admin.site.register(MetodoPago)
admin.site.register(OrdCompra)
admin.site.register(Compra)
admin.site.register(Categoria)
admin.site.register(Unidad)
admin.site.register(Producto)
admin.site.register(TipoMovInventario)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetVenta)
admin.site.register(VentaMetodoPago)
admin.site.register(Comprobante)
admin.site.register(MovCaja)
admin.site.register(DetCompra)
admin.site.register(CompraMetodoPago)
admin.site.register(ProveedorProducto)
admin.site.register(DetOrdCompra)
admin.site.register(MovInventario)
admin.site.register(DetInventario)
admin.site.register(HistorialDevolucion)
admin.site.register(HistorialGarantia)


# Register your models here.
