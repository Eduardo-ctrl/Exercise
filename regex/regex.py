import re

pattern = r'(ab)cd(ef)'
s = 'abcdefghabcdef'

#用re模块直接调用
l = re.findall(pattern,s)
print(l)

#complile对象调用
regex = re.compile(pattern)
l = regex.findall(s)
# l = re.compile(pattern).findall(s)
print(l)
print('=============')

l = re.split(r'\s+','Hello world nihao China')
print('split():',l)

s = re.subn(r'\s+','#','Hello world nihao   China',2)
print('subn():',s)



