num1 = int(input('Digite o 1º numero: '))
num2 = int(input('Digite o 2º numero: '))


def maximo(n1,n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return n1

print(maximo(num1,num2))
