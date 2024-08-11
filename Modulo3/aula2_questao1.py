#entrada de dados
id_Ju= int (input("Digite a idade de Juliana:"))
id_cris= int(input("Digite a idade de Cris:"))
#processamento
#True se ambos maiores de idade
#<exp1>Julliana > idade
#<exp2> Cris >idade
# <exp1> and <exp2>
#False em qualquer outro caso
pode_entrar=id_Ju>=18 and id_cris>=18

#saída
print (pode_entrar)
