# 使用compile对象调用正则表达式方法
# 读取一个文本，分别匹配文本中所有的
# ＊以大写字母开头的单词（包含特殊字符的不算）
# ＊数字　包括整数，小数，正数，负数分数，百分数


import re
f = open('test.txt','r')
s = f.read(1024)
f.close()
print(s)

pattern1 = r'[A-Z][^\W0-9]*'
pattern2 = r'-?\d+\.?/?\d*%?'

p = [pattern1,pattern2]
for i in p:
    regex = re.compile(i)
    l = regex.findall(s)
    print(l)



