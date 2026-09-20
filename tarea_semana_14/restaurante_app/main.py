import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView 


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App")
        self.root.geometry("900x650")

        self.archivo_servicio = ArchivoServicio()

        productos = self.archivo_servicio.cargar_productos()
        usuarios = self.archivo_servicio.cargar_usuarios()

        self.restaurante_servicio = RestauranteServicio(
            productos,
            usuarios,
            self.archivo_servicio
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
            self.mostrar_main_view
        )

    def mostrar_main_view(self, usuario):
        self.limpiar_ventana()

        MainView(
            self.root,
            self.restaurante_servicio,
            usuario,
            self.mostrar_login
        )


root = tk.Tk()
app = Aplicacion(root)
root.mainloop()

    