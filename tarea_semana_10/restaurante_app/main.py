import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


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
    """Muestra el menú principal."""

    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")

    for numero, opcion in enumerate(OPCIONES_MENU, start=1):
        print(f"{numero}. {opcion}")


def registrar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    try:
        codigo = int(input("Código del producto: "))
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        registrado = restaurante.registrar_producto(producto)

        if registrado:
            guardado = archivo_servicio.guardar_productos(
                restaurante.productos
            )

            if guardado:
                print("Producto guardado en productos.json.")

    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto(
    restaurante: Restaurante
) -> None:

    try:
        codigo = int(input("Ingrese el código del producto: "))

        producto = restaurante.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
        else:
            print("\nProducto encontrado:")
            producto.mostrar_informacion()

    except ValueError:
        print("El código debe ser un número.")


def actualizar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    try:
        codigo = int(
            input("Código del producto a actualizar: ")
        )

        producto = restaurante.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return

        nombre = input("Nuevo nombre: ")
        categoria = input("Nueva categoría: ")
        precio = float(input("Nuevo precio: "))

        actualizado = restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        if actualizado:
            archivo_servicio.guardar_productos(
                restaurante.productos
            )

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    try:
        codigo = int(
            input("Código del producto a eliminar: ")
        )

        eliminado = restaurante.eliminar_producto(codigo)

        if eliminado:
            archivo_servicio.guardar_productos(
                restaurante.productos
            )

    except ValueError:
        print("El código debe ser un número.")


def listar_productos(
    restaurante: Restaurante
) -> None:

    restaurante.listar_productos()


def registrar_usuario(
    restaurante: Restaurante
) -> None:

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


def listar_usuarios(
    restaurante: Restaurante
) -> None:

    restaurante.listar_usuarios()


def mostrar_categorias(
    restaurante: Restaurante
) -> None:

    restaurante.mostrar_categorias()


def ejecutar_programa() -> None:

    restaurante = Restaurante()

    # Obtiene la carpeta donde está main.py
    carpeta_principal = os.path.dirname(
        os.path.abspath(__file__)
    )

    # Construye la ruta correcta de productos.json
    ruta_productos = os.path.join(
        carpeta_principal,
        "datos",
        "productos.json"
    )

    print(f"\nArchivo JSON: {ruta_productos}")

    archivo_servicio = ArchivoServicio(
        ruta_productos
    )

    # Cargar productos guardados
    productos_cargados = archivo_servicio.cargar_productos()

    for producto in productos_cargados:
        restaurante.registrar_producto(
            producto,
            mostrar_mensaje=False
        )

    acciones_menu = {
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

        opcion = input(
            "\nSeleccione una opción: "
        )

        if opcion == "9":
            print("\nPrograma finalizado.")
            break

        accion = acciones_menu.get(opcion)

        if accion is None:
            print("Opción inválida.")
            continue

        if opcion == "1":
            accion(
                restaurante,
                archivo_servicio
            )

        elif opcion == "3":
            accion(
                restaurante,
                archivo_servicio
            )

        elif opcion == "4":
            accion(
                restaurante,
                archivo_servicio
            )

        else:
            accion(restaurante)


if __name__ == "__main__":
    ejecutar_programa()
    