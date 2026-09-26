from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:

    def __init__(self, productos, usuarios):
        self.productos = productos
        self.usuarios = usuarios

    def validar_acceso(self, identificacion: str, contrasena: str):
        for usuario in self.usuarios:
            if (
                usuario.identificacion == identificacion
                and usuario.contrasena == contrasena
            ):
                return usuario

        return None

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios

    def buscar_producto(self, codigo: str):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def buscar_usuario(self, identificacion: str):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None
        
    
