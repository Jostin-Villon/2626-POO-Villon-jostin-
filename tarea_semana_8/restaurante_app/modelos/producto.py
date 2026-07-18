class Producto:

    def __init__(self, codigo: int, nombre: str, categoria: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):

        print("----------------------------")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio}")
        