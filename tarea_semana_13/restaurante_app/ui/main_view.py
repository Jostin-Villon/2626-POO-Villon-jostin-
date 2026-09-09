import tkinter as tk
from tkinter import messagebox


class MainView:
    def __init__(
        self,
        root: tk.Tk,
        restaurante_servicio,
        usuario_actual,
        cerrar_sesion
    ):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.cerrar_sesion = cerrar_sesion

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
        encabezado = tk.Frame(
            self.frame,
            bg="#1d4ed8",
            height=80
        )

        encabezado.pack(
            fill="x"
        )

        encabezado.pack_propagate(False)

        titulo = tk.Label(
            encabezado,
            text="Restaurante App",
            font=("Arial", 20, "bold"),
            bg="#1d4ed8",
            fg="white"
        )

        titulo.pack(
            side="left",
            padx=25
        )

        boton_cerrar = tk.Button(
            encabezado,
            text="Cerrar sesión",
            command=self.cerrar_sesion,
            bg="#dc2626",
            fg="white",
            activebackground="#b91c1c",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )

        boton_cerrar.pack(
            side="right",
            padx=25
        )

        contenido = tk.Frame(
            self.frame,
            bg="#f2f4f7",
            padx=25,
            pady=25
        )

        contenido.pack(
            fill="both",
            expand=True
        )

        bienvenida = tk.Label(
            contenido,
            text=(
                f"Bienvenido, "
                f"{self.usuario_actual.nombre}"
            ),
            font=("Arial", 18, "bold"),
            bg="#f2f4f7",
            fg="#1f2937"
        )

        bienvenida.pack(
            anchor="w",
            pady=(0, 5)
        )

        resumen = tk.Label(
            contenido,
            text=self.restaurante_servicio.obtener_resumen(),
            font=("Arial", 11),
            bg="#f2f4f7",
            fg="#6b7280",
            justify="left"
        )

        resumen.pack(
            anchor="w",
            pady=(0, 20)
        )

        botones = tk.Frame(
            contenido,
            bg="#f2f4f7"
        )

        botones.pack(
            fill="x",
            pady=(0, 15)
        )

        boton_productos = tk.Button(
            botones,
            text="Productos",
            command=self.mostrar_productos,
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            width=18,
            cursor="hand2"
        )

        boton_productos.pack(
            side="left",
            padx=(0, 10)
        )

        boton_usuarios = tk.Button(
            botones,
            text="Usuarios",
            command=self.mostrar_usuarios,
            bg="#16a34a",
            fg="white",
            activebackground="#15803d",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            width=18,
            cursor="hand2"
        )

        boton_usuarios.pack(
            side="left",
            padx=10
        )

        boton_ventas = tk.Button(
            botones,
            text="Ventas",
            command=self.mostrar_ventas_pendientes,
            bg="#9ca3af",
            fg="white",
            activebackground="#6b7280",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            width=18,
            cursor="hand2"
        )

        boton_ventas.pack(
            side="left",
            padx=10
        )

        self.area_resultados = tk.Text(
            contenido,
            height=18,
            width=80,
            font=("Consolas", 10),
            state="disabled",
            bg="white",
            fg="#1f2937",
            wrap="word"
        )

        self.area_resultados.pack(
            fill="both",
            expand=True
        )

    def escribir_resultado(self, texto: str) -> None:
        self.area_resultados.config(
            state="normal"
        )

        self.area_resultados.delete(
            "1.0",
            tk.END
        )

        self.area_resultados.insert(
            tk.END,
            texto
        )

        self.area_resultados.config(
            state="disabled"
        )

    def mostrar_productos(self) -> None:
        productos = (
            self.restaurante_servicio.listar_productos()
        )

        if not productos:
            self.escribir_resultado(
                "No hay productos registrados."
            )
            return

        texto = "========== PRODUCTOS ==========\n\n"

        for producto in productos:
            texto += producto.mostrar_informacion()
            texto += "\n\n"

        self.escribir_resultado(texto)

    def mostrar_usuarios(self) -> None:
        usuarios = (
            self.restaurante_servicio.listar_usuarios()
        )

        if not usuarios:
            self.escribir_resultado(
                "No hay usuarios registrados."
            )
            return

        texto = "========== USUARIOS ==========\n\n"

        for usuario in usuarios:
            texto += usuario.mostrar_informacion()
            texto += "\n\n"

        self.escribir_resultado(texto)

    def mostrar_ventas_pendientes(self) -> None:
        self.escribir_resultado(
            "La funcionalidad de Ventas se incorporará "
            "en una semana posterior."
        )
        
