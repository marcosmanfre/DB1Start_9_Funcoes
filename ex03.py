#Escreva um programa que execute uma função que multiplique todos os números de uma lista passada por parâmetro.

from math import prod

def multiplicaLista(list):
    print(f'A Multiplicação da lista adicionada foi {prod(list)}. ')

multiplicaLista([2, 20, 20, 30, 44, 2])

