def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")

    return nombre, especie, edad

def mostrar_mascota(nombre, especie, edad):
    print("\n--- INFORMACIÓN DE LA MASCOTA ---")
    print("Nombre:", nombre)
    print("Especie:", especie)
    print("Edad:", edad, "años")

nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)
