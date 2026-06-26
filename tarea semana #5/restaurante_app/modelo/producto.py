class Producto:
    def __init__(self, nombre: str, precio: float, stock: int, disponible: bool):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.disponible = disponible

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock} | Disponible: {self.disponible}"
    