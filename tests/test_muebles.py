"""
Pruebas unitarias para las clases de muebles.
Estas pruebas validan el correcto funcionamiento de todos los conceptos OOP implementados.
"""

import pytest

from models.concretos.silla import Silla
from models.concretos.sofa import Sofa
from models.concretos.cama import Cama
from models.concretos.mesa import Mesa
from models.concretos.sofacama import SofaCama
from models.categorias.asientos import Asiento
from models.categorias.superficies import Superficie
from models.mueble import Mueble


class TestMuebleBase:
    def test_no_puede_instanciar_mueble_directamente(self):
        with pytest.raises(TypeError):
            Mueble("Test", "Madera", "Café", 100.0)

    def test_propiedades_string_y_repr(self):
        silla = Silla("Silla Demo", "Madera", "Negro", 100.0, True)
        assert str(silla) == "Silla Demo de Madera en color Negro"
        assert "Mueble(nombre='Silla Demo'" in repr(silla)


class TestSilla:
    def setup_method(self):
        self.silla_basica = Silla(
            nombre="Silla Básica",
            material="Madera",
            color="Café",
            precio_base=150.0,
            tiene_respaldo=True
        )

        self.silla_oficina = Silla(
            nombre="Silla Oficina",
            material="Metal",
            color="Negro",
            precio_base=300.0,
            tiene_respaldo=True,
            material_tapizado="cuero",
            altura_regulable=True,
            tiene_ruedas=True
        )

    def test_creacion_silla_basica(self):
        assert self.silla_basica.nombre == "Silla Básica"
        assert self.silla_basica.material == "Madera"
        assert self.silla_basica.color == "Café"
        assert self.silla_basica.precio_base == 150.0
        assert self.silla_basica.altura_regulable is False
        assert self.silla_basica.tiene_ruedas is False
        assert self.silla_basica.capacidad_personas == 1

    def test_calculo_precio_silla_basica(self):
        assert self.silla_basica.calcular_precio() == 165.0

    def test_calculo_precio_silla_oficina(self):
        assert self.silla_oficina.calcular_precio() == 450.0

    def test_es_silla_oficina(self):
        assert self.silla_oficina.es_silla_oficina() is True
        assert self.silla_basica.es_silla_oficina() is False

    def test_regular_altura_silla_sin_mecanismo(self):
        resultado = self.silla_basica.regular_altura(110)
        assert "no tiene altura regulable" in resultado.lower()

    def test_regular_altura_silla_con_mecanismo(self):
        resultado = self.silla_oficina.regular_altura(110)
        assert isinstance(resultado, str)
        assert "altura" in resultado.lower()

    def test_validaciones_setter(self):
        with pytest.raises(ValueError):
            self.silla_basica.nombre = ""

        with pytest.raises(ValueError):
            self.silla_basica.precio_base = -100

        with pytest.raises(ValueError):
            self.silla_basica.capacidad_personas = 0

    def test_obtener_descripcion(self):
        descripcion = self.silla_basica.obtener_descripcion()
        assert "Silla 'Silla Básica'" in descripcion
        assert "material Madera" in descripcion
        assert "color Café" in descripcion

    def test_polimorfismo_herencia(self):
        assert isinstance(self.silla_basica, Asiento)
        assert hasattr(self.silla_basica, 'calcular_precio')
        assert hasattr(self.silla_basica, 'obtener_descripcion')

        precio = self.silla_basica.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0

        descripcion = self.silla_basica.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


class TestSofa:
    def setup_method(self):
        self.sofa = Sofa(
            nombre="Sofá Lounge",
            material="Tela",
            color="Gris",
            precio_base=600.0,
            capacidad_personas=4,
            tiene_respaldo=True,
            material_tapizado="tela"
        )

    def test_calculo_precio_sofa(self):
        assert self.sofa.calcular_precio() == 950.0

    def test_obtener_descripcion_sofa(self):
        descripcion = self.sofa.obtener_descripcion()
        assert "Sofá Lounge" in descripcion
        assert "4 personas" in descripcion
        assert "Gris" in descripcion

    def test_sofa_hereda_de_asiento(self):
        assert isinstance(self.sofa, Asiento)
        assert hasattr(self.sofa, 'calcular_factor_comodidad')


