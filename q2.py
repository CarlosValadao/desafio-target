# buscar linear
# devolve a quantidade de ocorrencia
# dos caracteres contidos na lista de strings
# charset na string string
def count_occourences(charset: list[str], string: str) -> int:
    counter = 0
    for char in string:
        if char in charset:
            counter = counter + 1
    return counter

s_input = input("digite a sua entrada > ")
num_occourences = count_occourences(['A', 'a'], s_input)
print(f'A ou a aparecem {num_occourences} vezes na entrada')