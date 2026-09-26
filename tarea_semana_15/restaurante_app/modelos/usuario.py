class Usuario:
    def __init__(self, identificacion, nombre, correo, contrasena):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["identificacion"],
            datos["nombre"],
            datos["correo"],
            datos["contrasena"]
        )

    def validar_contrasena(self, contrasena):
        return self.contrasena == contrasena

    def mostrar_informacion(self):
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}"
        )
        