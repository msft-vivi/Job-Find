# -*- coding:utf-8 -*-
# @Time : 2020/3/2 22:37
# @Author : Bravezhangw
# @File : models.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from APP.exts import db

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False