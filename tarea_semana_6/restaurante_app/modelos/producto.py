# Clase padre que representa un producto del restaurante

class Producto:

    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre = nombre
        self.__precio = precio      # Encapsulación
        self.disponible = disponible

    # Método para obtener el precio
    def obtener_precio(self):
        return self.__precio

    # Método para modificar el precio
    def cambiar_precio(self, nuevo_precio):

        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: el precio debe ser mayor que cero.")

    # Método que será sobrescrito
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.__precio}")
        print(f"Disponible: {self.disponible}")