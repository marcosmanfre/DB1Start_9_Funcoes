#Escreva um programa que execute uma função que calcule o fatorial de um número passado por parâmetro.

def factorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f

print(factorial(3))

