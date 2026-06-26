from modelo.producto import Producto
from modelo.cliente import Cliente
from servicios.restaurante import Restaurante

producto1 = Producto("Pizza Familiar", 12.50, 20, True)
producto2 = Producto("Hamburguesa", 6.75, 15, True)

cliente1 = Cliente("Jostin villón", 19, "0984756935", True)
cliente2 = Cliente("Erika Lorena", 40, "0974637649", True)

mi_restaurante = Restaurante()

mi_restaurante.agregar_producto(producto1)
mi_restaurante.agregar_producto(producto2)

mi_restaurante.agregar_cliente(cliente1)
mi_restaurante.agregar_cliente(cliente2)

mi_restaurante.mostrar_productos()
mi_restaurante.mostrar_clientes()
