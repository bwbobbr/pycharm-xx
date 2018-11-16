#用type来造一个类

# 先定义类应该具有的成员函数:方法
def say(self):
	print("hello...")

def talk(self):
	print("TTTTTTT...")

#用type来创建一个类
A = type("Aname",(object,),{"person_say":say,"person_talk":talk})

# 然后可以像正常访问类一样使用类
a = A()
a.person_talk()
a.person_say()