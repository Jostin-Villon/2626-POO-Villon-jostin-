from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante()

while True:

    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        disponible = input("Disponible (si/no): ").lower() == "si"

        try:
            producto = Producto(nombre, categoria, precio, disponible)
            restaurante.registrar_producto(producto)
            print("Producto registrado correctamente.")

        except ValueError as error:
            print(error)

    elif opcion == "2":

        restaurante.listar_productos()

    elif opcion == "3":

        nombre = input("Ingrese el nombre del producto: ")
        restaurante.buscar_producto(nombre)

    elif opcion == "4":

        id_cliente = int(input("ID: "))
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        cliente = Cliente(id_cliente, nombre, correo)

        restaurante.registrar_cliente(cliente)

        print("Cliente registrado correctamente.")

    elif opcion == "5":

        restaurante.listar_clientes()

    elif opcion == "6":

        nombre = input("Ingrese el nombre del cliente: ")
        restaurante.buscar_cliente(nombre)

    elif opcion == "7":

        print("Programa finalizado.")
        break

    else:

        print("Opción inválida.")
        