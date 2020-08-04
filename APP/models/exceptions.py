# -*- coding:utf-8 -*-
# @Time : 2020/3/20 10:10
# @Author : Bravezhangw
# @File : exceptions.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from werkzeug.exceptions import HTTPException


class MyHttpException(HTTPException):
	def __init__(self,msg=None):
		self.msg = msg

	def MyHttpException(self):
		raise (self.msg)