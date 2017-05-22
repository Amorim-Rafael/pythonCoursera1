valor_str = input("digite um valor:")
valor = int(valor_str)
valor_len = len(valor_str)
resto_div = 0

while valor_len > 0:
    resto_int = valor//10
    resto_div += valor%10
    valor = resto_int
    valor_len -= 1
    print("valor:",valor)
    print("resto_div:",resto_div)

# print(valor//10)
# print(valor%10)