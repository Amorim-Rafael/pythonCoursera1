meu_cartao = int(input("Digite o numero do seu cartão de credito:"))

cartao_lido = 1
encontrei_cartao_lista = False

while cartao_lido != 0 and not encontrei_cartao_lista:
    cartao_lido = int(input("Digite o numero do proximo cartão de credito:"))
    if cartao_lido == meu_cartao:
        encontrei_cartao_lista = True

if encontrei_cartao_lista:
    print("Meu cartão está lá!")
else:
    print("Não encontrei!")