# -*- coding:utf-8 -*-
# @Time : 2020/3/10 22:52
# @Author : Bravezhangw
# @File : job_seeker.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import json
import os
import time
from datetime import datetime

from flask import Blueprint, render_template, request, jsonify, abort, redirect, current_app, flash, url_for, g
from pypinyin import lazy_pinyin
from sqlalchemy import text
from werkzeug.utils import secure_filename

from APP import utils
from APP.models.enterprise_model import Enterpriser
from APP.models.job_model import Job
from APP.models.resume import Resume
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
        enterprise = Enterpriser.query.filter(Enterpriser.id.__eq__(job.job_publisher_id)).first()
        return render_template("seeker/job_detail.html",job=job,enterprise_desc=enterprise.enterprise_desc,enterprise_name=enterprise.enterprise_name)
    except TypeError as e:
        abort(404,"job detail index need int type")

    return render_template('seeker/job_detail.html',ind=ind)

@bp_seeker.route("/job/edit/<string:ind>")
def job_edit(ind):
    try:
        ind = int(ind)
        job = Job.query.filter(Job.id.__eq__(ind)).first()
        return render_template("seeker/job_edit.html",job=job)
    except TypeError as e:
        abort(404,"job detail index need int type")

    return render_template('seeker/job_edit.html',ind=ind)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config.get("ALLOWED_EXTENSIONS")

@bp_seeker.route('/upload_file/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print("enter upload file")
        # check if the post request has the file part
        if 'file' not in request.files:
            print("file not in")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(file)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(''.join(lazy_pinyin(file.filename))) # 解决中文名字问题
            print(current_app.config['TEMP_UPLOAD_FOLDER'])
            if not os.path.exists(current_app.config['TEMP_UPLOAD_FOLDER']):
                os.makedirs(current_app.config['TEMP_UPLOAD_FOLDER'])
            file.save(os.path.join(current_app.config['TEMP_UPLOAD_FOLDER'], filename))
            print("file upload finished")
            return redirect(request.referrer)

@bp_seeker.route("/submit_resume/",methods=['GET','POST'])
def submit_resume():
    if request.method == 'POST':
        '''
            jsonify(request.form) 返回的是Reponse，其包括header,status,response
            这种方式好像只能获取input type=text 中的 name value
        '''

        job_id = request.form.get("job_id")
        seeker_id = request.form.get("seeker_id")
        enterpriser_id = request.form.get("enterpriser_id")
        username = request.form.get("username")
        phone_type = request.form.get("phone_type")
        phone = request.form.get("phone")
        email = request.form.get("email")
        idcard_type = request.form.get("idcard_type")
        idcard = request.form.get("idcard")
        birthday = request.form.get("birthday")
        education= request.form.get("education_desc")
        internship = request.form.get("internship_desc")
        campus = request.form.get("campus_desc")
        competition = request.form.get("competition_desc")
        sex = request.form.get("sex")
        job_category = request.form.get("job_category")
        job_name = request.form.get("job_name")
        workplace = request.form.get("workplace")
        job_type = request.form.get("job_type")
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename

        if file and allowed_file(file.filename):
            file_name = secure_filename(''.join(lazy_pinyin(file.filename)))  # 解决中文名字问题
            # print(current_app.config['UPLOAD_FOLDER'])
            if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
                os.makedirs(current_app.config['UPLOAD_FOLDER'])
            owner = "seeker_%s" % (seeker_id)
            file_name = owner  + "_" + str(int(time.time())) + "_" +  file_name
            save_path = os.path.join(current_app.config['UPLOAD_FOLDER'],file_name)
            file.save(save_path)
        enterpriser = Enterpriser.query.filter(Enterpriser.id.__eq__(enterpriser_id)).first()
        resume = Resume(
            j_id=job_id,
            s_id=seeker_id,
            e_id=enterpriser_id,
            username=username,
            phone=phone,
            sex=sex,
            idcard=idcard,
            email=email,
            birthday=birthday,
            campus=campus,
            competition=competition,
            education=education,
            internship=internship,
            resume_file_name=file_name,
            job_category=job_category,
            job_name=job_name,
            workplace=workplace,
            enterprise=enterpriser.enterprise_name,
            job_type=job_type
        )
        if resume.save():
            return redirect(url_for('seeker.index'))
        else:
            # 失败时候提示上传失败
            return "submit resume fail"

@bp_seeker.route("/my_post/")
def my_post():
    if request.method == 'GET':
        per_page = request.args.get("per_page", 5, type=int)
        pagination = Resume.query.filter(Resume.s_id.__eq__(g.user.id)).order_by(text('-created')).paginate(per_page=per_page) # 可以直接取元素
    return render_template("seeker/my_post.html",pagination=pagination,per_page=per_page)