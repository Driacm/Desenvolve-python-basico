#entrada
n=int (input("Digite:  "))
soma=0 #resultado->soma
cont=0 #variável de controle do laço

#processamento
while cont<n :
    idade=int(input("Digite idade: "))
    soma += idade #soma=soma+idade

    #atualizando a avariável de controle de laço

    cont += 1 #cont=cont+1

#saída
print (f"A soma das idades é {soma}")
print (f"A média das idades é {soma/n} anos.")