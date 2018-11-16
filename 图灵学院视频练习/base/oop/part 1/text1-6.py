class Person():

	name = "liujing"
	__age = 18

p = Person()
#name是共有变量
print(p.name)
#__age是私有变量
#print(p.__age)  #强档与加密了

print(Person.__dict__)  # 解密?得到age参数的正确表达式_Person__age
print(p._Person__age)