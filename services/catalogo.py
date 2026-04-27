from typing import List, Dict, Optional, Union, Callable
from models.mueble import Mueble
from models.composicion.comedor import Comedor


class CatalogoMuebles:
    def __init__(self, muebles: List[Union[Mueble, Comedor]] = None):
        self._muebles = muebles if muebles is not None else []

    @property
    def muebles(self) -> List[Union[Mueble, Comedor]]:
        return self._muebles.copy()

    def agregar_mueble(self, mueble: Union[Mueble, Comedor]) -> None:
        if mueble not in self._muebles:
            self._muebles.append(mueble)

    def buscar_por_nombre(self, nombre: str, case_sensitive: bool = False) -> List[Union[Mueble, Comedor]]:
        if not nombre or not nombre.strip():
            return []

        nombre_busqueda = nombre if case_sensitive else nombre.lower().strip()

        resultados = []
        for mueble in self._muebles:
            nombre_mueble = mueble.nombre if case_sensitive else mueble.nombre.lower()
            if nombre_busqueda in nombre_mueble:
                resultados.append(mueble)

        return resultados

    def filtrar_por_rango_precio(self, precio_min: float = 0,
                                precio_max: float = float('inf')) -> List[Union[Mueble, Comedor]]:
        if precio_min < 0:
            precio_min = 0

        resultados = []
        for mueble in self._muebles:
            try:
                if isinstance(mueble, Comedor):
                    precio = mueble.calcular_precio_total()
                else:
                    precio = mueble.calcular_precio()

                if precio_min <= precio <= precio_max:
                    resultados.append(mueble)
            except Exception:
                continue

        return resultados

    def filtrar_por_material(self, material: str) -> List[Union[Mueble, Comedor]]:
        if not material or not material.strip():
            return []

        material_lower = material.lower().strip()
        resultados = []

        for mueble in self._muebles:
            if hasattr(mueble, 'material') and mueble.material.lower() == material_lower:
                resultados.append(mueble)
            elif isinstance(mueble, Comedor):
                if mueble.mesa.material.lower() == material_lower:
                    resultados.append(mueble)
                    continue
                for silla in mueble.sillas:
                    if silla.material.lower() == material_lower:
                        resultados.append(mueble)
                        break

        return resultados

    def filtrar_por_color(self, color: str) -> List[Union[Mueble, Comedor]]:
        if not color or not color.strip():
            return []

        color_lower = color.lower().strip()
        resultados = []

        for mueble in self._muebles:
            if hasattr(mueble, 'color') and mueble.color.lower() == color_lower:
                resultados.append(mueble)
            elif isinstance(mueble, Comedor):
                if mueble.mesa.color.lower() == color_lower:
                    resultados.append(mueble)
                    continue
                for silla in mueble.sillas:
                    if silla.color.lower() == color_lower:
                        resultados.append(mueble)
                        break

        return resultados

    def filtrar_por_tipo(self, tipo_clase: type) -> List[Union[Mueble, Comedor]]:
        return [mueble for mueble in self._muebles if isinstance(mueble, tipo_clase)]

    def buscar_avanzada(self, criterios: Dict[str, Union[str, float, type]]) -> List[Union[Mueble, Comedor]]:
        resultados = self._muebles.copy()

        for criterio, valor in criterios.items():
            if criterio == "nombre":
                resultados = [m for m in resultados if valor.lower() in m.nombre.lower()]
            elif criterio == "material":
                resultados = [m for m in resultados
                            if hasattr(m, 'material') and m.material.lower() == valor.lower()]
            elif criterio == "color":
                resultados = [m for m in resultados
                            if hasattr(m, 'color') and m.color.lower() == valor.lower()]
            elif criterio == "precio_min":
                resultados = [m for m in resultados
                            if self._obtener_precio(m) >= valor]
            elif criterio == "precio_max":
                resultados = [m for m in resultados
                            if self._obtener_precio(m) <= valor]
            elif criterio == "tipo":
                resultados = [m for m in resultados if isinstance(m, valor)]

        return resultados

    def ordenar_por_precio(self, ascendente: bool = True) -> List[Union[Mueble, Comedor]]:
        def obtener_precio(mueble):
            try:
                return self._obtener_precio(mueble)
            except:
                return float('inf')

        return sorted(self._muebles, key=obtener_precio, reverse=not ascendente)

    def ordenar_por_nombre(self, ascendente: bool = True) -> List[Union[Mueble, Comedor]]:
        return sorted(self._muebles, key=lambda m: m.nombre.lower(), reverse=not ascendente)

    def obtener_estadisticas_materiales(self) -> Dict[str, int]:
        estadisticas = {}
        for mueble in self._muebles:
            if hasattr(mueble, 'material'):
                material = mueble.material.lower()
                estadisticas[material] = estadisticas.get(material, 0) + 1
            elif isinstance(mueble, Comedor):
                materiales_comedor = mueble._obtener_materiales_unicos()
                for material in materiales_comedor:
                    material_lower = material.lower()
                    estadisticas[material_lower] = estadisticas.get(material_lower, 0) + 1

        return estadisticas

    def obtener_rango_precios(self) -> Dict[str, float]:
        precios = []
        for mueble in self._muebles:
            try:
                precio = self._obtener_precio(mueble)
                precios.append(precio)
            except:
                continue

        if not precios:
            return {"min": 0, "max": 0, "promedio": 0}

        return {
            "min": min(precios),
            "max": max(precios),
            "promedio": sum(precios) / len(precios)
        }

    def _obtener_precio(self, mueble: Union[Mueble, Comedor]) -> float:
        if isinstance(mueble, Comedor):
            return mueble.calcular_precio_total()
        else:
            return mueble.calcular_precio()

    def __len__(self) -> int:
        """Retorna el número de muebles en el catálogo."""
        return len(self._muebles)

    def __str__(self) -> str:
        """Representación en cadena del catálogo."""
        return f"Catálogo con {len(self._muebles)} muebles"

