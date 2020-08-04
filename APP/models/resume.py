# -*- coding:utf-8 -*-
# @Time : 2020/3/17 20:07
# @Author : Bravezhangw
# @File : resume.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from datetime import datetime

from APP.exts import db
from APP.models import BaseModel


class Resume(BaseModel):
	__tablename__ = "resume"
	# s_id、j_id、e_id 三个作为联合主键
	j_id = db.Column(db.Integer, nullable=False)
	s_id = db.Column(db.Integer,nullable=False)
	e_id = db.Column(db.Integer,nullable=False)
	resume_file_name = db.Column(db.String(128),unique=True)
	username = db.Column(db.String(64),nullable=False)
	phone  = db.Column(db.String(32))
	email = db.Column(db.String(64),nullable=False)
	idcard = db.Column(db.String(64),nullable=False)
	sex = db.Column(db.String(8),nullable=False)
	birthday = db.Column(db.String(64),nullable=False)
	created = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
	job_type = db.Column(db.String(32), default="全职", nullable=False)
	job_name = db.Column(db.String(128), nullable=False)
	job_category = db.Column(db.String(32), nullable=False)  # eg(研发 运营)
	workplace = db.Column(db.String(64), nullable=False)
	enterprise = db.Column(db.String(128))

	education = db.Column(db.Text)
	campus = db.Column(db.Text)
	competition = db.Column(db.Text)
	internship = db.Column(db.Text)

