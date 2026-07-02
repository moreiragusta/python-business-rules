import pytest

from business_rules.descontos import calcular_preco_com_desconto


def test_deve_calcular_preco_com_desconto_de_10_por_cento():
    resultado = calcular_preco_com_desconto(100, 10)

    assert resultado == 90

def test_deve_calcular_preco_com_desconto_de_25_por_cento():
    resultado = calcular_preco_com_desconto(200, 25)

    assert resultado == 150

def test_deve_arredondar_resultado_para_duas_casas_decimais():
    resultado = calcular_preco_com_desconto(99.90, 10)

    assert resultado == 89.91

def test_deve_retornar_preco_original_quando_desconto_for_zero():
    resultado = calcular_preco_com_desconto(150, 0)

    assert resultado == 150

def test_deve_retornar_zero_quando_desconto_for_cem_por_cento():
    resultado = calcular_preco_com_desconto(150, 100)

    assert resultado == 0

def test_deve_lancer_erro_quando_preco_for_negativo():
    with pytest.raises(ValueError, match = "O preço não pode ser negativo"):
        calcular_preco_com_desconto(-100, 10)

def test_deve_lancar_erro_quando_desconto_for_negativo():
    with pytest.raises(ValueError, match = "O desconto não pode ser negativo"):
        calcular_preco_com_desconto(100, -10)

def test_deve_lancar_erro_quando_desconto_for_maior_que_cem():
    with pytest.raises(ValueError, match = "O desconto não pode ser maior que 100"):
        calcular_preco_com_desconto(100, 101)