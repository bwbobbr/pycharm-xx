# tell的案例
with open(r"text01.txt","r") as f:
    strChar = f.read(3)
    pos = f.tell()
    while strChar:
        print(strChar)
        print(pos)
        strChar = f.read(3)
        pos = f.tell()
# 说明tell是以字节为单位的byte
# read是字符为单位的