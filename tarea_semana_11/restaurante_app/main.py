import os

from modelos.producto import Producto
from modelos.usuario import Usuario

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


def registrar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n========== REGISTRAR PRODUCTO ==========")

    try:
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        if restaurante.registrar_producto(producto):
            archivo_servicio.guardar_productos(
                restaurante.productos
            )

    except ValueError as error:
        print(f"Error: {error}")


def listar_productos(
    restaurante: Restaurante
) -> None:

    restaurante.listar_productos()


def registrar_usuario(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n========== REGISTRAR USUARIO ==========")

    try:
        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        usuario = Usuario(
            identificacion,
            nombre,
            correo
        )

        if restaurante.registrar_usuario(usuario):
            archivo_servicio.guardar_usuarios(
                restaurante.usuarios
            )

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(
    restaurante: Restaurante
) -> None:

    restaurante.listar_usuarios()


def realizar_venta(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n========== REALIZAR VENTA ==========")

    codigo_producto = input(
        "Código del producto: "
    )

    identificacion_usuario = input(
        "Identificación del usuario: "
    )

    try:
        cantidad = int(
            input("Cantidad: ")
        )

        venta_realizada = restaurante.vender_producto(
            codigo_producto,
            identificacion_usuario,
            cantidad
        )

        if venta_realizada:

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            archivo_servicio.guardar_ventas(
                restaurante.ventas
            )

            print(
                "Información de la venta guardada correctamente."
            )

    except ValueError as error:
        print(f"Error: {error}")


def consultar_ventas_usuario(
    restaurante: Restaurante
) -> None:

    print(
        "\n========== CONSULTAR VENTAS =========="
    )

    identificacion = input(
        "Identificación del usuario: "
    )

    restaurante.listar_ventas_usuario(
        identificacion
    )


def ejecutar_programa() -> None:

    restaurante = Restaurante()

    carpeta_principal = os.path.dirname(
        os.path.abspath(__file__)
    )

    carpeta_datos = os.path.join(
        carpeta_principal,
        "datos"
    )

    archivo_servicio = ArchivoServicio(
        carpeta_datos
    )

    # Recuperar información guardada en JSON.
    productos = archivo_servicio.cargar_productos()
    usuarios = archivo_servicio.cargar_usuarios()
    ventas = archivo_servicio.cargar_ventas()

    restaurante.cargar_productos(productos)
    restaurante.cargar_usuarios(usuarios)
    restaurante.cargar_ventas(ventas)

    while True:

        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("----------------------------------------")
        print("3. Registrar usuario")
        print("4. Listar usuarios")
        print("----------------------------------------")
        print("5. Realizar venta")
        print("6. Consultar ventas de un usuario")
        print("----------------------------------------")
        print("7. Salir")
        print("========================================")

        opcion = input(
            "Seleccione una opción: "
        )

        if opcion == "1":

            registrar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == "2":

            listar_productos(
                restaurante
            )

        elif opcion == "3":

            registrar_usuario(
                restaurante,
                archivo_servicio
            )

        elif opcion == "4":

            listar_usuarios(
                restaurante
            )

        elif opcion == "5":

            realizar_venta(
                restaurante,
                archivo_servicio
            )

        elif opcion == "6":

            consultar_ventas_usuario(
                restaurante
            )

        elif opcion == "7":

            print("\nPrograma finalizado.")
            break

        else:

            print(
                "Opción inválida. Intente nuevamente."
            )


if __name__ == "__main__":
    ejecutar_programa()
    