import time
start = time.clock()
number = [i for i in range(1,1000001)]
sum = sum(number)
print(sum)
print(max(number))
print(min(number))
end = time.clock()
print("程序运行的时间:{0}s".format(end-start))