class Restaurante:

    def __init__(self):
        self.productos = []
        self.clientes = []

    # Productos

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):

        if len(self.productos) == 0:
            print("No existen productos registrados.")
            return

        for producto in self.productos:
            producto.mostrar_informacion()

    def buscar_producto(self, nombre):

        for producto in self.productos:

            if producto.nombre.lower() == nombre.lower():
                producto.mostrar_informacion()
                return

        print("Producto no encontrado.")

    # Clientes

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):

        if len(self.clientes) == 0:
            print("No existen clientes registrados.")
            return

        for cliente in self.clientes:
            print(cliente)

    def buscar_cliente(self, nombre):

        for cliente in self.clientes:

            if cliente.nombre.lower() == nombre.lower():
                print(cliente)
                return

        print("Cliente no encontrado.")
        