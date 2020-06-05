import re
import sys

menu = []
d = {}

f = open('exc.txt','r')
paragraph = str()
L =f.readlines()
L.append('\n')
for hang in L:
    if hang == '\n':
        s = re.findall(r'^\S+',paragraph)
        d[s[0]] = paragraph
        menu += s 
        paragraph = str()
    else:
        paragraph += hang
f.close()

del menu[0]
print('menu =',menu)

# for x in menu:
#     addr = re.findall(r'address is \S+',d[x])
#     for i in addr:
#         print(i[11:])

try:
    string = d[sys.argv[1]]
    addr =re.findall(r'address is \S+',string)
    for i in addr:
        print('adress =',i[11:])
except:
    print("不存在")

