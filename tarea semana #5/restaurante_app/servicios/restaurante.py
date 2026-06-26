class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n===== PRODUCTOS REGISTRADOS =====")
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        print("\n===== CLIENTES REGISTRADOS =====")
        for cliente in self.clientes:
            print(cliente)
            
