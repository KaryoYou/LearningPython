# 字符串拼接
from xml.etree.ElementTree import tostring

from pyexpat.errors import messages

s1 = "人生苦短，" "我用：" "python"
print(s1)

s2 = "人生苦短，"
s3 = "我用："
s4 = "python"
print(s2 + s3 + s4)

#案例：
name = "jack"
age = 18
job = "IT"
hobby = "python"
messages = "大家好，我叫：" + name + "，今年：" + str(age) + "岁，职业是：" + job + "，爱好：" + hobby
print(messages) #字符串拼接
print("大家好，我叫：%s，今年：%s岁，职业是：%s，爱好：%s" %(name,age,job,hobby)) # % 占位符格式化（老写法）
print(f"大家好，我叫：{name}，今年：{age}岁，职业是：{job}，爱好：{hobby}") # f-string 格式化（Python 3.6+ 官方推荐的现代输出方式）