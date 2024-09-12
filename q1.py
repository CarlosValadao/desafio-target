# claro, num precisa maior que 1
# para valor menores que zero, a funcao
# funciona de forma incorreta
def fibonacci_iterativo(num: int) -> list[int]:
    seq = []
    a, b = 0, 1
    for i in range(num):
        seq.append(a)
        a, b = b, a + b
    return seq

num = int(input("digite o numero -> "))
fibonacci_sequence = fibonacci_iterativo(num)
num_in_fibonacci_sequence = num in fibonacci_sequence
inhere = "pertence" if num_in_fibonacci_sequence else "nao pertence"
print(f'{num} {inhere} a sequência de Fibonacci')