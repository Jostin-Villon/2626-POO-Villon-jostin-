class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.stock = int(stock)

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["stock"]
        )

    def mostrar_informacion(self):
        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Stock: {self.stock}"
        )

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }
