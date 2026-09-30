from django.db import models

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=150, unique=True)
    descripcion_rol = models.TextField()

    def __str__(self):
        return self.nombre_rol

    class Meta:
        db_table = 'roles'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre_rol']


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=150)
    apellido_empleado = models.CharField(max_length=150)
    dni_empleado = models.CharField(max_length=15, unique=True)
    telefono_empleado = models.CharField(max_length=20)
    email_empleado = models.EmailField(max_length=150, unique=True)

    def __str__(self):
        return f'{self.apellido_empleado}, {self.nombre_empleado}'

    class Meta:
        db_table = 'empleados'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellido_empleado', 'nombre_empleado']


class TipoMovCaja(models.Model):
    id_tipo_mov_caja = models.AutoField(primary_key=True)
    nombre_tipo_mov_caja = models.CharField(max_length=150)
    naturaleza_movimiento = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_tipo_mov_caja

    class Meta:
        db_table = 'tipos_mov_caja'
        verbose_name = 'Tipo de Movimiento de Caja'
        verbose_name_plural = 'Tipos de Movimiento de Caja'
        ordering = ['nombre_tipo_mov_caja']


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=150)
    apellido_cliente = models.CharField(max_length=150)
    dni_cliente = models.CharField(max_length=15, unique=True)
    telefono_cliente = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.apellido_cliente}, {self.nombre_cliente}'

    class Meta:
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['apellido_cliente', 'nombre_cliente']


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre_metodo_pago = models.CharField(max_length=150)
    descripcion_metodo_pago = models.TextField()

    def __str__(self):
        return self.nombre_metodo_pago

    class Meta:
        db_table = 'metodos_pago'
        verbose_name = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pago'
        ordering = ['nombre_metodo_pago']


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    razon_social_proveedor = models.CharField(max_length=150)
    cuit_proveedor = models.CharField(max_length=30, unique=True)
    telefono_proveedor = models.CharField(max_length=20)
    email_proveedor = models.EmailField(max_length=150)

    def __str__(self):
        return self.razon_social_proveedor

    class Meta:
        db_table = 'proveedores'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['razon_social_proveedor']


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=150)
    descripcion_categoria = models.TextField()

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre_categoria']


class Unidad(models.Model):
    id_unidad = models.AutoField(primary_key=True)
    nombre_unidad = models.CharField(max_length=150)
    abreviatura_unidad = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_unidad

    class Meta:
        db_table = 'unidades'
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        ordering = ['nombre_unidad']


class TipoMovInventario(models.Model):
    id_tipo_mov_inv = models.AutoField(primary_key=True)
    nombre_tipo_mov_inv = models.CharField(max_length=150)
    efecto_stock = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_tipo_mov_inv

    class Meta:
        db_table = 'tipos_mov_inventario'
        verbose_name = 'Tipo de Movimiento de Inventario'
        verbose_name_plural = 'Tipos de Movimiento de Inventario'
        ordering = ['nombre_tipo_mov_inv']


class OrdCompra(models.Model):
    id_ord_compra = models.AutoField(primary_key=True)
    fecha_emision_orden = models.DateField()
    estado_orden = models.CharField(max_length=30)
    total_orden = models.DecimalField(max_digits=13, decimal_places=2)

    def __str__(self):
        return f'Orden {self.id_ord_compra}'

    class Meta:
        db_table = 'ords_compra'
        verbose_name = 'Orden de Compra'
        verbose_name_plural = 'Órdenes de Compra'
        ordering = ['-fecha_emision_orden']


class Caja(models.Model):
    id_caja = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(
        Empleado, on_delete=models.RESTRICT, db_column='id_empleado'
    )
    fecha_apertura = models.DateTimeField()
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    saldo_inicial = models.DecimalField(max_digits=13, decimal_places=2)
    saldo_final = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Caja {self.id_caja} - {self.fecha_apertura}'

    class Meta:
        db_table = 'cajas'
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'
        ordering = ['-fecha_apertura']


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.RESTRICT, db_column='id_categoria'
    )
    id_unidad = models.ForeignKey(
        Unidad, on_delete=models.RESTRICT, db_column='id_unidad'
    )
    codigo_barras = models.CharField(max_length=50, unique=True)
    nombre_producto = models.CharField(max_length=150)
    precio_producto = models.DecimalField(max_digits=13, decimal_places=2)
    stock_actual = models.IntegerField()
    stock_minimo = models.IntegerField()

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre_producto']


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_caja = models.ForeignKey(
        Caja, on_delete=models.RESTRICT, db_column='id_caja'
    )
    id_cliente = models.ForeignKey(
        Cliente, on_delete=models.RESTRICT, db_column='id_cliente'
    )
    fecha_hora_venta = models.DateTimeField()
    monto_total_venta = models.DecimalField(max_digits=13, decimal_places=2)

    def __str__(self):
        return f'Venta {self.id_venta}'

    class Meta:
        db_table = 'ventas'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['-fecha_hora_venta']


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_caja = models.ForeignKey(
        Caja, on_delete=models.RESTRICT, db_column='id_caja'
    )
    id_proveedor = models.ForeignKey(
        Proveedor, on_delete=models.RESTRICT, db_column='id_proveedor'
    )
    fecha_hora_compra = models.DateTimeField()
    total_compra = models.DecimalField(max_digits=13, decimal_places=2)
    num_factura_compra = models.CharField(max_length=30)

    def __str__(self):
        return f'Compra {self.id_compra}'

    class Meta:
        db_table = 'compras'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['-fecha_hora_compra']


