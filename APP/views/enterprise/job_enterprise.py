# -*- coding:utf-8 -*-
# @Time : 2020/3/12 20:40
# @Author : Bravezhangw
# @File : job_enterprise.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import json

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session, g
from sqlalchemy import and_, text

from APP import utils
from APP.exts import db
from APP.models.enterprise_model import Enterpriser
from APP.models.job_model import Job
from APP.models.resume import Resume

bp_enterprise = Blueprint("enterprise", __name__, url_prefix="/enterprise")


@bp_enterprise.route("/")
def index():
    return render_template("enterprise/index.html")


@bp_enterprise.route("/revise/",methods=['GET','POST'])
def revise_enterprise_info():
    if request.method == 'GET':
        enterprise = Enterpriser.query.filter(Enterpriser.id.__eq__(g.user.id)).first()
        return render_template("enterprise/revise_enterprise_info.html",enterprise=enterprise)
    elif request.method == 'POST':
        username = request.form.get("username")
        enterprise_name = request.form.get('enterprise_name')
        enterprise_phone = request.form.get('enterprise_phone')
        enterprise_email = request.form.get("enterprise_email")
        enterprise_desc = request.form.get("enterprise_desc")
        enterpriser = Enterpriser.query.filter(Enterpriser.id.__eq__(g.user.id)).first()
        enterpriser.username = username
        enterpriser.enterprise_name = enterprise_name
        enterpriser.phone = enterprise_phone
        enterpriser.email = enterprise_email
        enterpriser.enterprise_desc = enterprise_desc
        db.session.add(enterpriser)
        db.session.commit()
        return redirect(url_for('enterprise.index'))

    return render_template("enterprise/revise_enterprise_info.html")


@bp_enterprise.route("/read_resume/")
def read_resume():
    per_page = request.args.get("per_page", 5, type=int)
    pagination = Resume.query.filter(Resume.e_id.__eq__(g.user.id)).order_by(text('-created')).paginate(per_page=per_page)  # 可以直接取元素
    return render_template("enterprise/read_resume.html",pagination=pagination,per_page=per_page)


@bp_enterprise.route("/resume_detail/<int:s_id>/<int:e_id>/<int:j_id>")
def resume_detail(s_id, e_id, j_id):
    # 需要 三个 id 唯一确定resume
    resume = Resume.query.filter(and_(Resume.s_id == s_id, Resume.e_id == e_id, Resume.j_id == j_id)).first()
    return render_template("enterprise/resume_detail.html", resume=resume)


@bp_enterprise.route("/download_file/<path:file_name>")
def download_resume(file_name):
    return utils.download_file(file_name)


@bp_enterprise.route("/post_job/", methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        json_data = json.loads(request.form.get("data"))
        job_name = json_data.get("job_name")
        job_category = json_data.get("job_category")
        job_type = json_data.get("job_type")
        workplace = json_data.get("workplace")
        job_desc = json_data.get("job_desc")
        job_requirement = json_data.get("job_requirement")
        if job_name and job_category and job_type and workplace and job_desc and job_requirement:
            job = Job()
            job.job_name = job_name
            job.job_category = job_category
            job.job_type = job_type
            job.workplace = workplace
            job.job_publisher_id = session.get("user_id")
            job.job_desc = job_desc
            job.job_requirement = job_requirement
            print(job_desc)
            print(job_requirement)
            if job.save():
                return jsonify({"msg":"ok"})
            else:
                return jsonify({"msg":"fail"})
    return render_template('enterprise/post_job.html')

