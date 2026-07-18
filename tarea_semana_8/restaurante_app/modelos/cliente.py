class Cliente:

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ):

        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self):

        print("----------------------------")
        print(f"Identificación: {self.identificacion}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        