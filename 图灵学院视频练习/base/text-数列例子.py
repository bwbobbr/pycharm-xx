
# 斐波那契额数列
# 一列数字，第一个值是1， 第二个也是1， 从第三个开始，每一个数字的值等于前两个数字出现的值的和
# 数学公式为： f(1) = 1, f(2) = 1, f(n) = f(n-1) + f(n-2)
# 例如： 1,1，2，3,5,8,13.。。。。。。。。

# 下面求斐波那契数列函数有一定问题，比如n一开始就是负数，如何修正
# n表示求第n个数子的斐波那契数列的值
'''def fun (n):
	if n ==1:
		return 1
	if n!=1:
		fun(n-1)
n=input('输入第n个值:')
n=int(n)
z =fun(n-1)+fun(n-2)
print('值为：',z)
'''

def fun (n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	return fun(n-1)+fun(n-2)
print(fun(10))