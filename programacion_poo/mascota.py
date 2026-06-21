class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print("\n--- INFORMACIÓN DE LA MASCOTA ---")
        print("Nombre:", self.nombre)
        print("Especie:", self.especie)
        print("Edad:", self.edad, "años")

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print("¡Guau! ¡Guau!")
        elif self.especie.lower() == "gato":
            print("¡Miau! ¡Miau!")
        else:
            print("¡Sonido desconocido para esta especie!")
            
