import random, math
n=int (input( "Digite a quantidade de valores: "))
soma=0
for i in range(1,n):
  valor= random.randint (0,100)
  print (valor)
  soma=+ valor
print (soma)
print ("Soma da raiz quadrada é: ", math.sqrt(soma))