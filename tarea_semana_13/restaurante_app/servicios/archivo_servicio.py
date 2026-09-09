import json

from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:
    def __init__(self, carpeta_datos: str):
        self.ruta_productos = (
            f"{carpeta_datos}/productos.json"
        )

        self.ruta_usuarios = (
            f"{carpeta_datos}/usuarios.json"
        )

    def cargar_productos(self) -> list[Producto]:
        try:
            with open(
                self.ruta_productos,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

        except FileNotFoundError:
            print("Advertencia: no se encontró productos.json.")
            return []

        except json.JSONDecodeError:
            print("Error: productos.json tiene un formato inválido.")
            return []

        except PermissionError:
            print("Error: no hay permisos para leer productos.json.")
            return []

        except OSError as error:
            print(f"Error al leer productos.json: {error}")
            return []

        productos = []

        for dato in datos:
            try:
                producto = Producto.desde_diccionario(dato)
                productos.append(producto)

            except KeyError as error:
                print(
                    f"Error: falta la clave {error} en productos.json."
                )

            except ValueError as error:
                print(f"Error en los datos del producto: {error}")

        return productos

    def cargar_usuarios(self) -> list[Usuario]:
        try:
            with open(
                self.ruta_usuarios,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

        except FileNotFoundError:
            print("Advertencia: no se encontró usuarios.json.")
            return []

        except json.JSONDecodeError:
            print("Error: usuarios.json tiene un formato inválido.")
            return []

        except PermissionError:
            print("Error: no hay permisos para leer usuarios.json.")
            return []

        except OSError as error:
            print(f"Error al leer usuarios.json: {error}")
            return []

        usuarios = []

        for dato in datos:
            try:
                usuario = Usuario.desde_diccionario(dato)
                usuarios.append(usuario)

            except KeyError as error:
                print(
                    f"Error: falta la clave {error} en usuarios.json."
                )

            except ValueError as error:
                print(f"Error en los datos del usuario: {error}")

        return usuarios
    