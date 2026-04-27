"""
Clase concreta Mesa.
"""
from models.categorias.superficies import Superficie
from abc import ABC

class Mesa(Superficie, ABC):

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 largo: float, ancho: float, altura: float,
                 tipo_mesa: str):
        
        super().__init__(nombre, material, color, precio_base,
                         largo, ancho, altura)
        self._tipo_mesa = tipo_mesa
    
    @property
    def tipo_mesa(self) -> str:
        """Getter para el tipo de mesa (comedor, centro, auxiliar)."""
        return self._tipo_mesa
    
    @tipo_mesa.setter
    def tipo_mesa(self, value: str) -> None:
        """Setter para el tipo de mesa con validación."""
        tipos_validos = ["comedor", "centro", "auxiliar"]
        if value.lower() not in tipos_validos:
            raise ValueError(f"Tipo de mesa inválido. Debe ser uno de: {', '.join(tipos_validos)}")
        self._tipo_mesa = value.lower()

    def calcular_precio(self) -> float:
        """Calcula el precio final de la mesa."""
        precio_final = self.precio_base
        # Agregar un costo adicional según el tipo de mesa
        if self.tipo_mesa == "comedor":
            precio_final += 150  # Costo adicional para mesa de comedor
        elif self.tipo_mesa == "centro":
            precio_final += 50   # Costo adicional para mesa de centro
        elif self.tipo_mesa == "auxiliar":
            precio_final += 20   # Costo adicional para mesa auxiliar
        return precio_final
    
    def obtener_descripcion(self) -> str:
        """Obtiene una descripción detallada de la mesa."""
        descripcion = (f"Mesa {self.tipo_mesa.capitalize()} de {self.material}, "
                       f"color {self.color}, dimensiones {self.largo}x{self.ancho}x{self.altura} cm.")
        return descripcion
