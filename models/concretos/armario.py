"""
Clase concreta Armario.
"""
from models.categorias.almacenamiento import Almacenamiento
from abc import ABC

class Armario(Almacenamiento, ABC):
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_almacenamiento: float, numero_compartimentos: int,
                 tiene_espejo: bool):
        
        super().__init__(nombre, material, color, precio_base,
                         capacidad_almacenamiento, numero_compartimentos)
        self._tiene_espejo = tiene_espejo
    
    @property
    def tiene_espejo(self) -> bool:
        """Getter para saber si el armario tiene espejo."""
        return self._tiene_espejo
    
    @tiene_espejo.setter
    def tiene_espejo(self, value: bool) -> None:
        """Setter para el espejo con validación."""
        if not isinstance(value, bool):
            raise ValueError("El valor debe ser un booleano")
        self._tiene_espejo = value

    def calcular_precio(self) -> float:
        """Calcula el precio final del armario."""
        precio_final = self.precio_base
        # Agregar un costo adicional si el armario tiene espejo
        if self.tiene_espejo:
            precio_final += 50  # Costo adicional por el espejo
        return precio_final
    
    def obtener_descripcion(self) -> str:
        """Obtiene una descripción detallada del armario."""
        descripcion = f"Armario '{self.nombre}' de material {self.material}, color {self.color}, "
        descripcion += f"capacidad de almacenamiento de {self.capacidad_almacenamiento} litros, "
        descripcion += f"con {self.numero_compartimentos} compartimentos"
        if self.tiene_espejo:
            descripcion += " y equipado con espejo."
        else:
            descripcion += " sin espejo."
        return descripcion