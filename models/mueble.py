"""
Clase base abstracta Mueble
Este es el punto de partida de nuestra jerarquía de clases.
"""


from abc import ABC, abstractmethod

class Mueble(ABC):

    @abstractmethod
    def __init__(self, nombre: str, material: str, color: str, precio_base: float):

        self._nombre = nombre
        self._material = material
        self._color = color
        self._precio_base = precio_base
    pass
    
    # TODO: Implementar las propiedades (getters) para cada atributo
    # Usa el decorador @property para crear getters
    # Ejemplo:
    # @property
    # def nombre(self) -> str:
    #     """Getter para el nombre del mueble."""
    #     return self._nombre
    # TODO: Implementar los setters para cada atributo donde sea necesario
    # Usa el decorador @nombre.setter para crear setters
    # Incluye validaciones básicas (ej: precio no puede ser negativo)
    # Ejemplo:
    # @nombre.setter
    # def nombre(self, value: str) -> None:
    #     """Setter para el nombre con validación."""
    #     if not value or not value.strip():
    #         raise ValueError("El nombre no puede estar vacío")
    #     self._nombre = value.strip()
    
    # TODO: Implementar método abstracto calcular_precio()
    # Este método debe ser implementado por todas las clases hijas
    # Usa el decorador @abstractmethod
    # def calcular_precio(self) -> float:
    #     """
    #     Calcula el precio final del mueble.
    #     Este método debe ser implementado por cada clase concreta.
    #     
    #     Returns:
    #         float: Precio final calculado
    #     """
    #     pass
    
    # TODO: Implementar método abstracto obtener_descripcion()
    # Este método debe retornar una descripción detallada del mueble
    # def obtener_descripcion(self) -> str:
    #     """
    #     Obtiene una descripción detallada del mueble.
    #     Este método debe ser implementado por cada clase concreta.
    #     
    #     Returns:
    #         str: Descripción completa del mueble
    #     """
    #     pass
    
    def __str__(self) -> str:
        """
        Representación en cadena del mueble.
        Este método concreto puede ser usado por todas las clases hijas.
        """
        # TODO: Implementar usando las propiedades
        # return f"{self.nombre} de {self.material} en color {self.color}"
        pass
    
    def __repr__(self) -> str:
        """
        Representación técnica del mueble para debugging.
        """
        # TODO: Implementar una representación técnica
        # return f"Mueble(nombre='{self.nombre}', material='{self.material}', color='{self.color}', precio_base={self.precio_base})"
        pass

