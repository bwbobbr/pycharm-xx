import re
print(re.match("hello","hello world").span())
print(re.match("world","hello world"))
print(re.search("world","hello world").span())