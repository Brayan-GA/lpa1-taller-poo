"""
Pruebas unitarias para la Tienda.
"""

import pytest

from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.composicion.comedor import Comedor
from services.tienda import TiendaMuebles
from services.catalogo import CatalogoMuebles


class TestTienda:
    def setup_method(self):
        self.tienda = TiendaMuebles("Tienda Test")

        self.silla = Silla(
            nombre="Silla Comercial",
            material="Madera",
            color="Café",
            precio_base=120.0,
            tiene_respaldo=True
        )

        self.mesa = Mesa(
            nombre="Mesa Comercial",
            material="Roble",
            color="Café",
            precio_base=500.0,
            largo=180,
            ancho=90,
            altura=75,
            tipo_mesa="comedor"
        )

        self.comedor = Comedor(
            nombre="Comedor Comercial",
            mesa=self.mesa,
            sillas=[self.silla]
        )

        self.tienda.agregar_mueble(self.silla)
        self.tienda.agregar_comedor(self.comedor)

    def test_agregar_mueble_exitoso(self):
        tienda = TiendaMuebles("Nueva Tienda")
        resultado = tienda.agregar_mueble(self.silla)
        assert "agregado exitosamente" in resultado.lower()
        assert tienda.total_muebles == 1

    def test_agregar_mueble_invalido(self):
        resultado = self.tienda.agregar_mueble("no es un mueble")
        assert "error" in resultado.lower()

    def test_buscar_muebles_por_nombre(self):
        resultados = self.tienda.buscar_muebles_por_nombre("Silla")
        assert len(resultados) == 1
        assert resultados[0].nombre == "Silla Comercial"

    def test_filtrar_por_precio(self):
        resultados = self.tienda.filtrar_por_precio(100, 200)
        assert self.silla in resultados

    def test_filtrar_por_material(self):
        resultados = self.tienda.filtrar_por_material("madera")
        assert self.silla in resultados

    def test_aplicar_descuento_y_realizar_venta(self):
        self.tienda.aplicar_descuento("silla", 20)
        venta = self.tienda.realizar_venta(self.silla, "Cliente Test")

        assert "precio_final" in venta
        assert venta["precio_final"] == pytest.approx(105.6)
        assert self.tienda.total_muebles == 0

    def test_generar_reporte_inventario(self):
        reporte = self.tienda.generar_reporte_inventario()
        assert "Total de muebles" in reporte
        assert "Valor total del inventario" in reporte

    def test_obtener_estadisticas(self):
        stats = self.tienda.obtener_estadisticas()
        assert stats["total_muebles"] == 1
        assert stats["total_comedores"] == 1
        assert stats["ventas_realizadas"] == 0


class TestCatalogo:
    def setup_method(self):
        self.tienda = TiendaMuebles("Tienda Test")
        self.silla = Silla(
            nombre="Silla Comercial",
            material="Madera",
            color="Café",
            precio_base=120.0,
            tiene_respaldo=True
        )
        self.mesa = Mesa(
            nombre="Mesa Comercial",
            material="Roble",
            color="Café",
            precio_base=500.0,
            largo=180,
            ancho=90,
            altura=75,
            tipo_mesa="comedor"
        )
        self.comedor = Comedor("Comedor Comercial", self.mesa, [self.silla])
        self.tienda.agregar_mueble(self.silla)
        self.tienda.agregar_comedor(self.comedor)
        self.catalogo = self.tienda.catalogo

    def test_catalogo_buscar_por_nombre(self):
        resultados = self.catalogo.buscar_por_nombre("Silla")
        assert len(resultados) == 1
        assert resultados[0].nombre == "Silla Comercial"

    def test_catalogo_filtrar_por_material(self):
        resultados = self.catalogo.filtrar_por_material("madera")
        assert any(obj.material.lower() == "madera" for obj in resultados)

    def test_catalogo_ordenar_por_precio(self):
        ordenado = self.catalogo.ordenar_por_precio(ascendente=True)

        def precio(mueble):
            if isinstance(mueble, Comedor):
                return mueble.calcular_precio_total()
            return mueble.calcular_precio()

        assert precio(ordenado[0]) <= precio(ordenado[-1])

    def test_catalogo_ordenar_por_nombre(self):
        ordenado = self.catalogo.ordenar_por_nombre()
        assert ordenado[0].nombre.lower() <= ordenado[-1].nombre.lower()

    def test_catalogo_obtener_rango_precios(self):
        rango = self.catalogo.obtener_rango_precios()
        assert rango["min"] >= 0
        assert rango["max"] >= rango["min"]
        assert rango["promedio"] >= rango["min"]

    def test_catalogo_es_estado_valido(self):
        assert isinstance(self.catalogo, CatalogoMuebles)
