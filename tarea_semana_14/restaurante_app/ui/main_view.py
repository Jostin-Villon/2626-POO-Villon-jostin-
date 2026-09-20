import tkinter as tk
from tkinter import ttk, messagebox


class MainView:
    def __init__(
        self,
        root,
        restaurante_servicio,
        usuario_actual,
        cerrar_sesion
    ):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.cerrar_sesion = cerrar_sesion

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        self.crear_interfaz()

    def crear_interfaz(self):
        encabezado = tk.Frame(self.frame)
        encabezado.pack(fill="x", pady=10)

        tk.Label(
            encabezado,
            text=f"Bienvenido, {self.usuario_actual.nombre}",
            font=("Arial", 18, "bold")
        ).pack(side="left")

        tk.Button(
            encabezado,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        ).pack(side="right")

        navegacion = tk.LabelFrame(
            self.frame,
            text="Navegación",
            padx=10,
            pady=10
        )
        navegacion.pack(fill="x", pady=10)

        tk.Button(
            navegacion,
            text="Productos",
            command=self.mostrar_productos
        ).pack(side="left", padx=5)

        tk.Button(
            navegacion,
            text="Usuarios",
            command=self.mostrar_usuarios
        ).pack(side="left", padx=5)

        tk.Button(
            navegacion,
            text="Ventas",
            command=self.mostrar_ventas
        ).pack(side="left", padx=5)

        formulario = tk.LabelFrame(
            self.frame,
            text="Gestión de productos",
            padx=10,
            pady=10
        )
        formulario.pack(fill="x", pady=10)

        tk.Label(formulario, text="Código").grid(
            row=0, column=0, padx=5, pady=5
        )

        self.codigo = tk.Entry(formulario, width=15)
        self.codigo.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario, text="Nombre").grid(
            row=0, column=2, padx=5, pady=5
        )

        self.nombre = tk.Entry(formulario, width=20)
        self.nombre.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(formulario, text="Categoría").grid(
            row=1, column=0, padx=5, pady=5
        )

        self.categoria = ttk.Combobox(
            formulario,
            values=["Comida", "Bebida", "Postre"],
            state="readonly",
            width=17
        )
        self.categoria.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario, text="Precio").grid(
            row=1, column=2, padx=5, pady=5
        )

        self.precio = tk.Entry(formulario, width=20)
        self.precio.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(formulario, text="Stock").grid(
            row=2, column=0, padx=5, pady=5
        )

        self.stock = tk.Entry(formulario, width=15)
        self.stock.grid(row=2, column=1, padx=5, pady=5)

        botones = tk.Frame(formulario)
        botones.grid(row=2, column=2, columnspan=2, pady=5)

        tk.Button(
            botones,
            text="Registrar",
            command=self.registrar_producto
        ).pack(side="left", padx=3)

        tk.Button(
            botones,
            text="Cargar",
            command=self.cargar_producto
        ).pack(side="left", padx=3)

        tk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar_producto
        ).pack(side="left", padx=3)

        tk.Button(
            botones,
            text="Eliminar",
            command=self.eliminar_producto
        ).pack(side="left", padx=3)

        tk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_formulario
        ).pack(side="left", padx=3)

        tabla_frame = tk.Frame(self.frame)
        tabla_frame.pack(fill="both", expand=True, pady=10)

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "stock"
        )

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("categoria", text="Categoría")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("stock", text="Stock")

        self.tabla.column("codigo", width=100)
        self.tabla.column("nombre", width=180)
        self.tabla.column("categoria", width=120)
        self.tabla.column("precio", width=100)
        self.tabla.column("stock", width=100)

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla.yview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.mostrar_productos()

    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for producto in self.restaurante_servicio.listar_productos():
            self.tabla.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock
                )
            )

    def mostrar_productos(self):
        self.actualizar_tabla()

    def mostrar_usuarios(self):
        usuarios = self.restaurante_servicio.listar_usuarios()

        texto = "USUARIOS REGISTRADOS\n\n"

        for usuario in usuarios:
            texto += usuario.mostrar_informacion()
            texto += "\n\n"

        messagebox.showinfo("Usuarios", texto)

    def mostrar_ventas(self):
        messagebox.showinfo(
            "Ventas",
            "La funcionalidad de Ventas estará disponible en una semana posterior."
        )

    def registrar_producto(self):
        correcto, mensaje = self.restaurante_servicio.registrar_producto(
            self.codigo.get().strip(),
            self.nombre.get().strip(),
            self.categoria.get().strip(),
            self.precio.get().strip(),
            self.stock.get().strip()
        )

        if correcto:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_tabla()
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", mensaje)

    def cargar_producto(self):
        codigo = self.codigo.get().strip()

        producto = self.restaurante_servicio.obtener_producto(codigo)

        if producto is None:
            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )
            return

        self.nombre.delete(0, tk.END)
        self.nombre.insert(0, producto.nombre)

        self.categoria.set(producto.categoria)

        self.precio.delete(0, tk.END)
        self.precio.insert(0, producto.precio)

        self.stock.delete(0, tk.END)
        self.stock.insert(0, producto.stock)

    def actualizar_producto(self):
        correcto, mensaje = self.restaurante_servicio.actualizar_producto(
            self.codigo.get().strip(),
            self.nombre.get().strip(),
            self.categoria.get().strip(),
            self.precio.get().strip(),
            self.stock.get().strip()
        )

        if correcto:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_tabla()
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", mensaje)

    def eliminar_producto(self):
        codigo = self.codigo.get().strip()

        if not codigo:
            messagebox.showerror(
                "Error",
                "Ingrese el código del producto."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            "¿Desea eliminar este producto?"
        )

        if not confirmar:
            return

        correcto, mensaje = self.restaurante_servicio.eliminar_producto(
            codigo
        )

        if correcto:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_tabla()
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", mensaje)

    def limpiar_formulario(self):
        self.codigo.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.categoria.set("")
        self.precio.delete(0, tk.END)
        self.stock.delete(0, tk.END)
        
