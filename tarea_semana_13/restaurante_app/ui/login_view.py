import tkinter as tk
from tkinter import messagebox


class LoginView:
    def __init__(
        self,
        root: tk.Tk,
        restaurante_servicio,
        mostrar_main_view
    ):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_main_view = mostrar_main_view

        self.frame = tk.Frame(
            self.root,
            bg="#f2f4f7"
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.crear_interfaz()

    def crear_interfaz(self) -> None:
        contenedor = tk.Frame(
            self.frame,
            bg="white",
            padx=35,
            pady=35
        )

        contenedor.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        titulo = tk.Label(
            contenedor,
            text="Restaurante App",
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#1f2937"
        )

        titulo.pack(pady=(0, 8))

        subtitulo = tk.Label(
            contenedor,
            text="Inicio de sesión",
            font=("Arial", 12),
            bg="white",
            fg="#6b7280"
        )

        subtitulo.pack(pady=(0, 25))

        etiqueta_usuario = tk.Label(
            contenedor,
            text="Identificación",
            font=("Arial", 11),
            bg="white",
            anchor="w"
        )

        etiqueta_usuario.pack(
            fill="x",
            pady=(0, 5)
        )

        self.entrada_usuario = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11)
        )

        self.entrada_usuario.pack(
            ipady=7,
            pady=(0, 15)
        )

        etiqueta_contrasena = tk.Label(
            contenedor,
            text="Contraseña",
            font=("Arial", 11),
            bg="white",
            anchor="w"
        )

        etiqueta_contrasena.pack(
            fill="x",
            pady=(0, 5)
        )

        self.entrada_contrasena = tk.Entry(
            contenedor,
            width=30,
            show="*",
            font=("Arial", 11)
        )

        self.entrada_contrasena.pack(
            ipady=7,
            pady=(0, 20)
        )

        boton_ingresar = tk.Button(
            contenedor,
            text="Ingresar",
            command=self.ingresar,
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            width=25,
            cursor="hand2"
        )

        boton_ingresar.pack(
            pady=(0, 10)
        )

        self.mensaje = tk.Label(
            contenedor,
            text="",
            font=("Arial", 10),
            bg="white",
            fg="#dc2626"
        )

        self.mensaje.pack()

        self.entrada_usuario.focus()

        self.root.bind(
            "<Return>",
            lambda evento: self.ingresar()
        )

    def ingresar(self) -> None:
        identificacion = self.entrada_usuario.get().strip()
        contrasena = self.entrada_contrasena.get().strip()

        if not identificacion or not contrasena:
            self.mensaje.config(
                text="Debe completar todos los campos.",
                fg="#e71d1d"
            )
            return

        usuario = self.restaurante_servicio.validar_acceso(
            identificacion,
            contrasena
        )

        if usuario is None:
            self.mensaje.config(
                text="Credenciales incorrectas.",
                fg="#dc2626"
            )
            return

        self.mensaje.config(
            text="Acceso correcto.",
            fg="#15803d"
        )

        self.frame.destroy()

        self.mostrar_main_view(usuario)
        
        

