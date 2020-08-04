# -*- coding:utf-8 -*-
# @Time : 2020/3/17 19:58
# @Author : Bravezhangw
# @File : seeker_job_model.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from APP.exts import db

'''
	维护求职者与招聘信息直接的关系
'''
class SeekerJob(db.Model):
	__tablename__ = "seeker_job"
	s_id = db.Column(db.Integer,nullable=False)
	j_id = db.Column(db.Integer,nullable=False)