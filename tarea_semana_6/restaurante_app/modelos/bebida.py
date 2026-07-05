from modelos.producto import Producto
# Clase hija 2
class Bebida(Producto):

    def __init__(self, nombre: str, precio: float, disponible: bool, volumen: int):

        super().__init__(nombre, precio, disponible)

        self.volumen = volumen
    # Polimorfismo    
    def mostrar_informacion(self):

        print("===== BEBIDA =====")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio()}")
        print(f"Volumen: {self.volumen} ml")
        print(f"Disponible: {self.disponible}")