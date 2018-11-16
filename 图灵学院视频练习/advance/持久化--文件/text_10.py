import shelve
with shelve.open(r"shv.db") as shv:
    try:
        shv["one"] = {"eins":1, "zwei":2, "drei":3}
    except Exception as e:
        print("烦死了")

with shelve.open(r"shv.db", writeback=True) as shv:     # 添加writeback=True解决办法二
    try:
        one = shv["one"]
        print(one)
        one["eins"] = 100    # 第二个验证
    except Exception as e:
        print("烦死了")

with shelve.open(r"shv.db") as shv:
    try:
        one = shv["one"]           # 解决办法一,注释掉这句
        print(one)
    except Exception as e:
        print("烦死了")