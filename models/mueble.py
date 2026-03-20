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
    
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("El nombre debe ser una cadena de texto")
        self._nombre = value

    @property
    def material(self) -> str:
        return self._material
    
    @material.setter
    def material(self, value: str):
        if not isinstance(value, str):
            raise TypeError("El material debe ser una cadena de texto")
        self._material = value

    @property
    def color(self) -> str:
        return self._color
    
    @color.setter
    def color(self, value: str):    
        if not isinstance(value, str):
            raise TypeError("El color debe ser una cadena de texto")
        self._color = value

    @property
    def precio_base(self) -> float:
        return self._precio_base
    
    @precio_base.setter
    def precio_base(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("El precio base debe ser un número")
        if value < 0:
            raise ValueError("El precio base no puede ser negativo")
        self._precio_base = value
    
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

