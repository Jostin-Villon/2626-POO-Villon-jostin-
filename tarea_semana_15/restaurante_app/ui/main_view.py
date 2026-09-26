import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(self, root, servicio, cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.cerrar_sesion = cerrar_sesion

        self.limpiar_ventana()
        self.crear_interfaz()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def crear_interfaz(self):

        titulo = ttk.Label(
            self.root,
            text="SISTEMA DE RESTAURANTE",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=15)

        contenedor = ttk.Frame(self.root)
        contenedor.pack(pady=10)

        ttk.Button(
            contenedor,
            text="Usuarios",
            command=self.mostrar_usuarios
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            contenedor,
            text="Productos",
            command=self.mostrar_productos
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            contenedor,
            text="Ventas",
            command=self.mostrar_ventas
        ).grid(row=0, column=2, padx=5)

        ttk.Button(
            contenedor,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        ).grid(row=0, column=3, padx=5)

        self.contenido = ttk.Frame(self.root)
        self.contenido.pack(fill="both", expand=True, padx=20, pady=10)

        self.mostrar_productos()

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_productos(self):
        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="PRODUCTOS",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        tabla = ttk.Treeview(
            self.contenido,
            columns=("codigo", "nombre", "categoria", "precio", "stock"),
            show="headings"
        )

        for columna in ("codigo", "nombre", "categoria", "precio", "stock"):
            tabla.heading(columna, text=columna.capitalize())

        for producto in self.servicio.listar_productos():
            tabla.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    producto.precio,
                    producto.stock
                )
            )

        tabla.pack(fill="both", expand=True)

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="USUARIOS",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        tabla = ttk.Treeview(
            self.contenido,
            columns=("identificacion", "nombre", "correo"),
            show="headings"
        )

        for columna in ("identificacion", "nombre", "correo"):
            tabla.heading(columna, text=columna.capitalize())

        for usuario in self.servicio.listar_usuarios():
            tabla.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.correo
                )
            )

        tabla.pack(fill="both", expand=True)

    def mostrar_ventas(self):
        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="REGISTRAR VENTA",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        formulario = ttk.Frame(self.contenido)
        formulario.pack(pady=10)

        ttk.Label(formulario, text="Usuario:").grid(
            row=0, column=0, padx=5, pady=5
        )

        usuarios = self.servicio.listar_usuarios()

        self.usuario_combo = ttk.Combobox(
            formulario,
            state="readonly",
            values=[
                f"{usuario.identificacion} - {usuario.nombre}"
                for usuario in usuarios
            ]
        )
        self.usuario_combo.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(formulario, text="Producto:").grid(
            row=1, column=0, padx=5, pady=5
        )

        productos = self.servicio.listar_productos()

        self.producto_combo = ttk.Combobox(
            formulario,
            state="readonly",
            values=[
                f"{producto.codigo} - {producto.nombre}"
                for producto in productos
            ]
        )
        self.producto_combo.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(formulario, text="Cantidad:").grid(
            row=2, column=0, padx=5, pady=5
        )

        self.cantidad_entry = ttk.Entry(formulario)
        self.cantidad_entry.grid(
            row=2, column=1, padx=5, pady=5
        )

        ttk.Button(
            formulario,
            text="Registrar venta",
            command=self.registrar_venta
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10
        )

        self.tabla_ventas = ttk.Treeview(
            self.contenido,
            columns=("usuario", "producto", "cantidad", "fecha"),
            show="headings"
        )

        for columna in ("usuario", "producto", "cantidad", "fecha"):
            self.tabla_ventas.heading(
                columna,
                text=columna.capitalize()
            )

        self.tabla_ventas.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.actualizar_ventas()

    def registrar_venta(self):
        usuario = self.usuario_combo.get()
        producto = self.producto_combo.get()
        cantidad_texto = self.cantidad_entry.get()

        if not usuario or not producto or not cantidad_texto:
            messagebox.showwarning(
                "Aviso",
                "Complete todos los campos."
            )
            return

        try:
            cantidad = int(cantidad_texto)
        except ValueError:
            messagebox.showerror(
                "Error",
                "La cantidad debe ser un número."
            )
            return

        identificacion = usuario.split(" - ")[0]
        codigo = producto.split(" - ")[0]

        resultado, mensaje = self.servicio.registrar_venta(
            identificacion,
            codigo,
            cantidad
        )

        if resultado:
            messagebox.showinfo(
                "Venta",
                mensaje
            )

            self.cantidad_entry.delete(0, tk.END)
            self.actualizar_ventas()
            self.mostrar_ventas()

        else:
            messagebox.showerror(
                "Venta",
                mensaje
            )

    def actualizar_ventas(self):
        if not hasattr(self, "tabla_ventas"):
            return

        for elemento in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(elemento)

        productos = {
            producto.codigo: producto.nombre
            for producto in self.servicio.listar_productos()
        }

        for venta in self.servicio.listar_ventas():
            nombre_producto = productos.get(
                venta.producto_codigo,
                venta.producto_codigo
            )

            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    venta.usuario_id,
                    nombre_producto,
                    venta.cantidad,
                    venta.fecha
                )
            )
            