class TestCama:
    def setup_method(self):
        self.cama = Cama(
            nombre="Cama King",
            material="Madera",
            color="Blanco",
            precio_base=800.0,
            largo=200,
            ancho=150,
            altura=40,
            tipo_cama="king"
        )

    def test_calculo_precio_cama(self):
        assert self.cama.calcular_precio() == 1100.0

    def test_tipo_cama_invalido(self):
        with pytest.raises(ValueError):
            self.cama.tipo_cama = "doble"

    def test_obtener_descripcion_cama(self):
        descripcion = self.cama.obtener_descripcion()
        assert "Cama King" in descripcion
        assert "dimensiones" in descripcion


class TestMesa:
    def setup_method(self):
        self.mesa = Mesa(
            nombre="Mesa Comedor",
            material="Roble",
            color="Café",
            precio_base=500.0,
            largo=180,
            ancho=90,
            altura=75,
            tipo_mesa="comedor"
        )

    def test_calculo_precio_mesa(self):
        assert self.mesa.calcular_precio() == 650.0

    def test_tipo_mesa_invalido(self):
        with pytest.raises(ValueError):
            self.mesa.tipo_mesa = "patio"

    def test_obtener_descripcion_mesa(self):
        descripcion = self.mesa.obtener_descripcion()
        assert "Mesa Comedor" in descripcion
        assert "dimensiones" in descripcion


class TestSofaCama:
    def setup_method(self):
        self.sofacama = SofaCama(
            nombre="SofaCama Deluxe",
            material="Tela",
            color="Azul",
            precio_base=500.0,
            capacidad_personas=3,
            material_tapizado="tela",
            tamaño_cama="matrimonial",
            incluye_colchon=True,
            mecanismo_conversion="plegable"
        )

    def test_creacion_sofacama(self):
        assert self.sofacama.nombre == "SofaCama Deluxe"
        assert self.sofacama.capacidad_personas == 3
        assert self.sofacama.tamaño_cama == "matrimonial"
        assert self.sofacama.incluye_colchon is True
        assert self.sofacama.mecanismo_conversion == "plegable"
        assert self.sofacama.modo_actual == "sofa"

    def test_conversion_modos(self):
        assert self.sofacama.modo_actual == "sofa"

        resultado = self.sofacama.convertir_a_cama()
        assert "convertido a cama" in resultado.lower()
        assert self.sofacama.modo_actual == "cama"

        resultado2 = self.sofacama.convertir_a_cama()
        assert "ya está en modo cama" in resultado2.lower()

        resultado3 = self.sofacama.convertir_a_sofa()
        assert "convertida a sofá" in resultado3.lower()
        assert self.sofacama.modo_actual == "sofa"

    def test_calculo_precio_dual(self):
        precio = self.sofacama.calcular_precio()
        assert precio == 1375.0

    def test_capacidad_total(self):
        capacidades = self.sofacama.obtener_capacidad_total()
        assert capacidades["como_sofa"] == 3
        assert capacidades["como_cama"] == 2

    def test_herencia_multiple_mro(self):
        assert isinstance(self.sofacama, Sofa)
        assert isinstance(self.sofacama, Cama)
        assert hasattr(self.sofacama, 'convertir_a_cama')
        assert hasattr(self.sofacama, 'convertir_a_sofa')
        assert hasattr(self.sofacama, 'calcular_precio')
        assert hasattr(self.sofacama, 'obtener_descripcion')

    def test_str_suficientemente_descriptivo(self):
        valor = str(self.sofacama)
        assert "Sofá-cama" in valor
        assert "modo: sofa" in valor



