# se delta for negativo-> essa equação não possui raiz real
# se delta for 0->essa equação apresenta apenas uma raiz
# se delta for maior que 0-> essa equação possui duas raizes
import math

a = int(input("Insira o valor de a:"))
b = int(input("Insira o valor de b:"))
c = int(input("Insira o valor de c:"))

delta = (b**2)-(4*a*c)

if delta > 0:
    x1 = (-b + (math.sqrt(delta)))/2*a
    x2 = (-b - (math.sqrt(delta)))/2*a

elif delta == 0:
    x1 = (-b + (math.sqrt(delta)))/2*a
    x2 = (-b - (math.sqrt(delta)))/2*a
    
elif delta < 0:
    x1 = (-b + (math.sqrt(delta)))/2*a
    x2 = (-b - (math.sqrt(delta)))/2*a

print("x1:",int(x1))    
print("x2:",int(x2))    