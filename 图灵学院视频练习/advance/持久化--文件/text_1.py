# r 表示后面字符串内容不需要转义
with open(r"text01.txt","r") as f:

    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够读取文件直到结束
    while strline:
        print(strline)
        strline = f.readline()

print("--"*20)
with open(r"text01.txt", "r") as f:  # 重复打开
    l = list(f)
   # print(l)        # --->输出一个[] 只能读取一次
    for i in l:
        print(i)

# list能用打开的文件作为参数,把文件内每一行内容作为一个元素

# read按字符读取文件内容
print("--"*20)
with open(r"text01.txt","r") as f:
    strChar = f.read(2)                 # 表明2就输出2,默认全输出
    print(len(strChar))
    print(strChar)