class Estudiante:
    role = "Estudiante"
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")

estudiante1 = Estudiante("Jostin villón", 19, "Ingeniería en tic")                    
estudiante1.mostrar_informacion()
print("\n")
estudiante2 = Estudiante("kiara Ponce", 16, "informatica")
estudiante2.mostrar_informacion()

