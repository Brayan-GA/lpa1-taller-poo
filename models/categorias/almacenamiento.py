"""
Clase abstracta para muebles de almacenamiento.
"""
from models.mueble import Mueble
from abc import ABC, abstractmethod

class Almacenamiento(Mueble, ABC):
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_almacenamiento: float, numero_compartimentos: int):


        super().__init__(nombre, material, color, precio_base)
        self._capacidad_almacenamiento = capacidad_almacenamiento
        self._numero_compartimentos = numero_compartimentos
    

    @property
    def capacidad_almacenamiento(self) -> float:
        """Getter para la capacidad de almacenamiento."""
        return self._capacidad_almacenamiento
    
    @capacidad_almacenamiento.setter
    def capacidad_almacenamiento(self, value: float) -> None:
        """Setter para la capacidad con validación."""
        if value <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._capacidad_almacenamiento = value

    @property
    def numero_compartimentos(self) -> int:
        """Getter para el número de compartimentos."""
        return self._numero_compartimentos
    
    @numero_compartimentos.setter
    def numero_compartimentos(self, value: int) -> None:
        """Setter para el número de compartimentos con validación."""
        if value < 0:
            raise ValueError("El número de compartimentos no puede ser negativo")
        self._numero_compartimentos = value

    #Implementar métodos abstractos específicos para muebles de almacenamiento si es necesario



    @abstractmethod
    def calcular_precio(self) -> float:
        pass
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass