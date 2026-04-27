"""
Pruebas unitarias para las clases de composición.
"""

import pytest

from models.concretos.mesa import Mesa
from models.concretos.silla import Silla
from models.composicion.comedor import Comedor


class TestComedor:
    def setup_method(self):
        self.mesa = Mesa(
            nombre="Mesa Comedor",
            material="Madera",
            color="Roble",
            precio_base=500.0,
            largo=240,
            ancho=100,
            altura=75,
            tipo_mesa="comedor"
        )

        self.silla1 = Silla("Silla 1", "Madera", "Roble", 120.0, True)
        self.silla2 = Silla("Silla 2", "Madera", "Roble", 120.0, True)

        self.comedor = Comedor(
            nombre="Comedor Familiar",
            mesa=self.mesa,
            sillas=[self.silla1, self.silla2]
        )

    def test_creacion_comedor(self):
        assert self.comedor.nombre == "Comedor Familiar"
        assert self.comedor.mesa == self.mesa
        assert len(self.comedor.sillas) == 2
        assert self.silla1 in self.comedor.sillas
        assert self.silla2 in self.comedor.sillas

    def test_agregar_silla(self):
        silla_nueva = Silla("Silla Nueva", "Madera", "Roble", 120.0, True)
        resultado = self.comedor.agregar_silla(silla_nueva)

        assert "exitosamente" in resultado.lower()
        assert len(self.comedor.sillas) == 3
        assert silla_nueva in self.comedor.sillas

    def test_agregar_objeto_invalido(self):
        resultado = self.comedor.agregar_silla("no es silla")
        assert "error" in resultado.lower()

    def test_agregar_silla_capacidad_maxima(self):
        self.comedor.agregar_silla(Silla("Silla 3", "Madera", "Roble", 120.0, True))
        self.comedor.agregar_silla(Silla("Silla 4", "Madera", "Roble", 120.0, True))

        resultado = self.comedor.agregar_silla(Silla("Silla 5", "Madera", "Roble", 120.0, True))
        assert "no se pueden agregar más sillas" in resultado.lower()

    def test_quitar_silla(self):
        resultado = self.comedor.quitar_silla(0)
        assert "removida" in resultado.lower()
        assert len(self.comedor.sillas) == 1

    def test_quitar_silla_indice_invalido(self):
        resultado = self.comedor.quitar_silla(10)
        assert "índice de silla inválido" in resultado.lower()

    def test_calculo_precio_total(self):
        assert self.comedor.calcular_precio_total() == 914.0

    def test_calculo_precio_total_con_descuento(self):
        self.comedor.agregar_silla(Silla("Silla 3", "Madera", "Roble", 120.0, True))
        self.comedor.agregar_silla(Silla("Silla 4", "Madera", "Roble", 120.0, True))

        assert self.comedor.calcular_precio_total() == 1119.1

    def test_obtener_descripcion_completa(self):
        descripcion = self.comedor.obtener_descripcion_completa()
        assert "COMEDOR" in descripcion
        assert "MESA:" in descripcion
        assert "SILLAS" in descripcion
        assert "PRECIO TOTAL" in descripcion

    def test_obtener_resumen(self):
        resumen = self.comedor.obtener_resumen()
        assert resumen["nombre"] == "Comedor Familiar"
        assert resumen["total_muebles"] == 3
        assert resumen["precio_mesa"] == self.mesa.calcular_precio()
        assert resumen["precio_total"] == self.comedor.calcular_precio_total()
        assert set(resumen["materiales_utilizados"]) == {"Madera"}

    def test_len_comedor(self):
        assert len(self.comedor) == 3
