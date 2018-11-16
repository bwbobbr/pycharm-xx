import random
print(int(random.random() * 100))
l = list(range(0,10))
random.shuffle(l)           # 对列表进行随机的重新排序, 在原来的list里面, 不能直接print该语句
print(l)