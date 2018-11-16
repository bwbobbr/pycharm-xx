x=0
def fun ():
	global x
	print(x)
	x+=1
	fun() #自己调用自己
fun()