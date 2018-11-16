d = {"one":1,"two":2,"three":3}
dd = {k:v for k,v in d.items()}
print(dd)
ddd = {k:v for k,v in d.items() if v == 2}
print(ddd)
print("*"*60)
print(str(d))          #返回字典的字符串格式
print(d.get("ada"))  #搜索字典关键字"ada",返回value没有则返回默认值是None
print(d.get("one",100)) #将返回的默认值跟改为100
print(d.get("ada",100))
l = ("1","b","c","d")
ll = dict.fromkeys(l,100)  #将某个有字符串形式的变量(list,dict,tuple都可以改变)-->变成value都为某值得dict像是
print(ll)