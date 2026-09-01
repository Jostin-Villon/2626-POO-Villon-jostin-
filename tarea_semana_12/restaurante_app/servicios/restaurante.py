from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class Restaurante:

    def __init__(self):
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []
        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_identificacion: dict[str, Usuario] = {}
        self._ventas_por_usuario: dict[str, list[Venta]] = {}

    @property
    def productos(self) -> list[Producto]:
        return self._productos

    @property
    def usuarios(self) -> list[Usuario]:
        return self._usuarios

    @property
    def ventas(self) -> list[Venta]:
        return self._ventas

    def registrar_producto(
        self,
        producto: Producto
    ) -> bool:

        if producto.codigo in self._productos_por_codigo:
            print(
                "Error: ya existe un producto con ese código."
            )
            return False

        self._productos.append(producto)

        self._productos_por_codigo[
            producto.codigo
        ] = producto

        print(
            "Producto registrado correctamente."
        )

        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

        return self._productos_por_codigo.get(codigo)

    def listar_productos(self) -> None:

        if not self._productos:
            print(
                "\nNo hay productos registrados."
            )
            return

        print(
            "\n========== PRODUCTOS =========="
        )

        for producto in self._productos:
            producto.mostrar_informacion()

    def registrar_usuario(
        self,
        usuario: Usuario
    ) -> bool:

        if usuario.identificacion in self._usuarios_por_identificacion:
            print(
                "Error: ya existe un usuario con esa identificación."
            )
            return False

        self._usuarios.append(usuario)

        self._usuarios_por_identificacion[
            usuario.identificacion
        ] = usuario

        self._ventas_por_usuario.setdefault(
            usuario.identificacion,
            []
        )

        print(
            "Usuario registrado correctamente."
        )

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        return self._usuarios_por_identificacion.get(
            identificacion
        )

    def listar_usuarios(self) -> None:

        if not self._usuarios:
            print(
                "\nNo hay usuarios registrados."
            )
            return

        print(
            "\n========== USUARIOS =========="
        )

        for usuario in self._usuarios:
            usuario.mostrar_informacion()

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        if usuario is None:
            print(
                "Error: el usuario no existe."
            )
            return False

        if producto is None:
            print(
                "Error: el producto no existe."
            )
            return False

        if cantidad <= 0:
            print(
                "Error: la cantidad debe ser mayor que cero."
            )
            return False

        if producto.stock < cantidad:
            print(
                f"Error: stock insuficiente. "
                f"Stock disponible: {producto.stock}"
            )
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self._ventas.append(venta)

        self._ventas_por_usuario.setdefault(
            usuario.identificacion,
            []
        )

        self._ventas_por_usuario[
            usuario.identificacion
        ].append(venta)

        producto.vender(cantidad)

        print(
            "\nVenta registrada correctamente."
        )

        print(
            f"Producto: {producto.nombre}"
        )

        print(
            f"Cantidad vendida: {cantidad}"
        )

        print(
            f"Stock restante: {producto.stock}"
        )

        return True

    def buscar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        # Ya no es necesario recorrer todas las ventas.
        return self._ventas_por_usuario.get(
            identificacion_usuario,
            []
        )

    def listar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> None:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        if usuario is None:
            print(
                "Error: el usuario no existe."
            )
            return

        ventas_usuario = self.buscar_ventas_usuario(
            identificacion_usuario
        )

        if not ventas_usuario:
            print(
                "\nEste usuario no tiene ventas registradas."
            )
            return

        print(
            "\n========== VENTAS DEL USUARIO =========="
        )

        for venta in ventas_usuario:

            producto = self.buscar_producto(
                venta.producto_codigo
            )

            print(
                "----------------------------------------"
            )

            print(
                f"Producto: {venta.producto_codigo}"
            )

            if producto is not None:
                print(
                    f"Nombre: {producto.nombre}"
                )

            print(
                f"Cantidad: {venta.cantidad}"
            )

    def cargar_productos(
        self,
        productos: list[Producto]
    ) -> None:

        self._productos = productos

        self._productos_por_codigo = {}

        for producto in self._productos:
            self._productos_por_codigo[
                producto.codigo
            ] = producto

    def cargar_usuarios(
        self,
        usuarios: list[Usuario]
    ) -> None:

        self._usuarios = usuarios

        self._usuarios_por_identificacion = {}

        for usuario in self._usuarios:
            self._usuarios_por_identificacion[
                usuario.identificacion
            ] = usuario

    def cargar_ventas(
        self,
        ventas: list[Venta]
    ) -> None:

        self._ventas = ventas

        self._ventas_por_usuario = {}

        for usuario in self._usuarios:
            self._ventas_por_usuario[
                usuario.identificacion
            ] = []

        for venta in self._ventas:

            self._ventas_por_usuario.setdefault(
                venta.usuario_id,
                []
            )

            self._ventas_por_usuario[
                venta.usuario_id
            ].append(venta)
