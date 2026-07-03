def calcular_valor_com_multa(
        valor_original: float,
        percentual_multa: float,
        dias_atraso: int
) -> float:
    if valor_original < 0:
        raise ValueError("O valor original não pode ser negativo")

    if percentual_multa < 0:
        raise ValueError("O percentual de multa não pode ser negativo")
    
    if dias_atraso < 0:
        raise ValueError("Os dias de atraso não podem ser negativos")

    if dias_atraso == 0:
        return round(valor_original, 2)

    valor_multa = valor_original * percentual_multa / 100
    valor_final = valor_original + valor_multa

    return round(valor_final, 2)