#entrada de dados
id_Ju= int (input("Digite a idade de Juliana:"))
id_cris= int(input("Digite a idade de Cris:"))
#processamento
#True se Juliana ou Cris forem maiores de idade
#<exp1>Juliana > idade
#<exp2> Cris >idade
# <exp1> or <exp2>
#False se Juliana e Cris forem menores de idade
pode_entrar=id_Ju>=18 or id_cris>=18

#saída
print (pode_entrar)