# -*- coding:utf-8 -*-
# @Time : 2020/3/15 14:53
# @Author : Bravezhangw
# @File : enterprise_model.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from werkzeug.security import generate_password_hash, check_password_hash

from APP.exts import db
from APP.models import BaseModel

# Object Relationship Mapping
class Enterpriser(BaseModel):
    __tablename__= "enterpriser"
    username = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    phone = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(64))
    enterprise_name = db.Column(db.String(128))
    enterprise_desc = db.Column(db.Text)  # 提供该字段，由企业自行添加
    is_delete = db.Column(db.Boolean, default=False)

    # is_verify = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise Exception("can't access password")

    @password.setter
    def password(self, password_value):
        self._password = generate_password_hash(password_value)

    def check_password(self, password_value):
        return check_password_hash(self._password, password_value)