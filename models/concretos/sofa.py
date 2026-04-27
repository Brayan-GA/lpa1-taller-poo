"""
Clase concreta Sofa.
"""
from models.categorias.asientos import Asiento

class Sofa(Asiento):

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int, tiene_respaldo: bool = True,
                 material_tapizado: str = None):
        
        super().__init__(nombre, material, color, precio_base,
                         capacidad_personas, tiene_respaldo, material_tapizado)
        
    def calcular_precio(self) -> float:
        """
        Calcula el precio del sofá basado en su material, capacidad y características.
        """
        precio = self.precio_base
        # Agregar un costo adicional por cada persona adicional
        if self.capacidad_personas > 2:
            precio += (self.capacidad_personas - 2) * 100
        # Agregar un costo adicional por material de tapizado
        if self.material_tapizado:
            precio += 150  # Costo adicional por tapizado
        return round(precio, 2)    
     
    def obtener_descripcion(self) -> str:
        """
        Obtiene la descripción del sofá.
        """
        return f"Sofá {self.nombre}, {self.capacidad_personas} personas, {self.color}"
                                                    