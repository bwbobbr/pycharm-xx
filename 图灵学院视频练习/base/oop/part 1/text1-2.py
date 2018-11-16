class A():
	name = "bob"
	age = 18

print(A.name)
print(A.age)

print("*" * 50)

print(id(A.name))
print(id(A.age))     #同一个类之中的参数地址也是不同的

print("*" * 50)
a = A()
#查看A内所有的属性
print(A.__dict__)
print(a.__dict__)      #为空
# 对a进行里面的参数进行改变
a.name = "sam"
a.age = 200
print(a.__dict__)

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

#对比与text 1-1发现当直接赋予而不改变类里面的内容时,其地址不会发生改变,当里面的值发生改变时地址发生改变