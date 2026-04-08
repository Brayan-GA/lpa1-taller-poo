"""
Clase abstracta para muebles para superficios de trabajo o del hogar .
"""
from models.mueble import Mueble
from abc import ABC, abstractmethod 

class Superficie(Mueble, ABC):

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 largo: float, ancho: float, altura: float):
        super().__init__(nombre, material, color, precio_base)
        self._largo = largo
        self._ancho = ancho
        self._altura = altura
    

    @property
    def largo(self) -> float:
        """Getter para el largo de la superficie."""
        return self._largo
    
    @largo.setter
    def largo(self, value: float) -> None:
        """Setter para el largo con validación."""
        if value <= 0:
            raise ValueError("El largo debe ser mayor a 0")
        self._largo = value


    @property
    def ancho(self) -> float:
        """Getter para el ancho de la superficie."""
        return self._ancho
    
    @ancho.setter
    def ancho(self, value: float) -> None:
        """Setter para el ancho con validación."""
        if value <= 0:
            raise ValueError("El ancho debe ser mayor a 0")
        self._ancho = value


    @property
    def altura(self) -> float:
        """Getter para la altura de la superficie."""
        return self._altura
    
    @altura.setter
    def altura(self, value: float) -> None:
        """Setter para la altura con validación."""
        if value <= 0:
            raise ValueError("La altura debe ser mayor a 0")
        self._altura = value

        