"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""

# TODO: Importar la clase padre Asiento
# from ..categorias.asientos import Asiento
from models.categorias.asientos import Asiento

class Silla(Asiento):
 
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 altura_regulable: bool = False, tiene_ruedas: bool = False):
        
        # TODO: Llamar al constructor padre con capacidad fija de 1 persona
        super().__init__(nombre, material, color, precio_base,
                         capacidad_personas=1, tiene_respaldo=tiene_respaldo,
                         material_tapizado=material_tapizado)
        # TODO: Inicializar atributos específicos de la silla
        self._altura_regulable = altura_regulable
        self._tiene_ruedas = tiene_ruedas
        pass
    
    # TODO: Implementar propiedades para los nuevos atributos
    # @property
    # def altura_regulable(self) -> bool:
    #     """Getter para altura regulable."""
    #     return self._altura_regulable
    @property
    def altura_regulable(self) -> bool:
        """Getter para altura regulable."""
        return self._altura_regulable

    # @altura_regulable.setter
    # def altura_regulable(self, value: bool) -> None:
    #     """Setter para altura regulable."""
    #     self._altura_regulable = value
    @altura_regulable.setter
    def altura_regulable(self, value: bool) -> None:
        """Setter para altura regulable con validación."""
        if not isinstance(value, bool):
            raise ValueError("El valor debe ser un booleano")
        self._altura_regulable = value

    @property
    def tiene_ruedas(self) -> bool:
        """Getter para saber si la silla tiene ruedas."""
        return self._tiene_ruedas   
    
    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        """Setter para las ruedas con validación."""
        if not isinstance(value, bool):
            raise ValueError("El valor debe ser un booleano")
        self._tiene_ruedas = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para sillas.
        
        Returns:
            float: Precio final de la silla
        """
        # TODO: Implementar cálculo de precio para silla

        # 1. Comenzar con el precio base
        
        # 2. Aplicar factor de comodidad heredado
        
        # 3. Agregar costos por características especiales
        
        # 4. Retornar precio redondeado a 2 decimales
        precio_final = self.precio_base
        # Aplicar factor de comodidad
        precio_final *= self.calcular_factor_comodidad()
        # Agregar costos por características especiales
        if self.altura_regulable:
            precio_final += 40  # Costo adicional por altura regulable
            if self.tiene_ruedas:
                precio_final += 20  # Costo adicional por ruedas
                return round(precio_final, 2)
        return round(precio_final, 2)
    

    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la silla.
        
        Returns:
            str: Descripción completa de la silla
        """
        # TODO: Crear y retornar descripción detallada
        descripcion = f"Silla '{self.nombre}' de material {self.material}, color {self.color}, "
        descripcion += f"con respaldo {'sí' if self.tiene_respaldo else 'no'}, "
        if self.material_tapizado:
            descripcion += f"tapizada en {self.material_tapizado}, "    
            descripcion += f"con altura regulable {'sí' if self.altura_regulable else 'no'} y "
            descripcion += f"con ruedas {'sí' if self.tiene_ruedas else 'no'}."
        return descripcion
        pass
    
    def regular_altura(self, nueva_altura: int) -> str:
        """
        Simula la regulación de altura de la silla.
        Método específico de la clase Silla.
        
        Args:
            nueva_altura: Nueva altura en centímetros
            
        Returns:
            str: Mensaje del resultado de la operación
        """
        # TODO: Implementar lógica de regulación
        if not self.altura_regulable:
            return "Esta silla no tiene altura regulable."
        pass
    
    def es_silla_oficina(self) -> bool:
        """
        Determina si la silla es adecuada para oficina.
        
        Returns:
            bool: True si es silla de oficina
        """
        # TODO: Una silla es de oficina si tiene ruedas Y altura regulable
        if self.altura_regulable and self.tiene_ruedas:
            return True
        return False
        pass

