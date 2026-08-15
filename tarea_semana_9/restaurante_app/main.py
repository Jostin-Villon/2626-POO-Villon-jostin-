from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

OPCIONES_MENU = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías",
    "Salir"
)

def mostrar_menu() -> None:
    """Muestra las opciones disponibles del sistema."""

    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")

    for numero, opcion in enumerate(OPCIONES_MENU, start=1):
        print(f"{numero}. {opcion}")

def registrar_producto(restaurante: Restaurante) -> None:
    """Solicita los datos y registra un producto."""

    try:
        codigo = int(input("Código del producto: "))
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))

        if nombre.strip() == "":
            print("El nombre no puede estar vacío.")
            return

        if categoria.strip() == "":
            print("La categoría no puede estar vacía.")
            return

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            return

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        restaurante.registrar_producto(producto)

    except ValueError:
        print("Error: ingrese datos válidos.")

def buscar_producto(restaurante: Restaurante) -> None:
    """Busca un producto utilizando su código."""

    try:
        codigo = int(input("Ingrese el código del producto: "))

        producto = restaurante.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
        else:
            print("\nProducto encontrado:")
            producto.mostrar_informacion()

    except ValueError:
        print("Error: el código debe ser un número.")

def actualizar_producto(restaurante: Restaurante) -> None:
    """Solicita nuevos datos para actualizar un producto."""

    try:
        codigo = int(input("Código del producto a actualizar: "))

        producto = restaurante.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return

        print("\nDatos actuales:")
        producto.mostrar_informacion()

        nombre = input("Nuevo nombre: ")
        categoria = input("Nueva categoría: ")
        precio = float(input("Nuevo precio: "))

        restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio
        )

    except ValueError:
        print("Error: ingrese datos válidos.")

def eliminar_producto(restaurante: Restaurante) -> None:
    """Elimina un producto utilizando su código."""

    try:
        codigo = int(input("Código del producto a eliminar: "))

        restaurante.eliminar_producto(codigo)

    except ValueError:
        print("Error: el código debe ser un número.")

def listar_productos(restaurante: Restaurante) -> None:
    """Muestra todos los productos registrados."""

    restaurante.listar_productos()

def registrar_usuario(restaurante: Restaurante) -> None:
    """Solicita los datos y registra un usuario."""

    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    if identificacion.strip() == "":
        print("La identificación no puede estar vacía.")
        return

    if nombre.strip() == "":
        print("El nombre no puede estar vacío.")
        return

    if correo.strip() == "":
        print("El correo no puede estar vacío.")
        return

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    restaurante.registrar_usuario(usuario)

def listar_usuarios(restaurante: Restaurante) -> None:
    """Muestra todos los usuarios registrados."""

    restaurante.listar_usuarios()

def mostrar_categorias(restaurante: Restaurante) -> None:
    """Muestra las categorías registradas sin repetir."""

    restaurante.mostrar_categorias()

def ejecutar_programa() -> None:
    """Ejecuta el menú principal del sistema."""

    restaurante = Restaurante()
    acciones_menu: dict[str, callable] = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias
    }

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "9":
            print("\nPrograma finalizado.")
            break

        accion = acciones_menu.get(opcion)

        if accion is not None:
            accion(restaurante)
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_programa()
    