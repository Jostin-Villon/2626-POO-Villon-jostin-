import tkinter as tk


class LoginView:
    def __init__(self, root, restaurante_servicio, mostrar_main_view):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_main_view = mostrar_main_view

        self.frame = tk.Frame(root, padx=40, pady=40)
        self.frame.pack(expand=True)

        tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        tk.Label(self.frame, text="Identificación").pack()
        self.entrada_usuario = tk.Entry(self.frame, width=30)
        self.entrada_usuario.pack(pady=5)

        tk.Label(self.frame, text="Contraseña").pack()
        self.entrada_contrasena = tk.Entry(
            self.frame,
            width=30,
            show="*"
        )
        self.entrada_contrasena.pack(pady=5)

        tk.Button(
            self.frame,
            text="Ingresar",
            command=self.ingresar,
            width=20
        ).pack(pady=15)

        self.mensaje = tk.Label(
            self.frame,
            text="",
            fg="red"
        )
        self.mensaje.pack()

    def ingresar(self):
        identificacion = self.entrada_usuario.get().strip()
        contrasena = self.entrada_contrasena.get().strip()

        if not identificacion or not contrasena:
            self.mensaje.config(text="Complete todos los campos.")
            return

        usuario = self.restaurante_servicio.validar_acceso(
            identificacion,
            contrasena
        )

        if usuario is None:
            self.mensaje.config(text="Credenciales incorrectas.")
            return

        self.frame.destroy()
        self.mostrar_main_view(usuario)
        
        

