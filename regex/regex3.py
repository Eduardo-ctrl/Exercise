import re

s = '''hello world
hello kitty
你好,北京'''

pattern = r'^你好'

regex = re.compile(pattern,flags = re.M)

try:
    l = regex.search(s).group()
except:
    print("没有匹配到内容")
else:
    print(l)
