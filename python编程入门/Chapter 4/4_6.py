# 输出1-20里面的所有基数
list1 = [i for i in range(1,21,2)]
for i in list1:
    print(i)

print("-"*50)
# 3-30里面能被3整除的数
list2 =list()
for i in range(3,31):
    if i%3 ==0:
        list2.append(i)
for i in list2:
    print(i)

print("*"*50)
# 1-10的立方
list3 = [i**3 for i in range(1,11)]
# 这个称之为列表解析式
for i in list3:
    print(i)