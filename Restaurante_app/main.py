from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

producto1 = Producto("Pizza", 8.50, "Comida")
producto2 = Producto("Hamburguesa", 6.00, "Comida")
producto3 = Producto("Coca Cola", 1.50, "Bebida")

cliente1 = Cliente("Juan Pérez", "1234567890", "0999999999")
cliente2 = Cliente("María López", "0987654321", "0888888888")

mi_restaurante = Restaurante()

mi_restaurante.agregar_producto(producto1)
mi_restaurante.agregar_producto(producto2)
mi_restaurante.agregar_producto(producto3)

mi_restaurante.agregar_cliente(cliente1)
mi_restaurante.agregar_cliente(cliente2)

mi_restaurante.mostrar_productos()
mi_restaurante.mostrar_clientes()
