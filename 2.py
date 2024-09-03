def is_fibonacci(num,a=0,b=1):
    if num < 0:
        return False

    while a < num:
        a, b = b, a + b

    return a == num

# Exemplo para uso:
num = 8
if is_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
