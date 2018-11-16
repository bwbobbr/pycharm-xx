# 魔法函数
class fun():
	def  __init__(self):
		print("第一次调用")

	def __call__(self):    #__call__ 当对象被当做是函数调用时触发
		print("第二次调用")

	def __str__(self):        # __str__:当对象被当做是字符串调用时触发,并且返回值内容时用return函数来返回值
		return "我是字符串..."

	def __getattr__(self, item):   # __getattr__:当访问不存在的对象时触发,注意!!此处要有两个参数
		print("我是不存在的")
		print(item)                # 此处打印的是不存在的那个对象叫什么

	def __setattr__(self, key, value):   # __setattr对成员属性进行设置时触发 key:对象叫什么,value:对象的值
		print("{0}   {1}".format(key,value))


b = fun()  # a对象的实例化
b()         # a对象调用函数时启用call函数
print(b)   # 此处a对象被当作是字符串来使用,触发了str函数
#b.addr    # name对象不存在
print(b.name)  # 比较上面的那个b.name输出时多了一个None,输出无效?无print值
print("华丽的分割线","-"*50)
b.age = 18   # 触发setattr函数