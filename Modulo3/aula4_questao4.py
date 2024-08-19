#entrada
#Calculo de frete

dist=int (input("Digite a distância da entrega em KM:  "))
peso=float(input("Digite o peso do pacote em Kg:  "))

#processamento

if dist <= 100 and peso<10 :
   print (f"O valor do frete é {peso*1}Reais")
if dist <= 100 and peso>=10:
   print(f"O valor do frete é {(peso*1)+10}Reais")   


if dist == (101>= dist<=300) and peso<10:
   print (f"O valor do frete é {peso*1.5}Reais")
if dist== (101>= dist<=300) and peso>=10:
   print(f"O valor do frete é {(peso*1.5)+10}Reais")

   
if dist > 300 and peso<10 :
   print (f"O valor do frete é {peso*2}Reais")
if dist > 300 and peso>=10 :
   print(f"O valor do frete é {(peso*2)+10}Reais")