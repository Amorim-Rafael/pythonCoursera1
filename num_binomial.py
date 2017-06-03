n = int(input("Digite o numero de n: "))
k = int(input("Digite o numero de k: "))

def calcula_fatorial(n): 
    num_fat = 1
    while n > 0:
        num_fat *= n
        n -= 1    
    return num_fat

def calcula_binomial(n, k):
    n_fat = calcula_fatorial(n)
    k_fat = calcula_fatorial(k)
    sub = (n - k)
    sub_fat = calcula_fatorial(sub)    
    num_binomial = n_fat / (k_fat * sub_fat)

    return int(num_binomial)

print(calcula_binomial(n,k))    

  