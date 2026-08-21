# Clase que representa un producto del restaurante

class Producto:

    def __init__(
        self,
        codigo: int,
        nombre: str,
        categoria: str,
        precio: float
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

        self._validar_datos()

    def _validar_datos(self) -> None:
        """Valida los datos del producto."""

        if self.nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío.")

        if self.categoria.strip() == "":
            raise ValueError("La categoría no puede estar vacía.")

        if self.precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

    def mostrar_informacion(self) -> None:
        """Muestra la información del producto."""

        print("----------------------------------------")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio:.2f}")

    def convertir_a_diccionario(self) -> dict:
        """Convierte el producto en un diccionario para JSON."""

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }
    