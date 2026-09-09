class Usuario:
    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        contrasena: str
    ):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

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

        if not self.contrasena.strip():
            raise ValueError(
                "La contraseña no puede estar vacía."
            )

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            datos["identificacion"],
            datos["nombre"],
            datos["correo"],
            datos["contrasena"]
        )

    def validar_contrasena(self, contrasena: str) -> bool:
        return self.contrasena == contrasena

    def mostrar_informacion(self) -> str:
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}"
        )
    