# coding=utf-8
__author__ = 'king'
import sys, urllib
import re
url = "http://www.163.com"
# ��������
conn = urllib.urlopen(url)
# ��ȡ����
content = conn.read()
conn.close();
# ����ƥ��
c_re = re.compile(r'[0-9a-z]+\.163\.com')
data = c_re.findall(content)
# ȥ��
lastData = list(set(data))
# ����
lastData.sort()
# �����ӡ
for i in range(0,len(lastData)):
    print i,"-",lastData[i]