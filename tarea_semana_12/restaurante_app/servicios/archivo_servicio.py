import json

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class ArchivoServicio:

    def __init__(self, carpeta_datos: str):

        self.carpeta_datos = carpeta_datos

        self.ruta_productos = (
            f"{carpeta_datos}/productos.json"
        )

        self.ruta_usuarios = (
            f"{carpeta_datos}/usuarios.json"
        )

        self.ruta_ventas = (
            f"{carpeta_datos}/ventas.json"
        )

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> bool:

        datos = []

        for producto in productos:
            datos.append(
                producto.convertir_a_diccionario()
            )

        try:
            with open(
                self.ruta_productos,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except PermissionError:
            print(
                "Error: no hay permisos para guardar productos."
            )
            return False

        except OSError as error:
            print(
                f"Error al guardar productos: {error}"
            )
            return False

    def cargar_productos(self) -> list[Producto]:

        try:
            with open(
                self.ruta_productos,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: productos.json contiene JSON inválido."
            )
            return []

        except PermissionError:
            print(
                "Error: no hay permisos para leer productos."
            )
            return []

        productos: list[Producto] = []

        for dato in datos:

            try:
                producto = Producto(
                    dato["codigo"],
                    dato["nombre"],
                    dato["categoria"],
                    float(dato["precio"]),
                    int(dato["stock"])
                )

                productos.append(producto)

            except KeyError as error:
                print(
                    f"Error: falta la clave {error} en productos.json."
                )

            except ValueError as error:
                print(
                    f"Error en producto: {error}"
                )

        return productos

    def guardar_usuarios(
        self,
        usuarios: list[Usuario]
    ) -> bool:

        datos = []

        for usuario in usuarios:
            datos.append(
                usuario.convertir_a_diccionario()
            )

        try:
            with open(
                self.ruta_usuarios,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except PermissionError:
            print(
                "Error: no hay permisos para guardar usuarios."
            )
            return False

        except OSError as error:
            print(
                f"Error al guardar usuarios: {error}"
            )
            return False

    def cargar_usuarios(self) -> list[Usuario]:

        try:
            with open(
                self.ruta_usuarios,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: usuarios.json contiene JSON inválido."
            )
            return []

        except PermissionError:
            print(
                "Error: no hay permisos para leer usuarios."
            )
            return []

        usuarios: list[Usuario] = []

        for dato in datos:

            try:
                usuario = Usuario(
                    dato["identificacion"],
                    dato["nombre"],
                    dato["correo"]
                )

                usuarios.append(usuario)

            except KeyError as error:
                print(
                    f"Error: falta la clave {error} en usuarios.json."
                )

            except ValueError as error:
                print(
                    f"Error en usuario: {error}"
                )

        return usuarios

    def guardar_ventas(
        self,
        ventas: list[Venta]
    ) -> bool:

        datos = []

        for venta in ventas:
            datos.append(
                venta.convertir_a_diccionario()
            )

        try:
            with open(
                self.ruta_ventas,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except PermissionError:
            print(
                "Error: no hay permisos para guardar ventas."
            )
            return False

        except OSError as error:
            print(
                f"Error al guardar ventas: {error}"
            )
            return False

    def cargar_ventas(self) -> list[Venta]:

        try:
            with open(
                self.ruta_ventas,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: ventas.json contiene JSON inválido."
            )
            return []

        except PermissionError:
            print(
                "Error: no hay permisos para leer ventas."
            )
            return []

        ventas: list[Venta] = []

        for dato in datos:

            try:
                venta = Venta(
                    dato["usuario_id"],
                    dato["producto_codigo"],
                    int(dato["cantidad"])
                )

                ventas.append(venta)

            except KeyError as error:
                print(
                    f"Error: falta la clave {error} en ventas.json."
                )

            except ValueError as error:
                print(
                    f"Error en venta: {error}"
                )
        return ventas
    