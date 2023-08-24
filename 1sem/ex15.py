import math 

a = int(input("Informe o valor de a: "))

b = int(input("Informe o valor de b: "))

c = int(input("Informe o valor de c: "))

(delta) = ( b * b ) - ( 4 * a * c)

print(f"O valor de delta é: {delta} ")

x2 = (-b + math.sqrt(delta)) / (2 * a)
y1 = (-b - math.sqrt(delta)) / (2 * a)

print("fSeu valor de X é: {x2} ")
print("Seu valor de Y é: {y1}")