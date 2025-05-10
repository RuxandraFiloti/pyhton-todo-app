# file = open("files/a.txt", 'r')
# content = file.read()
# print(content)
# file = open("files/a.txt", 'r')
# content = file.read()
# print(content)
# file = open("files/a.txt", 'r')
# content = file.read()
# print(content)

files = ["files/a.txt", "files/b.txt", "files/c.txt"]
for file in files:
    file = open(file, 'r')
    content = file.read()
    print(content)
