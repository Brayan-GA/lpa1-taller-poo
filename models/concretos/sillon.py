"""
Clase concreta Sillón.
"""
from models.categorias.asientos import Asiento

class Sillon(Asiento):
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 altura_regulable: bool = False, tiene_ruedas: bool = False):
        
        super().__init__(nombre, material, color, precio_base,
                         capacidad_personas=1, tiene_respaldo=tiene_respaldo,
                         material_tapizado=material_tapizado)
        self._altura_regulable = altura_regulable
        self._tiene_ruedas = tiene_ruedas

    @property
    def altura_regulable(self) -> bool:
        """Getter para altura regulable."""
        return self._altura_regulable
    
    @altura_regulable.setter
    def altura_regulable(self, value: bool) -> None:
        """Setter para altura regulable con validación."""
        if not isinstance(value, bool):
            raise ValueError("El valor debe ser un booleano")
        self._altura_regulable = value

    @property
    def tiene_ruedas(self) -> bool:
        """Getter para saber si el sillón tiene ruedas."""
        return self._tiene_ruedas
    
    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:    
        """Setter para las ruedas con validación."""
        if not isinstance(value, bool):
            raise ValueError("El valor debe ser un booleano")
        self._tiene_ruedas = value
    def calcular_precio(self) -> float:
        """
        Calcula el precio del sillón basado en su material y características.
        """
        precio = self._precio_base
        if self._tiene_ruedas:
            precio += 50
        if self._altura_regulable:
            precio += 100
        return precio
    