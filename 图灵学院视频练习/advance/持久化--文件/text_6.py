with open(r"text02.txt","a") as f:
    # a代表以追加的方式打开
    f.write("生活不仅有眼前的苟且,\n 还有远方的苟且")

l = ["\n","I love you","wangxiaojing"]
with open(r"text02.txt","a") as f:
    f.writelines(l)
    # 以列表的形式加入