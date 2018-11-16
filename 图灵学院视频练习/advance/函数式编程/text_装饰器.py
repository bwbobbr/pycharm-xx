import  time
# 装饰器---高阶函数,以函数作为参数
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())     # 实际代码的执行就是5,6行
        return f(*args,**kwargs)         # 返回传入函数,相当于运行传入函数
    return wrapper
# @的使用,此符号是python的语法糖
@printTime
def hello():        # 对 hello函数进行功能扩展,每次执行hello完打印当前时间
    print("Hello World!")
# 第一部分,简单输出
fun = hello
fun()
print(id(fun))
print(id(hello))
print(fun.__name__)

print("-"*50)

def fun3():
    print("我是手动执行的")
fun3()
fun3 = printTime(fun3)
fun3()

print("-"*50)
f = printTime(fun3)   # 问题为什么输出的时候时间戳出现了俩次
f()