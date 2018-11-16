import shelve
with shelve.open(r"shv.db") as shv:
    shv["one"] = 1          # 只能一个一个的写入
    shv["two"] = 2
    shv["three"] = 3

with shelve.open(r"shv.db") as shv:     # 由此可以看出需要进行两步,一步存,一步读取
    try:
        k1 = shv["three"]
        print(shv["one"])
        print(k1)
    except Exception as e:
        print("Error")