class MovCaja(models.Model):
    id_mov_caja = models.AutoField(primary_key=True)
    id_caja = models.ForeignKey(
        Caja, on_delete=models.RESTRICT, db_column='id_caja'
    )
    id_tipo_mov_caja = models.ForeignKey(
        TipoMovCaja, on_delete=models.RESTRICT, db_column='id_tipo_mov_caja'
    )
    id_venta = models.ForeignKey(
        Venta, on_delete=models.RESTRICT, null=True, blank=True,
        db_column='id_venta'
    )
    id_compra = models.ForeignKey(
        Compra, on_delete=models.RESTRICT, null=True, blank=True,
        db_column='id_compra'
    )
    monto_mov_caja = models.DecimalField(max_digits=13, decimal_places=2)
    hora_mov_caja = models.TimeField()
    observacion_mov_caja = models.TextField()

    def __str__(self):
        return f'Movimiento {self.id_mov_caja}'

    class Meta:
        db_table = 'movs_caja'
        verbose_name = 'Movimiento de Caja'
        verbose_name_plural = 'Movimientos de Caja'
        ordering = ['-hora_mov_caja']


class MovInventario(models.Model):
    id_mov_inv = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(
        Producto, on_delete=models.RESTRICT, db_column='id_producto'
    )
    id_tipo_mov_inv = models.ForeignKey(
        TipoMovInventario, on_delete=models.RESTRICT, db_column='id_tipo_mov_inv'
    )
    id_det_venta = models.ForeignKey(
        'DetVenta', on_delete=models.RESTRICT, null=True, blank=True,
        db_column='id_det_venta'
    )
    id_det_compra = models.ForeignKey(
        'DetCompra', on_delete=models.RESTRICT, null=True, blank=True,
        db_column='id_det_compra'
    )
    observacion_mov_inv = models.TextField()
    fecha_mov_inv = models.DateField()

    def __str__(self):
        return f'Movimiento Inventario {self.id_mov_inv}'

    class Meta:
        db_table = 'movs_inventario'
        verbose_name = 'Movimiento de Inventario'
        verbose_name_plural = 'Movimientos de Inventario'
        ordering = ['-fecha_mov_inv']


class HistorialDevolucion(models.Model):
    id_devolucion = models.AutoField(primary_key=True)
    id_mov_inv = models.OneToOneField(
        MovInventario, on_delete=models.RESTRICT, db_column='id_mov_inv'
    )
    motivo_devolucion = models.TextField()
    fecha_devolucion = models.DateField()
    estado_devolucion = models.CharField(max_length=30)

    def __str__(self):
        return f'Devolución {self.id_devolucion}'

    class Meta:
        db_table = 'historiales_devoluciones'
        verbose_name = 'Historial de Devolución'
        verbose_name_plural = 'Historiales de Devoluciones'
        ordering = ['-fecha_devolucion']


class HistorialGarantia(models.Model):
    id_garantia = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(
        Producto, on_delete=models.RESTRICT, db_column='id_producto'
    )
    fecha_reclamo = models.DateField()
    resolucion_garantia = models.TextField()
    estado_garantia = models.CharField(max_length=30)

    def __str__(self):
        return f'Garantía {self.id_garantia}'

    class Meta:
        db_table = 'historiales_garantias'
        verbose_name = 'Historial de Garantía'
        verbose_name_plural = 'Historiales de Garantías'
        ordering = ['-fecha_reclamo']


class DetInventario(models.Model):
    id_det_inventario = models.AutoField(primary_key=True)
    id_mov_inv = models.ForeignKey(
        MovInventario, on_delete=models.CASCADE, db_column='id_mov_inv'
    )
    id_producto = models.ForeignKey(
        Producto, on_delete=models.RESTRICT, db_column='id_producto'
    )
    cantidad_afectada = models.IntegerField()
    estado_item = models.CharField(max_length=30)

    def __str__(self):
        return f'Detalle Inventario {self.id_det_inventario}'

    class Meta:
        db_table = 'det_inventario'
        verbose_name = 'Detalle de Inventario'
        verbose_name_plural = 'Detalles de Inventario'
        ordering = ['id_det_inventario']


