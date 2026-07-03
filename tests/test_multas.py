import pytest

from business_rules.multas import calcular_valor_com_multa


def test_deve_retornar_valor_original_quando_nao_houver_atraso():
    resultado = calcular_valor_com_multa(1000, 2, 0)

    assert resultado == 1000

def test_deve_calcular_valor_com_multa_quando_houver_atraso():
    resultado = calcular_valor_com_multa(1000, 2, 5)

    assert resultado == 1020

def test_deve_arredondar_resultado_para_duas_casas_decimais():
    resultado = calcular_valor_com_multa(999.99, 1.5, 10)

    assert resultado == 1014.99

def test_deve_lancar_erro_quando_valor_original_for_negativo():
    with pytest.raises(ValueError, match="O valor original não pode ser negativo"):
        calcular_valor_com_multa(-1000, 2, 5)

def test_deve_lancar_erro_quando_percentual_multa_for_negativo():
    with pytest.raises(ValueError, match="O percentual de multa não pode ser negativo"):
        calcular_valor_com_multa(1000, -2, 5)

def test_deve_lancar_erro_quando_dias_atraso_for_negativo():
    with pytest.raises(ValueError, match="Os dias de atraso não podem ser negativos"):
        calcular_valor_com_multa(1000, 2, -5)