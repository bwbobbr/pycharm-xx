#成员检测检测的是关键字key里面的内容与value里面的值无关
d = {"one":1,"two":2,"three":3}
if 2 in d:
	print('value')
if "two" in d:
	print('key')
if ("two",2) in d:
	print("2")
print("-"*50)
#使用for循环,直接按key值访问
for k in d:
	print(k, d[k])
#方法二
for k in d.keys():
	print(k, d[k])
#只访问value里面的数值
for v in d.values():
	print(v)
#注意以下的特殊用法
for k, v in d.items():
	print(k, "--", v)