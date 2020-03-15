# -*- coding:utf-8 -*-
# @Time : 2020/3/10 22:52
# @Author : Bravezhangw
# @File : job_seeker.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from datetime import datetime

from flask import Blueprint, render_template, request, jsonify, abort

from APP import utils
from APP.models.job_model import Job
from APP.utils import search

bp_seeker = Blueprint("seeker",__name__,url_prefix="/seeker")

@bp_seeker.route("/index/",methods=['GET','POST'])
def index():
	if request.method == 'POST':
		job_category = request.form.get("category")
		job_type = request.form.get("type")
		workplace = utils.parse_workplace(request.form.get("workplace")) # 解析stringnify 的地址列表
		search_input = request.form.get("search_input")
		print({"job_category":job_category,"job_type":job_type,"workplace":workplace,"search_input":search_input})

		# 查询
		job_list = search(category=job_category,type=job_type,workplace=workplace,search_input=search_input)

		# 返回列表
		data_list = []
		if job_list:
			for i in range(len(job_list)):
				job = job_list[i]
				data_list.append({"job_name": job.job_name,
								  "job_category": job.job_category,
								  "workplace": job.workplace,
								  "post_time": datetime.strftime(job.post_time, "%Y-%m-%d"),
								  "job_id": job.id
								  })
		response = {"status": 200, "msg": "ok", "data": data_list}
		return jsonify(response)


	return render_template('seeker/index.html')

@bp_seeker.route("/job/detail/<string:ind>")
def job_detail(ind):
	try:
		ind = int(ind)
		job = Job.query.filter(Job.id.__eq__(ind)).first()
		return render_template("seeker/job_detail.html",job=job)
	except TypeError as e:
		abort(404,"job detail index need int type")

	return render_template('seeker/job_detail.html',ind=ind)

@bp_seeker.route("/job/edit/")
def job_edit():
	try:
		# ind = int(ind)
		# job = Job.query.filter(Job.id.__eq__(ind)).first()
		job = None
		return render_template("seeker/job_edit.html",job=job)
	except TypeError as e:
		abort(404,"job detail index need int type")

	return render_template('seeker/job_edit.html')