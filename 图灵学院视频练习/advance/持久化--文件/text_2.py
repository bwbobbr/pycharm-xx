# read作业题
with open(r"text01.txt", "r") as f:
    i = 1
    while i<=18:
        strChar = f.read(1)
# read是按字符读取文件内容(字符不是byte这是字节)
        if strChar == '\n':
            i += 1
            continue
        print(strChar)
        i += 1