class DetVenta(models.Model):
    id_det_venta = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(
        Venta, on_delete=models.CASCADE, db_column='id_venta'
    )
    id_producto = models.ForeignKey(
        Producto, on_delete=models.RESTRICT, db_column='id_producto'
    )
    cantidad = models.IntegerField()
    precio_unit_venta = models.DecimalField(max_digits=13, decimal_places=2)
    subtotal_venta = models.DecimalField(max_digits=13, decimal_places=2)

    def __str__(self):
        return f'Detalle Venta {self.id_det_venta}'

    class Meta:
        db_table = 'det_venta'
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        ordering = ['id_det_venta']


class DetCompra(models.Model):
    id_det_compra = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey(
        Compra, on_delete=models.CASCADE, db_column='id_compra'
    )
    id_producto = models.ForeignKey(
        Producto, on_delete=models.RESTRICT, db_column='id_producto'
    )
    cantidad = models.IntegerField()
    costo_unit_compra = models.DecimalField(max_digits=13, decimal_places=2)
    subtotal_compra = models.DecimalField(max_digits=13, decimal_places=2)

    def __str__(self):
        return f'Detalle Compra {self.id_det_compra}'

    class Meta:
        db_table = 'det_compra'
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compra'
        ordering = ['id_det_compra']


class DetOrdCompra(models.Model):
    id_det_ord_compra = models.AutoField(primary_key=True)
    id_ord_compra = models.ForeignKey(
        OrdCompra, on_delete=models.CASCADE, db_column='id_ord_compra'
    )
    id_proveedor_producto = models.ForeignKey(
        'ProveedorProducto', on_delete=models.RESTRICT, db_column='id_proveedor_producto'
    )
    cantidad_pedida = models.IntegerField()

    def __str__(self):
        return f'Detalle Orden Compra {self.id_det_ord_compra}'

    class Meta:
        db_table = 'det_ord_compra'
        verbose_name = 'Detalle de Orden de Compra'
        verbose_name_plural = 'Detalles de Órdenes de Compra'
        ordering = ['id_det_ord_compra']


class EmpleadoRol(models.Model):
    id_empleado_rol = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(
        Empleado, on_delete=models.RESTRICT, db_column='id_empleado'
    )
    id_rol = models.ForeignKey(
        Rol, on_delete=models.RESTRICT, db_column='id_rol'
    )
    fecha_asignacion = models.DateField()

    def __str__(self):
        return f'{self.id_empleado} - {self.id_rol}'

    class Meta:
        db_table = 'empleado_rol'
        verbose_name = 'Asignación de Rol'
        verbose_name_plural = 'Asignaciones de Roles'
        ordering = ['-fecha_asignacion']


class VentaMetodoPago(models.Model):
    id_venta_met_pago = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(
        Venta, on_delete=models.CASCADE, db_column='id_venta'
    )
    id_metodo_pago = models.ForeignKey(
        MetodoPago, on_delete=models.RESTRICT, db_column='id_metodo_pago'
    )
    monto_abonado = models.DecimalField(max_digits=13, decimal_places=2)

    def __str__(self):
        return f'Pago Venta {self.id_venta_met_pago}'

    class Meta:
        db_table = 'venta_metodo_pago'
        verbose_name = 'Pago de Venta'
        verbose_name_plural = 'Pagos de Ventas'
        ordering = ['id_venta_met_pago']


class CompraMetodoPago(models.Model):
    id_compra_met_pago = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey(
        Compra, on_delete=models.CASCADE, db_column='id_compra'
    )
    id_metodo_pago = models.ForeignKey(
        MetodoPago, on_delete=models.RESTRICT, db_column='id_metodo_pago'
    )
    monto_pagado = models.DecimalField(max_digits=13, decimal_places=2)

    def __str__(self):
        return f'Pago Compra {self.id_compra_met_pago}'

    class Meta:
        db_table = 'compra_metodo_pago'
        verbose_name = 'Pago de Compra'
        verbose_name_plural = 'Pagos de Compras'
        ordering = ['id_compra_met_pago']


class ProveedorProducto(models.Model):
    id_prov_prod = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey(
        Proveedor, on_delete=models.RESTRICT, db_column='id_proveedor'
    )
    id_producto = models.ForeignKey(
        Producto, on_delete=models.RESTRICT, db_column='id_producto'
    )
    precio_costo = models.DecimalField(max_digits=13, decimal_places=2)

    def __str__(self):
        return f'{self.id_proveedor} - {self.id_producto}'

    class Meta:
        db_table = 'proveedor_producto'
        verbose_name = 'Producto de Proveedor'
        verbose_name_plural = 'Productos de Proveedores'
        ordering = ['id_prov_prod']


class Comprobante(models.Model):
    id_comprobante = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(
        Venta, on_delete=models.RESTRICT, db_column='id_venta'
    )
    tipo_comprobante = models.CharField(max_length=30)
    ruta_archivo = models.CharField(max_length=255)
    fecha_generacion_comprobante = models.DateTimeField()

    def __str__(self):
        return f'Comprobante {self.id_comprobante}'

    class Meta:
        db_table = 'comprobantes'
        verbose_name = 'Comprobante'
        verbose_name_plural = 'Comprobantes'
        ordering = ['-fecha_generacion_comprobante']



# Create your models here.
