# Clase que administra la lista de productos

class Restaurante:

    def __init__(self):

        self.productos = []

    def agregar_producto(self, producto):

        self.productos.append(producto)

    def mostrar_productos(self):

        print("\n========== PRODUCTOS ==========\n")

        for producto in self.productos:

            # Polimorfismo
            producto.mostrar_informacion()

            print("----------------------")