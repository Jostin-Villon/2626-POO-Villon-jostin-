import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    def __init__(self):
        self.ruta_datos = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "datos"
        )

    def cargar_productos(self):
        ruta = os.path.join(self.ruta_datos, "productos.json")

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            return [
                Producto.desde_diccionario(producto)
                for producto in datos
            ]

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def guardar_productos(self, productos):
        ruta = os.path.join(self.ruta_datos, "productos.json")

        datos = [
            producto.to_dict()
            for producto in productos
        ]

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar_usuarios(self):
        ruta = os.path.join(self.ruta_datos, "usuarios.json")

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            return [
                Usuario.desde_diccionario(usuario)
                for usuario in datos
            ]

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def cargar_ventas(self):
        ruta = os.path.join(self.ruta_datos, "ventas.json")

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            return [
                Venta.desde_diccionario(venta)
                for venta in datos
            ]

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def guardar_ventas(self, ventas):
        ruta = os.path.join(self.ruta_datos, "ventas.json")

        datos = [
            venta.to_dict()
            for venta in ventas
        ]

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
            