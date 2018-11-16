name = ["a","b","c","d","e","f"]
while len(name) > 2:
    remove_person = name.pop()
    print(remove_person,"sorry")
while len(name) > 0:
    print(name[0],"welcome")
    del name[0]
if name == []:
    print(name)