s = {1,}
print(type(s))
print(id(s))
s1 = s.add(12304)
print(s)
print(id(s1))
print(id(s))
print('-'*50)
#字典dict{**:**}
s2 = {}
print(type(s2))
print(id(s2))
s2 = dict()
print(id(s2))
#字典的创建
d = {"one":1,"two":2,"three":3}
print(d)
d = dict({"one":1,"two":2,"three":3})
print(d)
d = dict(one=1,two=2, three=3)  #按照关键字来进行定义
print(d)
d = dict([("one",1),("two",2),("three",3)])
print(d)