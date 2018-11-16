l4= list()
print(type(l4))
l1 = [1,2,3,4,5,6,7]
l2 =l1[:]
l3=l2
print(id(l1))
print(id(l2))
print(id(l3))
l1[1]=100
print(l1)
print(l2)
l2[1]=100
print(l2)
print(l3)
