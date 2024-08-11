#idade
#Se já jogou pelo menos 3 jogos de tabuleiro (Resposta True ou false)
#quantas vezes venceu um jogo.

idade=int (input("Qual sua idade? "))
jogou= bool (input("Você já jogou pelo menos 3 jogos de tabuleiro? Se sim, digite True; Se não, digite False: "))
venceu= int (input ("Quantas vezes venceu um jogo? " ))

#Processamento:
a = 16<=idade<=18
b = jogou=True
c = venceu >=1

Apto = a and b and c

#saída
print(Apto)
