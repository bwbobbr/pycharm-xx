# seek案例---不是很清楚
with open(r"text01.txt","r") as f:
    f.seek(6,0)
    strChar = f.read()
    print(strChar)