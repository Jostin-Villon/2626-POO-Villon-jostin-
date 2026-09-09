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

        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo.")

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            float(datos["precio"]),
            int(datos["stock"])
        )

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Stock: {self.stock}"
        )
        