# -*- coding:utf-8 -*-
# @Time : 2020/3/14 12:56
# @Author : Bravezhangw
# @File : test.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

import datetime
# str转时间格式：
dd = '2019-03-07'
dd = datetime.datetime.strptime(dd, "%Y-%m-%d")
print(dd) # 带时分秒
# 去除时分秒
res = datetime.datetime.strftime(dd,"%Y-%m-%d")
print(res)

