# coding=utf-8
__author__ = 'king'
import sys, urllib
import re
url = "http://www.163.com"
# 建立链接
conn = urllib.urlopen(url)
# 获取数据
content = conn.read()
conn.close();
# 正则匹配
c_re = re.compile(r'[0-9a-z]+\.163\.com')
data = c_re.findall(content)
# 去重
lastData = list(set(data))
# 排序
lastData.sort()
# 输出打印
for i in range(0,len(lastData)):
    print i,"-",lastData[i]