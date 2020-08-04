# -*- coding:utf-8 -*-
# @Time : 2020/3/13 20:09
# @Author : Bravezhangw
# @File : job_model.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from datetime import datetime

from APP.exts import db
from APP.models import BaseModel
from APP.models.enterprise_model import Enterpriser


class Job(BaseModel):
	__tablename__= "job"
	job_publisher_id = db.Column(db.Integer,db.ForeignKey(Enterpriser.id),nullable=False)
	job_name = db.Column(db.String(128),nullable=False)
	job_category = db.Column(db.String(32),nullable=False) # eg(研发 运营)
	workplace = db.Column(db.String(64),nullable=False)
	post_time = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())
	job_type = db.Column(db.String(32),default="全职",nullable=False)
	job_desc = db.Column(db.Text)
	job_requirement = db.Column(db.Text)
	is_delete = db.Column(db.Boolean,default=False) # 招聘信息是否被删除
	# post_time = db.Column(db.String(64),nullable=False) # 先设置这样造数据方便
