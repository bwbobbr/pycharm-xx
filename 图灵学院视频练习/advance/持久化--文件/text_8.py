import pickle
l = [19, "i love", "you", "wangxiaojing",[111,222]]
with open(r"text01.txt","wb") as f:  # 相当于存入
    pickle.dump(l,f)        # 序列化
with open(r"text01.txt","rb") as f:     # 相当于取出,数据保持不变
    pickle.load(f)          # 反序列化--取出了数据
    print(l)