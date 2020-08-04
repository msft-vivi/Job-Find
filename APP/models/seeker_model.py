# -*- coding:utf-8 -*-
# @Time : 2020/3/10 22:14
# @Author : Bravezhangw
# @File : seeker_model.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from werkzeug.security import generate_password_hash, check_password_hash

from APP.exts import db
from APP.models import BaseModel


class Seeker(BaseModel):
    __tablename__= "seeker"
    username = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    phone = db.Column(db.String(32), unique=True)
    is_delete = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(64))
    # is_verify = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise Exception("can't access password")

    @password.setter
    def password(self, password_value):
        self._password = generate_password_hash(password_value)

    def check_password(self, password_value):
        return check_password_hash(self._password, password_value)

#     def check_permission(self, permission):
#         if not self.is_verify:
#             return False
#
#         permissions = User.query.filter_by(c_user_id=self.id)
#
#         for user_permission in permissions:
#             if permission == Permissions.query.get(user_permission.c_permission_id).p_name:
#                 return True
#
#         return False
#
#
# class Permissions(BaseModel):
#     p_name = db.Column(db.String(64), unique=True)
#
#
# class CinemaUserPermission(BaseModel):
#     c_user_id = db.Column(db.Integer, db.ForeignKey(CinemaUser.id))
#     c_permission_id = db.Column(db.Integer, db.ForeignKey(Permissions.id))
