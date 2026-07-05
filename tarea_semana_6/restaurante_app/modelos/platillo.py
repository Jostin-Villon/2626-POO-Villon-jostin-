from modelos.producto import Producto
# Clase hija 1
class Platillo(Producto):

    def __init__(self, nombre: str, precio: float, disponible: bool, calorias: int):

        super().__init__(nombre, precio, disponible)

        self.calorias = calorias

    # Polimorfismo
    def mostrar_informacion(self):

        print("===== PLATILLO =====")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio()}")
        print(f"Calorías: {self.calorias}")
        print(f"Disponible: {self.disponible}")