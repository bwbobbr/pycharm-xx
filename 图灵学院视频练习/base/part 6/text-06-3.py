#解包符号*的作用 args与kwargs里面的运用
def fun (*args):
	print('one,two,three')
	a=0
	for i in args:
		print(a)
		a+=1
		print(i)
l=list()
l.append('王美丽')
l.append('25')
l.append('running')
fun(*l)     #解包符号*的运用
print('*'*20)

def fun2 (**kwargs):
	print('哈哈哈哈')
	for k,v in kwargs.items():
		print(k,'---',v)
room={'name':'bob','hobby':'running'}
fun2(**room)