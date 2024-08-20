import random

list1, list2=[],[]
for i in range (20):
    list1.append(random.randint (0,50))
    list2.append(random.randint (0,50))
    print (sorted (list1))
    print (sorted(list2))
inters=[]

for elemento in list1:
        if elemento in list2 and elemento not in inters:
            inters.append (elemento)

inters.sort()
for i in inters:
    print (f"{i}:({list1.count(i)}, {list2.count(i)})")