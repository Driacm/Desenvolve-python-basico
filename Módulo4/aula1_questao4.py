n=int (input ("Digite um número inteiro: ")) #questao aula 4.1 questao4
maior=0
while n>0:
   x=int (input("digite um número inteiro: "))
   if x>maior:
      maior=x
      n=n-1
   else:
      n=n-1

else:
 print (maior)