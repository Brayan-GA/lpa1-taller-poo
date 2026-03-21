"""
Clase abstracta para muebles de asiento.
Esta clase agrupa las características comunes de sillas, sillones y sofás.
"""
from models.mueble import Mueble
from abc import ABC

class Asiento(Mueble, ABC):
    """
    Clase abstracta para todos los muebles donde las personas se sientan.
    
    Hereda de Mueble y añade características específicas de los asientos
    como capacidad de personas, tipo de respaldo, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de asientos
    - Polimorfismo: Permite diferentes implementaciones del cálculo de comodidad
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int, tiene_respaldo: bool, material_tapizado: str = None):
        """
        Constructor para muebles de asiento.
        
        Args:
            capacidad_personas: Número de personas que pueden sentarse
            tiene_respaldo: Si el asiento tiene respaldo o no
            material_tapizado: Material del tapizado (opcional)
            Otros argumentos heredados de Mueble
        """
        super().__init__(nombre, material, color, precio_base)
        self._capacidad_personas = capacidad_personas
        self._tiene_respaldo = tiene_respaldo
        self._material_tapizado = material_tapizado
        pass
    
    # TODO: Implementar propiedades (getters) para los nuevos atributos
    # @property
    # def capacidad_personas(self) -> int:
    #     """Getter para la capacidad de personas."""
    #     return self._capacidad_personas
    
    # TODO: Implementar setters con validaciones apropiadas
    # @capacidad_personas.setter
    # def capacidad_personas(self, value: int) -> None:
    #     """Setter para capacidad con validación."""
    #     if value <= 0:
    #         raise ValueError("La capacidad debe ser mayor a 0")
    #     self._capacidad_personas = value
    
    def calcular_factor_comodidad(self) -> float:
        """
        Calcula un factor de comodidad basado en las características del asiento.
        Este es un método concreto que pueden usar las clases hijas.
        
        Returns:
            float: Factor multiplicador para el precio (1.0 = neutral)
        """
        # TODO: Implementar lógica de cálculo de comodidad
        # Considerar factores como:
        # - Si tiene respaldo (+0.1)
        # - Material del tapizado (cuero +0.2, tela +0.1)
        # - Capacidad de personas (más personas = más cómodo)
        
        factor = 1.0
        
        # TODO: Agregar lógica aquí
        # if self.tiene_respaldo:
        #     factor += 0.1
        # 
        # if self.material_tapizado:
        #     if self.material_tapizado.lower() == "cuero":
        #         factor += 0.2
        #     elif self.material_tapizado.lower() == "tela":
        #         factor += 0.1
        
        return factor
    
    def obtener_info_asiento(self) -> str:
        """
        Obtiene información específica del asiento.
        Método concreto auxiliar para las clases hijas.
        
        Returns:
            str: Información detallada del asiento
        """
        # TODO: Implementar retornando información del asiento
        # info = f"Capacidad: {self.capacidad_personas} personas"
        # info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        # if self.material_tapizado:
        #     info += f", Tapizado: {self.material_tapizado}"
        # return info
        pass
    
    # TODO: Mantener el método calcular_precio como abstracto
    # Las clases concretas deben implementar su propio cálculo
    
    # TODO: Mantener el método obtener_descripcion como abstracto
    # Cada tipo de asiento tendrá su propia descripción

