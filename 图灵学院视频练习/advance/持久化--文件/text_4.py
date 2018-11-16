# 关于读取文件的联系
# 打开文件,是哪个字符一组独处内容,然后显示在屏幕上
# 没读一次,休息一秒钟

import time
with open(r"text01.txt","r") as f:

    strChar = f.read(3)
    while strChar:
        print(strChar)
        time.sleep(1)
        strChar = f.read(3)
# 作业为什么每行不是三个字符