import pytest

from business_rules.juros import calcular_juros_simples


def test_deve_calcular_juros_taxa_2_por_cento_3_meses():
    resultado = calcular_juros_simples(1000, 2, 3)

    assert resultado == 1060


def test_deve_calcular_juros_taxa_um_e_meio_por_cento_2_meses():
    resultado = calcular_juros_simples(500, 1.5, 2)

    assert resultado == 515


def test_deve_calcular_juros_com_taxa_0_por_cento_12_meses():
    resultado = calcular_juros_simples(1000, 0, 12)

    assert resultado == 1000


def test_deve_calcular_juros_com_taxa_2_por_cento_0_meses():
    resultado = calcular_juros_simples(1000, 2, 0)

    assert resultado == 1000


def test_deve_arredondar_resultado_para_duas_casas_decimais():
    resultado = calcular_juros_simples(201.9, 0.7, 1)

    assert resultado == 203.31


def test_deve_lancar_erro_quando_valor_inicial_for_negativo():
    with pytest.raises(ValueError, match="O valor inicial não pode ser negativo"):
        calcular_juros_simples(-1000, 2, 3)


def test_deve_lancar_erro_quando_taxa_percentual_for_negativa():
    with pytest.raises(ValueError, match="A taxa percentual não pode ser negativa"):
        calcular_juros_simples(1000, -4, 2)


def test_deve_lancar_erro_quando_quantidade_meses_for_negativa():
    with pytest.raises(ValueError, match="A quantidade de meses não pode ser negativa"):
        calcular_juros_simples(1000, 5, -6)