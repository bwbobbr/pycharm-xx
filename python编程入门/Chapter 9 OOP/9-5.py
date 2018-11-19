class User():

    def __init__(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

john = User()
print("初始访问人数:%s 人"%john.login_attempts)
john.increment_login_attempts()
john.increment_login_attempts()
john.increment_login_attempts()
print("1小时之后的访问人数: %s 人"%john.login_attempts)
john.reset_login_attempts()
print("第二天凌晨的访问人数:{0}人".format(john.login_attempts))