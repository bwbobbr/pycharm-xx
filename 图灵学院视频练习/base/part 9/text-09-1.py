def fun1 (n):
	a[2] = 300
	print(n)
def fun2 (n):
	n+=9
	print(n)

a = [1,2,3,4,5,6]
print(a)
fun1(a)
print(a)  #传的是地址,而不是值
b = 1
print(b)
fun2 (b)
print(b)