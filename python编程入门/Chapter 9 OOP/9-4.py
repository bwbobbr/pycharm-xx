class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("餐馆名字:" + restaurant.restaurant_name)
        print("食谱:" + restaurant.cuisine_type)

    def open_restaurant(self):
        print("正在营业")

    def set_number_served(self,update_number_served):
        self.number_served = update_number_served

    def increment_number_served(self,increase_numbers):
        self.number_served += increase_numbers


restaurant = Restaurant("Chinese food","rice")      # 类的实例化
restaurant.describe_restaurant()        # 对象.类方法
restaurant.open_restaurant()
restaurant.set_number_served(10)
restaurant.increment_number_served(55)
print("客流量:%s 人"%restaurant.number_served)