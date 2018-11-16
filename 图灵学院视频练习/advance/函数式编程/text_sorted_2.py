a = ["abs","Abs","asdfasdf","liuxiaojing","bob"]
str1 = sorted(a, key = str.lower)
print(str1)
str2 = sorted(a)  # ASCII码大写字母排在小写字母之前
print(str2)