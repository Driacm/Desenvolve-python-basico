n= int(input("Digite quantidade de experimentos: ")) #quantidade de experimentos
cont=0
soma_sapo, soma_rato,soma_coelho = 0 , 0 , 0


while cont <n:
        quantia=int (input("Digite a quantidade de cobaias: ")) #quantidade de cobaias
        tipo= input("Digite o tipo de cobaia, sendo R para rato, S para sapo e C para coelho: ") #tipos de cobaias (R=rato, S=sapo , C=coelho)
        cont+=1
        if tipo=='S':
         soma_sapo+=quantia
        elif tipo=='R':
         soma_rato+=quantia
        elif tipo=='C':
         soma_coelho+=quantia

#atualização da variavel de laço


#saída
    
         print(cont,n)
         print("Total de cobaias:", soma_coelho+soma_rato+soma_sapo)
         print("Total de sapos: ", soma_sapo)
         print("Total de rato: ", soma_rato)
         print ("Total de coelho: ", soma_coelho)
         print ("Percentual de sapos:", (soma_sapo)/n, "%")
         print("Percentual de rapos: ", (soma_rato)/n, "%")
         print ("Percental de coelhos: ", (soma_coelho)/n, "%")
