from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante()

while True:

    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        codigo = int(input("Código: "))
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        restaurante.registrar_producto(producto)

    elif opcion == "2":

        codigo = int(input("Código: "))
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        tamano = input("Tamaño: ")

        bebida = Bebida(
            codigo,
            nombre,
            categoria,
            precio,
            tamano
        )

        restaurante.registrar_producto(bebida)

    elif opcion == "3":

        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        cliente = Cliente(
            identificacion,
            nombre,
            correo
        )

        restaurante.registrar_cliente(cliente)

    elif opcion == "4":

        restaurante.listar_productos()

    elif opcion == "5":

        restaurante.listar_clientes()

    elif opcion == "6":

        print("Programa finalizado.")
        break

    else:

        print("Opción inválida.")
        
