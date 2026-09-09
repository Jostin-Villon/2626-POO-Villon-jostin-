import os
import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio

from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion:
    def __init__(self, root: tk.Tk):
        self.root = root

        self.root.title(
            "Restaurante App"
        )

        self.root.geometry(
            "900x600"
        )

        self.root.minsize(
            700,
            500
        )

        self.root.configure(
            bg="#f2f4f7"
        )

        carpeta_principal = os.path.dirname(
            os.path.abspath(__file__)
        )

        carpeta_datos = os.path.join(
            carpeta_principal,
            "datos"
        )

        self.archivo_servicio = ArchivoServicio(
            carpeta_datos
        )

        productos = (
            self.archivo_servicio.cargar_productos()
        )

        usuarios = (
            self.archivo_servicio.cargar_usuarios()
        )

        self.restaurante_servicio = RestauranteServicio(
            productos,
            usuarios
        )

        self.mostrar_login()

    def limpiar_ventana(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_login(self) -> None:
        self.limpiar_ventana()

        LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_main_view
        )

    def mostrar_main_view(self, usuario_actual) -> None:
        self.limpiar_ventana()

        MainView(
            self.root,
            self.restaurante_servicio,
            usuario_actual,
            self.mostrar_login
        )


def ejecutar_aplicacion() -> None:
    root = tk.Tk()

    Aplicacion(root)

    root.mainloop()


if __name__ == "__main__":
    ejecutar_aplicacion()
    