class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("餐馆名字:" + restaurant.restaurant_name)
        print("食谱:" + restaurant.cuisine_type)

    def open_restaurant(self):
        print("正在营业")

restaurant = Restaurant("Chinese food","rice")      # 类的实例化
restaurant.describe_restaurant()        # 对象.类方法
restaurant.open_restaurant()
