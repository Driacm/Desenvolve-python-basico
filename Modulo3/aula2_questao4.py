#Jogo RPG
#Entrada
pers= str (input ("Digite a classe do personagem escolhido:guerreiro, mago ou arqueiro: "))
forca= int (input("Digite os pontos de força (de 1 a 20)"))
magia= int(input("Digite os pontos de magia (de 1 a 20)"))

#processamento
a= pers="guerreiro" and forca>=15 and magia<=15
b= pers="mago" and forca<=10 and magia>=15
c= pers="arqueiro" and 5>=forca<=10 and 5<=magia>=15

#saída
pts_atr_consistentes_classe= a or b or c
print (pts_atr_consistentes_classe)