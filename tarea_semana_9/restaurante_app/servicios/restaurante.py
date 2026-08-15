from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:

    def __init__(self):
        self.productos: list[Producto] = []

        self.usuarios: list[Usuario] = []

        self.productos_por_codigo: dict[int, Producto] = {}

        self.categorias: set[str] = set()

    def registrar_producto(self, producto: Producto) -> bool:

        if producto.codigo in self.productos_por_codigo:
            print("Error: ya existe un producto con ese código.")
            return False

        self.productos.append(producto)

        self.productos_por_codigo[producto.codigo] = producto

        self.categorias.add(producto.categoria)

        print("Producto registrado correctamente.")
        return True

    def buscar_producto(self, codigo: int) -> Producto | None:

        return self.productos_por_codigo.get(codigo)

    def actualizar_producto(
        self,
        codigo: int,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return False

        if nombre.strip() == "":
            print("El nombre no puede estar vacío.")
            return False

        if categoria.strip() == "":
            print("La categoría no puede estar vacía.")
            return False

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio

        # Actualizar las categorías disponibles
        self.categorias = {
            producto.categoria
            for producto in self.productos
        }

        print("Producto actualizado correctamente.")
        return True

    def eliminar_producto(self, codigo: int) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return False

        self.productos.remove(producto)

        del self.productos_por_codigo[codigo]

        # Actualizar categorías únicas
        self.categorias = {
            producto.categoria
            for producto in self.productos
        }

        print("Producto eliminado correctamente.")
        return True

    def listar_productos(self) -> None:

        if not self.productos:
            print("No existen productos registrados.")
            return

        print("\n========== PRODUCTOS ==========")

        for producto in self.productos:
            producto.mostrar_informacion()

    def registrar_usuario(self, usuario: Usuario) -> bool:

        for usuario_registrado in self.usuarios:

            if usuario_registrado.identificacion == usuario.identificacion:
                print("Error: esa identificación ya está registrada.")
                return False

        self.usuarios.append(usuario)

        print("Usuario registrado correctamente.")
        return True

    def listar_usuarios(self) -> None:

        if not self.usuarios:
            print("No existen usuarios registrados.")
            return

        print("\n========== USUARIOS ==========")

        for usuario in self.usuarios:
            usuario.mostrar_informacion()

    def mostrar_categorias(self) -> None:

        if not self.categorias:
            print("No existen categorías registradas.")
            return

        print("\n====== CATEGORÍAS ======")

        for categoria in sorted(self.categorias):
            print(f"- {categoria}")
            