#import package1    不能使用,只能调用内部必存在的文件__init__
#from package1 import*   同上
#import package1.module_01
stu = package1.module_01.Student("yueyue",28)
stu.speak()
#talk()
package1.module_01.talk()