number_dict = {"first_name":"bob","last_name":"Andrew",
               "age":"18","city":"HangZhou"}

for i in number_dict:
    # print(i)
    # i = str(i) 当"age":18时, 启用 18是整型
    print(i + ":"+ str(number_dict[i]))
# print(number_dict["first_name"])
print("-"*20)

for key,value in number_dict.items():
    print(key + ":" + value)
# 注意变量是什么格式的,那么输出的时候也是什么格式的
for a in sorted(number_dict):
    print(a)