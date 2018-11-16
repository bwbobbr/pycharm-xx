movies = ['The Holy Grail','The Life of Brain','The Meaning of Life']
#自己的答案
print('{0},1975,{1},1979,{2},1983'.format(movies[0],movies[1],movies[2]))
#标准答案
movies.insert(1,1975)
movies.insert(3,1979)
movies.append(1983)
print(movies)
##insert(index,obj)



