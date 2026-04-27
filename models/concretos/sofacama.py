"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""


from ..mueble import Mueble
from .sofa import Sofa
from .cama import Cama

class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.
    
    Un sofá-cama es un mueble que funciona tanto como asiento durante el día
    como cama durante la noche.
    
    Conceptos OOP aplicados:
    - Herencia múltiple: Hereda de Sofa y Cama
    - Resolución MRO: Maneja el orden de resolución de métodos
    - Polimorfismo: Implementa comportamientos únicos combinando funcionalidades
    - Super(): Usa super() para resolver conflictos de herencia
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, material_tapizado: str = "tela",
                 tamaño_cama: str = "matrimonial", incluye_colchon: bool = True,
                 mecanismo_conversion: str = "plegable"):
        """
        Constructor del sofá-cama.
        
        Args:
            mecanismo_conversion: Tipo de mecanismo de conversión (plegable, extensible, etc.)
            Otros argumentos se pasan a las clases padre
        """

        Mueble.__init__(self, nombre, material, color, precio_base)
        self._capacidad_personas = capacidad_personas
        self._tiene_respaldo = True
        self._material_tapizado = material_tapizado

        self.tamaño_cama = tamaño_cama
        self.tipo_cama = tamaño_cama
        self.incluye_colchon = incluye_colchon
        self.mecanismo_conversion = mecanismo_conversion
        self.modo_actual = "sofa"  # Puede ser "sofa" o "cama"
    

    @property
    def tamaño_cama(self) -> str:
        """Getter para el tamaño de la cama."""
        return self._tamaño_cama
    
    @tamaño_cama.setter
    def tamaño_cama(self, valor: str):
        """Setter para el tamaño de la cama con validación."""
        tamaños_validos = ["individual", "matrimonial", "queen", "king"]
        if valor not in tamaños_validos:
            raise ValueError(f"Tamaño de cama inválido. Debe ser uno de: {', '.join(tamaños_validos)}")
        self._tamaño_cama = valor

    @property
    def incluye_colchon(self) -> bool:
        """Getter para si incluye colchón."""
        return self._incluye_colchon    
    
    @incluye_colchon.setter
    def incluye_colchon(self, valor: bool):
        """Setter para si incluye colchón con validación."""
        if not isinstance(valor, bool):
            raise ValueError("El valor de incluye_colchon debe ser un booleano.")
        self._incluye_colchon = valor

    @property
    def mecanismo_conversion(self) -> str:
        """Getter para el mecanismo de conversión."""
        return self._mecanismo_conversion   
    
    @mecanismo_conversion.setter
    def mecanismo_conversion(self, valor: str):
        """Setter para el mecanismo de conversión con validación."""
        mecanismos_validos = ["plegable", "extensible", "electrico", "hidraulico"]
        if valor not in mecanismos_validos:
            raise ValueError(f"Mecanismo de conversión inválido. Debe ser uno de: {', '.join(mecanismos_validos)}")
        self._mecanismo_conversion = valor

    @property
    def modo_actual(self) -> str:
        """Getter para el modo actual (sofa o cama)."""
        return self._modo_actual
    
    @modo_actual.setter
    def modo_actual(self, valor: str):
        """Setter para el modo actual con validación."""
        modos_validos = ["sofa", "cama"]
        if valor not in modos_validos:
            raise ValueError(f"Modo actual inválido. Debe ser 'sofa' o 'cama'.")
        self._modo_actual = valor   

    
    def convertir_a_cama(self) -> str:
        """
        Convierte el sofá en cama.
        Método específico del sofá-cama.
        
        Returns:
            str: Mensaje del resultado de la conversión
        """
        if self._modo_actual == "cama":
            return "El sofá-cama ya está en modo cama"
        self._modo_actual = "cama"
        return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"
    
    def convertir_a_sofa(self) -> str:
        """
        Convierte la cama en sofá.
        Método específico del sofá-cama.
        
        Returns:
            str: Mensaje del resultado de la conversión
        """
        if self._modo_actual == "sofa":
            return "El sofá-cama ya está en modo sofá"
        self._modo_actual = "sofa"
        return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"
    
    def calcular_precio(self) -> float:
        """
        Calcula el precio combinando las funcionalidades de sofá y cama.
        
        Returns:
            float: Precio final del sofá-cama
        """
        precio = self.precio_base
        precio *= self.calcular_factor_comodidad()
        precio *= 1.5  # 50% más caro por ser dual
        if self.mecanismo_conversion == "electrico":
            precio += 200
        elif self.mecanismo_conversion == "hidraulico":
            precio += 150
        else:  # manual/plegable
            precio += 100
        if self.incluye_colchon:
            precio += 300
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Descripción que combina características de sofá y cama.
        
        Returns:
            str: Descripción completa del sofá-cama
        """
        descripcion = f"Sofá-cama {self.nombre} fabricado en {self.material}, color {self.color}."
        descripcion += f"\n{self.obtener_info_asiento()}"
        descripcion += f"\nTamaño de cama: {self.tamaño_cama}"
        descripcion += f"\nMecanismo de conversión: {self.mecanismo_conversion}"
        descripcion += f"\nColchón incluido: {'Sí' if self.incluye_colchon else 'No'}"
        descripcion += f"\nModo actual: {self.modo_actual}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion
    
    def obtener_capacidad_total(self) -> dict:
        """
        Obtiene la capacidad tanto como sofá como cama.
        Método único del sofá-cama.
        
        Returns:
            dict: Capacidades en ambos modos
        """
        capacidades = {
            "como_sofa": self.capacidad_personas,
            "como_cama": 2 if self.tamaño_cama in ["matrimonial", "queen", "king"] else 1
        }
        return capacidades
    
    def puede_usar_como_cama(self) -> bool:
        """Verifica si actualmente puede usarse como cama."""
        return self.modo_actual == "cama"
    
    def puede_usar_como_sofa(self) -> bool:
        """Verifica si actualmente puede usarse como sofá."""
        return self.modo_actual == "sofa"
    
    def __str__(self) -> str:
        """
        Representación en cadena del sofá-cama.
        Sobrescribe el método heredado para mostrar información específica.
        """
        return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"

