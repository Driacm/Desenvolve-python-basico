import random

n1=random.randint (1,10)
n2=0
n2>n1
n2<n1

while n1!=n2:
  n2=int (input("Advinhe qual é o número entre 1 a 10: "))
  if n2>n1:
   print ("É menor!")
  elif n2<n1:
   print ("É maior!") 

  else:
    print("você acertou")
    print ("fim")