class Usuario:
    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

        self._validar_datos()

    def _validar_datos(self) -> None:
        if not self.identificacion.strip():
            raise ValueError(
                "La identificación no puede estar vacía."
            )

        if not self.nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not self.correo.strip():
            raise ValueError(
                "El correo no puede estar vacío."
            )

    def convertir_a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    def mostrar_informacion(self) -> None:
        print("----------------------------------------")
        print(f"Identificación: {self.identificacion}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        