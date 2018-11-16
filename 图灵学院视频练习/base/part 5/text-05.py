#如果说年利率是6.7%，本例是每年翻滚，则多少年后本钱会翻倍
money=100000
i=0
while money<200000:
	i+=1
	money=money*(1+0.067)
	print('第{0}年获得的总钱:{1}'.format(i,money))
else:
	print('来钱真是慢啊')