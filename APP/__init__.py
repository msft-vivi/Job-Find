# -*- coding:utf-8 -*-
# @Time : 2020/3/2 16:31
# @Author : Bravezhangw
# @File : __init__.py.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from flask import Flask
from APP.config import envs
from APP.exts import init_exts
from APP.views import init_views

def create_app(env):
	app = Flask(__name__)
	app.config.from_object(envs.get(env))
	init_views(app)
	init_exts(app)

	return app