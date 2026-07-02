def calcular_juros_simples(valor_inicial: float, taxa_percentual: float, meses: int) -> float:
    if valor_inicial < 0:
        raise ValueError("O valor inicial não pode ser negativo")

    if taxa_percentual < 0:
        raise ValueError("A taxa percentual não pode ser negativa")
    
    if meses < 0:
        raise ValueError("A quantidade de meses não pode ser negativa")

    valor_final = valor_inicial + (valor_inicial * taxa_percentual / 100 * meses)

    return round(valor_final, 2)