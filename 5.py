def inverter_string(string):
    resultado = ""
    
    # Percorre a string original de trás para frente
    for i in range(len(string) - 1, -1, -1):
        resultado += string[i]
    
    return resultado

# Exemplo de uso:
string_original = "Target Sistemas"
string_invertida = inverter_string(string_original)

print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
