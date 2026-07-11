from dataclasses import dataclass

# Clase Cliente usando dataclass

@dataclass
class Cliente:
    id_cliente: int
    nombre: str
    correo: str
    