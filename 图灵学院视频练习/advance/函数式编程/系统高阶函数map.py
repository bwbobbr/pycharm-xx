l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i*10)
print(l2)

def fun(n):
    return n * 10
l3 = map(fun,l1)  # l3 类型是class  map型
print(type(l3))
for i in l3:
    print(i)
l4 = [i for i in l3]  # ????
print(l4)
