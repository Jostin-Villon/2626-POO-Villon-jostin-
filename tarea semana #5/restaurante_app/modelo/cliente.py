class Cliente:
    def __init__(self, nombre: str, edad: int, telefono: str, activo: bool):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.activo = activo

    def __str__(self):
        return f"Cliente: {self.nombre} | Edad: {self.edad} | Teléfono: {self.telefono} | Activo: {self.activo}"
    