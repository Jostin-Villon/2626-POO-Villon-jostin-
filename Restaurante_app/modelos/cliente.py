class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre} | Cédula: {self.cedula} | Teléfono: {self.telefono}"
    