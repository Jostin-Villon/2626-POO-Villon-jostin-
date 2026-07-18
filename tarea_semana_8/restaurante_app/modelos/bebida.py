from modelos.producto import Producto

class Bebida(Producto):

    def __init__(
        self,
        codigo: int,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str
    ):

        super().__init__(codigo, nombre, categoria, precio)

        self.tamano = tamano

    def mostrar_informacion(self):

        print("----------------------------")
        print("BEBIDA")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio}")
        print(f"Tamaño: {self.tamano}")
        