#继承的使用:
class Animal(object):
	def run(self):
		print("running....")
	def __fight(self):
		print("fighting...")

class Cat(Animal):
	pass

class Dog(Animal):
	pass

class Elephant(Animal):
	def eat(self):
		print("eating....")


cat = Cat()
cat.run()
elephant = Elephant()
elephant.eat()
#xiaoming.__fight()   # 子类不能调用父类中的非公开函数
print("-"*60)
#多态的使用:不用知道类(或对象类型)的对象进行方法的调用
def run_two_times(animal):   #运行两次run()方法
	animal.run()
	animal.run()

run_two_times(Animal())

class bird(Animal):
	def run(self):
		print("Bird is flying the sky...")


run_two_times(bird())