# 汉诺塔问题
#1.每次移动一个盘子
#2.任何时候大盘子在下面,小盘子在上面
def function (n, a, b, c):
#其中n代表总共有多少的盘子
#a,b,c代表三座塔
#a表示起始塔
#b表示过度塔
#c表示目标塔
	if n == 1:
		print(a,'-->',b)
		return None
	'''if n == 2:
		print(a, '-->', b)
		print(a, '-->', c)
		print(b, '-->', c)
		return None
	'''
	#可以注释掉
	function(n-1, a, c ,b)  #将n-1个塔借由c塔从a塔移动到b塔上
	print(a, '-->', c)      #将剩余的最长杆子从a塔移动到c塔上
	function(n-1, b, a, c)  #将n-1个塔借由a塔从b塔移动到c塔上

a = 'A'
b= 'B'
c= 'C'
n = input('n的值:')
n = int (n)
function(n, a, b, c)