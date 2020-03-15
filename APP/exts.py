# -*- coding:utf-8 -*-
# @Time : 2020/3/2 16:37
# @Author : Bravezhangw
# @File : exts.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import functools

from flask_session import Session

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jsglue import JSGlue
from flask import redirect, url_for, g

db = SQLAlchemy()
migrate = Migrate()
sess = Session()
jsglue = JSGlue()
def init_exts(app):
    db.init_app(app)
    migrate.init_app(app,db)
    jsglue.init_app(app)
    # sess.init_app(app)


