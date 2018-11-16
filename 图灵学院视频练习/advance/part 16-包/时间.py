import time
print(time.daylight)  # 检测当时是否为夏令时间状态,0表示是
print(time.time())   # 表示时间戳

# localtime， 得到当前时间的时间结构
print("localtime的功能")
t = time.localtime()
print(t)   # 里面有很多东西,相当于表示函数
print(t.tm_hour)

# asctime()/ctime() 返回元组的正常字符串化之后的时间格式
print("asctime的功能")
t1 = time.asctime()
print(t1)

# sleep: 使程序进入睡眠，n秒后继续
print("sleep的功能")
for i in range(10):
    print(i)
    time.sleep(1)
# strftime:将时间元组转化为自定义的字符串格式
