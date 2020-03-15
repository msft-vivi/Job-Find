# -*- coding:utf-8 -*-
# @Time : 2020/3/12 20:40
# @Author : Bravezhangw
# @File : job_enterprise.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from flask import Blueprint

bp_enterprise = Blueprint("enterprise",__name__,url_prefix="/enterprise")

@bp_enterprise.route("/")
def index():
	return "Hello enterprise"