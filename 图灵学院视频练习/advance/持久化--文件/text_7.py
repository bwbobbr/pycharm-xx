# 序列化案列
import pickle
age = 18
with open(r"test01.txt","wb") as f:   # 第一步是wb
    pickle.dump(age,f)
with open(r"test01.txt","rb") as f:     # 第二步是rb
    age = pickle.load(f)
    print(age)