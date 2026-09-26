import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion:

    def __init__(self, root):
        self.root = root
        self.archivo_servicio = ArchivoServicio()

        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()

        self.restaurante_servicio = RestauranteServicio(
            self.productos,
            self.usuarios
        )

        self.mostrar_login()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_login(self):
        self.limpiar_ventana()

        LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_principal
        )

    def mostrar_principal(self):
        self.limpiar_ventana()

        MainView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_login
        )


root = tk.Tk()
root.title("Restaurante App")
root.geometry("900x600")

app = Aplicacion(root)

root.mainloop()

