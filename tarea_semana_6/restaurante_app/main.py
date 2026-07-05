from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante
# Crear restaurante
mi_restaurante = Restaurante()
# Crear platillos

platillo1 = Platillo(
    "Pizza Familiar",
    12.50,
    True,
    1200
)

platillo2 = Platillo(
    "Hamburguesa",
    2.75,
    True,
    850
)
# Crear bebidas

bebida1 = Bebida(
    "Coca Cola",
    1.75,
    True,
    500
)

bebida2 = Bebida(
    "Jugo Natural",
    1.25,
    True,
    350
)
# Agregar productos

mi_restaurante.agregar_producto(platillo1)
mi_restaurante.agregar_producto(platillo2)
mi_restaurante.agregar_producto(bebida1)
mi_restaurante.agregar_producto(bebida2)
# Modificar precio usando encapsulación

platillo1.cambiar_precio(13.50)

# Mostrar información

mi_restaurante.mostrar_productos()