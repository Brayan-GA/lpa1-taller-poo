"""
Clase concreta Escritorio.
"""
from models.categorias.superficies import Superficie
from abc import ABC

class Escritorio(Superficie, ABC):

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 largo: float, ancho: float, altura: float,
                 tiene_cajones: bool):
        
        super().__init__(nombre, material, color, precio_base,
                         largo, ancho, altura)
        self._tiene_cajones = tiene_cajones
    
    @property
    def tiene_cajones(self) -> bool:
        """Getter para saber si el escritorio tiene cajones."""
        return self._tiene_cajones
    
    @tiene_cajones.setter
    def tiene_cajones(self, value: bool) -> None:
        """Setter para los cajones con validación."""
        if not isinstance(value, bool):
            raise ValueError("El valor debe ser un booleano")
        self._tiene_cajones = value

    def calcular_precio(self) -> float:
        """Calcula el precio final del escritorio."""
        precio_final = self.precio_base
        # Agregar un costo adicional si el escritorio tiene cajones
        if self.tiene_cajones:
            precio_final += 30  # Costo adicional por los cajones
        return precio_final
    
    def obtener_descripcion(self) -> str:
        """Obtiene una descripción detallada del escritorio."""
        descripcion = f"Escritorio '{self.nombre}' de material {self.material}, color {self.color}, "
        descripcion += f"dimensiones {self.largo}x{self.ancho}x{self.altura} cm"
        if self.tiene_cajones:
            descripcion += " y equipado con cajones."
        else:
            descripcion += " sin cajones."
        return descripcion  