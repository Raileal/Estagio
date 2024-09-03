faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento.values())
print(f"A soma dos faturamentos foi: {faturamento_total}, que corresponde a 100%")

for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado} - {percentual:.2f}% do total")