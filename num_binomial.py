n = int(input("Digite o numero de n: "))
k = int(input("Digite o numero de k: "))

def fatorial(n): 
    fat = 1
    while n > 0:
        fat *= n
        n -= 1    
    return fat

def numero_binomial(n, k):
    return fatorial(n) // (fatorial(k) * (fatorial(n - k)))

print(numero_binomial(n,k))    

  