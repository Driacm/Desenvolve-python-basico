#entrada de dados
#genero, idade e tempo de serviço.
genero = input("Digite seu gênero, f (feminino) e m(masculino):")
idade  = int(input("Digite sua idade:"))
tempo  = int(input("Digite seu tempo de serviço:"))

#processamento
#Aposentadoria: Para mulheres ter mais de 60 anos, para homens ter mais de 65 anos.
#B: ou ter trabalhado pelo menos 30 anos.
#C: ou ter sessenta anos e trabalho pelo menos 25 anos.

a=(genero=='f' and idade>=60) or (genero=='m' and idade>=65)
b=tempo>=30
c=idade>=60 and tempo >=25

pode_aposentar= a or b or c

#saída
print (a, b, c, pode_aposentar)