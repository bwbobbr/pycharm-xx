class User():

    def __init__(self,first_name,last_name,home):
        self.first_name = first_name
        self.last_name = last_name
        self.home = home

    def describe_user(self):
        print("用户的姓氏:{0}".format(self.first_name.title()))
        print("用户的名字:{0}".format(self.last_name.title()))
        print("用户的住址:{0}".format(self.home.title()))

    def greet_user(self):
        print("{0}{1}你好!".format(self.first_name.title(),self.last_name.title()))

user1 = User("jhon","bob","zhe jiang")
user1.describe_user()
user1.greet_user()