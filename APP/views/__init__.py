# -*- coding:utf-8 -*-
# @Time : 2020/3/2 16:41
# @Author : Bravezhangw
# @File : views.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from .auth import bp_auth
from APP.views.seeker.job_seeker import bp_seeker
from .enterprise.job_enterprise import bp_enterprise


def init_views(app):
	app.register_blueprint(bp_auth)
	app.register_blueprint(bp_seeker)
	app.register_blueprint(bp_enterprise)
	app.add_url_rule('/',endpoint='seeker.index')
