def sum_late(*args):
	def calc_sum():
		ax=0
		for n in args:
			ax+=n
		return ax
	return calc_sum
#print('调用sum_late的结果：',sum_late(1,2,3,4))
#calc_sum=sum_late(1,2,3,4)
#print('调用cal_sum的结果：',calc_sum())
f1=sum_late(1,2,3)
f2=sum_late(1,2,3)
print('f1==f2的结果是：',f1==f2)