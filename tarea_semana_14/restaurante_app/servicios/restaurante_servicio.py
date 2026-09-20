from modelos.producto import Producto


class RestauranteServicio:

    def __init__(self, productos, usuarios, archivo_servicio):
        self.productos = productos
        self.usuarios = usuarios
        self.archivo_servicio = archivo_servicio

    def validar_acceso(self, identificacion, contrasena):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                if usuario.validar_contrasena(contrasena):
                    return usuario

        return None

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios

    def registrar_producto(self, codigo, nombre, categoria, precio, stock):
        if not codigo or not nombre or not categoria:
            return False, "Complete todos los campos."

        if self.obtener_producto(codigo):
            return False, "El código ya existe."

        try:
            precio = float(precio)
            stock = int(stock)
        except ValueError:
            return False, "Precio y stock deben ser números."

        if precio < 0 or stock < 0:
            return False, "Precio y stock no pueden ser negativos."

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        self.productos.append(producto)
        self.archivo_servicio.guardar_productos(self.productos)

        return True, "Producto registrado correctamente."

    def obtener_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ):
        producto = self.obtener_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        if not nombre or not categoria:
            return False, "Complete todos los campos."

        try:
            precio = float(precio)
            stock = int(stock)
        except ValueError:
            return False, "Precio y stock deben ser números."

        if precio < 0 or stock < 0:
            return False, "Precio y stock no pueden ser negativos."

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock

        self.archivo_servicio.guardar_productos(self.productos)

        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, codigo):
        producto = self.obtener_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        self.productos.remove(producto)
        self.archivo_servicio.guardar_productos(self.productos)

        return True, "Producto eliminado correctamente."
    