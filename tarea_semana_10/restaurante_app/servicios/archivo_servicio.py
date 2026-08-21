import json

from modelos.producto import Producto


class ArchivoServicio:

    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> bool:
        """Guarda los productos en productos.json."""

        datos_productos = []

        for producto in productos:
            datos_productos.append(
                {
                    "codigo": producto.codigo,
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "precio": producto.precio
                }
            )

        try:
            with open(
                self.ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos_productos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            print("Productos guardados correctamente.")
            return True

        except PermissionError:
            print("Error: no hay permisos para escribir el archivo.")
            return False

        except OSError as error:
            print(f"Error al guardar los productos: {error}")
            return False

    def cargar_productos(self) -> list[Producto]:
        """Carga los productos desde productos.json."""

        try:
            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos_productos = json.load(archivo)

        except FileNotFoundError:
            print("No existe el archivo de productos.")
            return []

        except json.JSONDecodeError:
            print("Error: productos.json no contiene un JSON válido.")
            return []

        except PermissionError:
            print("Error: no hay permisos para leer el archivo.")
            return []

        productos_cargados = []

        for registro in datos_productos:

            try:
                producto = Producto(
                    registro["codigo"],
                    registro["nombre"],
                    registro["categoria"],
                    registro["precio"]
                )

                productos_cargados.append(producto)

            except KeyError as error:
                print(f"Error: falta el dato {error}.")

            except ValueError as error:
                print(f"Error en los datos del producto: {error}")

        return productos_cargados
    
    
    