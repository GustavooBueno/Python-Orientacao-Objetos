import random
import time

# Implementa uma função que recebe uma lista de inteiros 
lista = []
print('====================')
print('Para parar digite 0')
print('====================\n')
while True:
    numeros = int(input('Digite um numero: '))
    if numeros == 0: 
        break
    lista.append(numeros)

# Ordena essa lista utilizando o Bubble Sort
def bubble(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

# Mostra a lista ordenada através do Bubble Sort
bubble(lista)
print('\nLista ordenada através do BUBBLE SORT: ', lista) 

# Ordena essa lista utilizando o Quick Sort
def quick(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        pivo = partition(lista, inicio, fim)
        quick(lista, inicio, pivo-1)
        quick(lista, pivo+1, fim)

def partition(lista, inicio, fim):
    p = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= p:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

# Mostra a lista ordenada através do Quick Sort
quick(lista)
print('Lista ordenada através do QUICK SORT: ', lista)

# Gerando números aleatórios:
aleatorios = random.sample(range(1, 100000), 10000)

# Tempo gasto para ordenar a lista usando Quick Sort

inicio_quick = time.time()
quick(aleatorios)
fim_quick = time. time()
tempo_quick = (fim_quick - inicio_quick) * 1000

# Tempo gasto para ordenar a lista usando Bubble Sort

inicio_bubble = time.time()
bubble(aleatorios)
fim_bubble = time. time()
tempo_bubble = (fim_bubble - inicio_bubble) * 1000

# Imprimindo os resultados obtidos

print('\nTempo gasto em milisegundos pelo Bubble Sort para ordenar 10 mil números aleatórios:', tempo_bubble)
print('Tempo gasto em milisegundos pelo Quick Sort para ordenar 10 mil números aleatórios:', tempo_quick)
print('\n')