"""
Clase concreta Cajonera.
"""             
from models.categorias.almacenamiento import Almacenamiento
from abc import ABC

class Cajonera(Almacenamiento, ABC):    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_almacenamiento: float, numero_compartimentos: int,
                 tiene_ruedas: bool):
        
        super().__init__(nombre, material, color, precio_base,
                         capacidad_almacenamiento, numero_compartimentos)
        self._tiene_ruedas = tiene_ruedas
    
    @property
    def tiene_ruedas(self) -> bool:
        """Getter para saber si la cajonera tiene ruedas."""
        return self._tiene_ruedas
    
    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        """Setter para las ruedas con validación."""
        if not isinstance(value, bool):
            raise ValueError("El valor debe ser un booleano")
        self._tiene_ruedas = value

    def calcular_precio(self):
        """Calcula el precio final de la cajonera."""
        precio_final = self.precio_base
        # Agregar un costo adicional si la cajonera tiene ruedas
        if self.tiene_ruedas:
            precio_final += 20  # Costo adicional por las ruedas
        return precio_final 
    
    def obtener_descripcion(self) -> str:
        """Obtiene una descripción detallada de la cajonera."""
        descripcion = f"Cajonera '{self.nombre}' de material {self.material}, color {self.color}, "
        descripcion += f"capacidad de almacenamiento de {self.capacidad_almacenamiento} litros, "
        descripcion += f"con {self.numero_compartimentos} compartimentos"
        if self.tiene_ruedas:
            descripcion += " y equipada con ruedas."
        else:
            descripcion += " sin ruedas."
        return descripcion