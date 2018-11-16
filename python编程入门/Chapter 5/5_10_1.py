# 用户输入名字,判断改名字是否已经存在

current_name = ["john","bob","bobbr","mackle","meimei"]
new_name = ["jushenm","MeiMei","BoB","bobbrs","jackson"]
current_name_upper = [i.upper() for i in current_name]
#
for i in new_name:
    if i.upper() in current_name_upper:
         print(i,"名字已占用")
    else:
        print(i,"可用名字")

# 这种判断的语句简单用   XXX in YYY这种是否包含的语句就好 用"=="较为的复杂