from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:

    def __init__(self):
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

    @property
    def productos(self) -> list[Producto]:
        return self._productos

    @property
    def usuarios(self) -> list[Usuario]:
        return self._usuarios

    @property
    def ventas(self) -> list[Venta]:
        return self._ventas

    # =========================
    # PRODUCTOS
    # =========================

    def registrar_producto(
        self,
        producto: Producto
    ) -> bool:

        if self.buscar_producto(producto.codigo) is not None:
            print("Error: ya existe un producto con ese código.")
            return False

        self._productos.append(producto)

        print("Producto registrado correctamente.")
        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def listar_productos(self) -> None:

        if not self._productos:
            print("\nNo hay productos registrados.")
            return

        print("\n========== PRODUCTOS ==========")

        for producto in self._productos:
            producto.mostrar_informacion()

    # =========================
    # USUARIOS
    # =========================

    def registrar_usuario(
        self,
        usuario: Usuario
    ) -> bool:

        if self.buscar_usuario(
            usuario.identificacion
        ) is not None:

            print(
                "Error: ya existe un usuario con esa identificación."
            )

            return False

        self._usuarios.append(usuario)

        print("Usuario registrado correctamente.")
        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> None:

        if not self._usuarios:
            print("\nNo hay usuarios registrados.")
            return

        print("\n========== USUARIOS ==========")

        for usuario in self._usuarios:
            usuario.mostrar_informacion()

    # =========================
    # VENTAS
    # =========================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        if usuario is None:
            print("Error: el usuario no existe.")
            return False

        producto = self.buscar_producto(
            codigo_producto
        )

        if producto is None:
            print("Error: el producto no existe.")
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

        producto.vender(cantidad)

        print("\nVenta registrada correctamente.")
        print(f"Producto: {producto.nombre}")
        print(f"Cantidad vendida: {cantidad}")
        print(f"Stock restante: {producto.stock}")

        return True

    def buscar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        ventas_usuario: list[Venta] = []

        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)

        return ventas_usuario

    def listar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> None:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        if usuario is None:
            print("Error: el usuario no existe.")
            return

        ventas_usuario = self.buscar_ventas_usuario(
            identificacion_usuario
        )

        if not ventas_usuario:
            print(
                "\nEste usuario no tiene ventas registradas."
            )
            return

        print("\n========== VENTAS DEL USUARIO ==========")

        for venta in ventas_usuario:

            producto = self.buscar_producto(
                venta.producto_codigo
            )

            print("----------------------------------------")
            print(f"Producto: {venta.producto_codigo}")

            if producto is not None:
                print(f"Nombre: {producto.nombre}")

            print(f"Cantidad: {venta.cantidad}")

    # =========================
    # CARGA DE DATOS
    # =========================

    def cargar_productos(
        self,
        productos: list[Producto]
    ) -> None:

        self._productos = productos

    def cargar_usuarios(
        self,
        usuarios: list[Usuario]
    ) -> None:

        self._usuarios = usuarios

    def cargar_ventas(
        self,
        ventas: list[Venta]
    ) -> None:

        self._ventas = ventas
        