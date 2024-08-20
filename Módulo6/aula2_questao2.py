import random

elementos = []
for i in range (1):
    num_elementos= random.randint (5,20)
    print (num_elementos)

    for i in range (num_elementos):
     elementos.append (random.randint(1,10))
print (elementos)    