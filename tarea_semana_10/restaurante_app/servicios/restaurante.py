from modelos.producto import Producto
from modelos.usuario import Usuario


# Clase encargada de administrar productos y usuarios

class Restaurante:

    def __init__(self):
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

        # Diccionario para buscar productos por código
        self.productos_por_codigo: dict[int, Producto] = {}

        # Conjunto para guardar categorías sin repetir
        self.categorias: set[str] = set()

    # ========================================
    # PRODUCTOS
    # ========================================

    def registrar_producto(
        self,
        producto: Producto,
        mostrar_mensaje: bool = True
    ) -> bool:
        """Registra un producto."""

        if producto.codigo in self.productos_por_codigo:
            if mostrar_mensaje:
                print("Error: ya existe un producto con ese código.")
            return False

        self.productos.append(producto)

        self.productos_por_codigo[producto.codigo] = producto

        self.categorias.add(producto.categoria)

        if mostrar_mensaje:
            print("Producto registrado correctamente.")

        return True

    def buscar_producto(
        self,
        codigo: int
    ) -> Producto | None:
        """Busca un producto por código."""

        return self.productos_por_codigo.get(codigo)

    def actualizar_producto(
        self,
        codigo: int,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:
        """Actualiza un producto."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return False

        try:
            producto.nombre = nombre
            producto.categoria = categoria
            producto.precio = precio

            producto._validar_datos()

        except ValueError as error:
            print(f"Error: {error}")
            return False

        self._actualizar_categorias()

        print("Producto actualizado correctamente.")

        return True

    def eliminar_producto(
        self,
        codigo: int
    ) -> bool:
        """Elimina un producto."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return False

        self.productos.remove(producto)

        del self.productos_por_codigo[codigo]

        self._actualizar_categorias()

        print("Producto eliminado correctamente.")

        return True

    def listar_productos(self) -> None:
        """Muestra todos los productos."""

        if not self.productos:
            print("No existen productos registrados.")
            return

        print("\n========== PRODUCTOS ==========")

        for producto in self.productos:
            producto.mostrar_informacion()

    def _actualizar_categorias(self) -> None:
        """Actualiza las categorías."""

        self.categorias = {
            producto.categoria
            for producto in self.productos
        }

    def mostrar_categorias(self) -> None:
        """Muestra las categorías sin repetir."""

        if not self.categorias:
            print("No existen categorías registradas.")
            return

        print("\n====== CATEGORÍAS ======")

        for categoria in sorted(self.categorias):
            print(f"- {categoria}")

    # ========================================
    # USUARIOS
    # ========================================

    def registrar_usuario(
        self,
        usuario: Usuario
    ) -> bool:
        """Registra un usuario."""

        for usuario_registrado in self.usuarios:

            if (
                usuario_registrado.identificacion
                == usuario.identificacion
            ):
                print(
                    "Error: esa identificación ya está registrada."
                )
                return False

        self.usuarios.append(usuario)

        print("Usuario registrado correctamente.")

        return True

    def listar_usuarios(self) -> None:
        """Muestra todos los usuarios."""

        if not self.usuarios:
            print("No existen usuarios registrados.")
            return

        print("\n========== USUARIOS ==========")

        for usuario in self.usuarios:
            usuario.mostrar_informacion()
            