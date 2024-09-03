import json

def calcular_faturamento(faturamento):
    faturamento_filtrado = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    
    if not faturamento_filtrado:
        return None, None, 0
    
    menor_faturamento = min(faturamento_filtrado)
    maior_faturamento = max(faturamento_filtrado)
    
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
    
    dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media, media_mensal

def main():
    with open('faturamento.json', 'r') as file:
        faturamento = json.load(file)
    
    menor, maior, dias_acima_media, media_mensal = calcular_faturamento(faturamento)
    
    if menor is not None and maior is not None:
        print(f"Menor valor de faturamento: R$ {menor:.2f}")
        print(f"Maior valor de faturamento: R$ {maior:.2f}")
        print(f"Média Mensal: {round(media_mensal,2)}")
        print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
    else:
        print("Não houve faturamento durante o mês.")


main()

