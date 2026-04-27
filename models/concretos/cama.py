"""
Clase concreta Cama.
"""
from models.categorias.superficies import Superficie
from abc import ABC
class Cama(Superficie, ABC):
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 largo: float, ancho: float, altura: float,
                 tipo_cama: str):
        
        super().__init__(nombre, material, color, precio_base,
                         largo, ancho, altura)
        self._tipo_cama = tipo_cama
    
    @property
    def tipo_cama(self) -> str:
        """Getter para el tipo de cama (individual, matrimonial, queen, king)."""
        return self._tipo_cama
    
    @tipo_cama.setter
    def tipo_cama(self, value: str) -> None:
        """Setter para el tipo de cama con validación."""
        tipos_validos = ["individual", "matrimonial", "queen", "king"]
        if value.lower() not in tipos_validos:
            raise ValueError(f"Tipo de cama inválido. Debe ser uno de: {', '.join(tipos_validos)}")
        self._tipo_cama = value.lower()

    def calcular_precio(self) -> float:
        """Calcula el precio final de la cama."""
        precio_final = self.precio_base
        # Agregar un costo adicional según el tipo de cama
        if self.tipo_cama == "matrimonial":
            precio_final += 100  # Costo adicional para cama matrimonial
        elif self.tipo_cama == "queen":
            precio_final += 200  # Costo adicional para cama queen
        elif self.tipo_cama == "king":
            precio_final += 300  # Costo adicional para cama king
        return precio_final
    
    def obtener_descripcion(self) -> str:
        """Obtiene una descripción detallada de la cama."""
        descripcion = (f"Cama {self.tipo_cama.capitalize()} de {self.material}, "
                       f"color {self.color}, dimensiones {self.largo}x{self.ancho}x{self.altura} cm.")
        return descripcion