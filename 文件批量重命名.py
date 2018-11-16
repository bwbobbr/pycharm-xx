import os
path = 'E:\\书籍\\香港大学推荐的50本经典书籍\\香港大学推荐50部经典书籍'
drop_str = '【关注微信：世界是我的表象 回复 图书分享 即可获取解压密码和更多精选图书】'
items = os.listdir(path)
os.chdir(path)
print(os.getcwd())
for name in items:
    print(name)
    new_name = ''.join(name.split(drop_str))
    os.rename(name, new_name)
print('-----------------分界线--------------------')
items = os.listdir(path)
for name in items:
    print(name)
