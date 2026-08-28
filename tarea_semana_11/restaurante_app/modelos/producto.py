class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

        self._validar_datos()

    def _validar_datos(self) -> None:
        if not self.codigo.strip():
            raise ValueError("El código no puede estar vacío.")

        if not self.nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not self.categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        if self.precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo.")

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        if cantidad > self.stock:
            raise ValueError(
                "No existe suficiente stock disponible."
            )

        self.stock -= cantidad

    def convertir_a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    def mostrar_informacion(self) -> None:
        print("----------------------------------------")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Stock: {self.stock}")
        