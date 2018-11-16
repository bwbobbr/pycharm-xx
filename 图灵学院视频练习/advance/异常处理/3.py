# 用户手动触发异常
# 自定义异常
# 需要注意的地方:  自定义异常必须是系统异常的子类
class BobValueError(ValueError):        # BobValueError是ValueError的子类
    pass
try:
    print("我爱王晓静")
    print(3.1415)
    # 手动引发一个异常
    # 注意语法: raise  ErrorClassName
    raise BobValueError
    print("还没完")      # 代码不会执行, 上一行人为出现错误
except NameError as e:
    print("NameError")
except BobValueError as e:
    print("ValueError")
    print(e)
else:                       # 刚行只是为了举例子  次.py编辑时肯定有错, 这是人为的, 改行代码不会执行
    print("无差错")
finally:
    print("我肯定会被执行")