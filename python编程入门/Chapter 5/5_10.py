current_name = ["john","bob","bobbr","mackle","meimei"]
new_name = ["jushenm","MeiMei","BoB","bobbrs","jackson"]
for i in new_name:
    a = 0
    for j in current_name:
        a += 1
        if j.upper() == i.upper():
            print(i,"名字已占用,请重新输入")
            break
        elif a == 4:
             print(i,"名字未被使用")
# 改程序写的不好,修正详见5_10_1