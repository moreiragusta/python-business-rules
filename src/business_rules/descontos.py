def calcular_preco_com_desconto(preco: float, percentual_desconto: float) -> float:
    if preco < 0:
        raise ValueError("O preço não pode ser negativo")
    
    if percentual_desconto < 0:
        raise ValueError("O desconto não pode ser negativo")
    
    if percentual_desconto > 100:
        raise ValueError("O desconto não pode ser maior que 100")
    
    valor_desconto = preco * percentual_desconto / 100
    preco_final = preco - valor_desconto
    
    return round(preco_final, 2)