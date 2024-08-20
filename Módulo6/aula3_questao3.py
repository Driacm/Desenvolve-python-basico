import random

# Passo 1: Gerar uma lista com 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

# Exibir a lista original
print("Lista original:", lista)

# Passo 2: Encontrar o intervalo com a maior quantidade de números negativos
maior_qtd_negativos = 0
melhor_inicio = 0
melhor_fim = 0

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        sublista = lista[i:j]
        qtd_negativos = len([num for num in sublista if num < 0])
        if qtd_negativos > maior_qtd_negativos:
            maior_qtd_negativos = qtd_negativos
            melhor_inicio = i
            melhor_fim = j

# Passo 3: Deletar o intervalo encontrado
del lista[melhor_inicio:melhor_fim]

# Exibir a lista após a remoção do intervalo
print("Lista após remoção do intervalo:", lista)
