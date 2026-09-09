from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    def __init__(
        self,
        productos: list[Producto],
        usuarios: list[Usuario]
    ):
        self._productos = productos
        self._usuarios = usuarios

    def validar_acceso(
        self,
        identificacion: str,
        contrasena: str
    ) -> Usuario | None:

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                if usuario.validar_contrasena(contrasena):
                    return usuario

                return None

        return None

    def listar_productos(self) -> list[Producto]:
        return self._productos

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def cantidad_productos(self) -> int:
        return len(self._productos)

    def cantidad_usuarios(self) -> int:
        return len(self._usuarios)

    def obtener_resumen(self) -> str:
        return (
            f"Productos registrados: "
            f"{self.cantidad_productos()}\n"
            f"Usuarios registrados: "
            f"{self.cantidad_usuarios()}"
        )
    