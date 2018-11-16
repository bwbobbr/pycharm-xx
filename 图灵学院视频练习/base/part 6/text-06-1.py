#关键字参数
def stu (name,age,addr):
	print('I am a student')
	print('我叫:{0},我今年:{1},我住{2}'.format(name,age,addr))
n = 'jingjing'
m = '25'
addr = 'home'
stu(n,m,addr)

def stu_ob1(name='NO name', age=0, addr='No addr'):
	print('I am a student')
	print('我叫:{0},我今年:{1},我住{2}'.format(name,age,addr))
n = 'jingjing'
m = '25'
addr = 'home'
stu_ob1(name=n,age=m,addr=addr)