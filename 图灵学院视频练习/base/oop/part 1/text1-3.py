class Student():
	name = "change"
	age = 18

	def say(self):
		self.name = "bob"
		self.age = 200
		print("你的名字是:{0}".format(self.name))
		print("你的年龄是:{0}",format(self.age))
#self并不是关键字，只是一个用于接受对象的普通参数，理论上可以用任何一个普通变量名代替
	def sayagain(s):
		#s.name = "sam"
		#s.age = 89
		print("你的名字是:{0}".format(s.name))
		print("你的年龄是:{0}", format(s.age))

yueyue = Student()
yueyue.age
yueyue.name
yueyue.say()    #相当于yueyue = self带入其中
yueyue.sayagain()