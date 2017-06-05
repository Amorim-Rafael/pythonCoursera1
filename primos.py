
def primos_maiores_que_10(n):

    i=2
    while i<10:
        if(n%i==0):
            return "Não é primo."
        i=i+1
    return 1

def primos_menores_que_10(n):
    if n==2 or n==3 or n==5 or n==7:
        return 1
    else:
        return "Não é primo."


def maior_primo(n):
    x=0
    while n<2:
        n=int(input("Digite o valor de n>= 2."))

    while n>1:
        if n>10:
            x=primos_maiores_que_10(n)
            if x==1:
                return n
            n=n-1
        else:
            x=primos_menores_que_10(n)
            if x==1:
                return n
            n=n-1