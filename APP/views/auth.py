# -*- coding:utf-8 -*-
# @Time : 2020/3/2 16:41
# @Author : Bravezhangw
# @File : auth.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from flask import Blueprint, make_response, abort, request, session, g, flash, redirect
from flask import render_template,url_for,Response
from werkzeug.security import generate_password_hash, check_password_hash
from APP.exts import db
from APP.models.enterprise_model import Enterpriser
from APP.models.seeker_model import Seeker

bp_auth = Blueprint("auth",__name__,url_prefix="/auth")


@bp_auth.before_app_request # 任何app的请求都触发
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    print("trigger load_logged_in_user")
    user_id = session.get("user_id")
    usertype = session.get("usertype")
    if user_id is None:
        g.user = None
    else:
        # TODO 从数据库加载这个人的信息
        if usertype == 0:
            g.user = Seeker.query.filter_by(id=user_id).first()
        else:
            g.user = Enterpriser.query.filter_by(id=user_id).first()



@bp_auth.route("/login/",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        usertype = int(request.form.get("usertype","0"))
        error = None
        if usertype == 0:
            user = Seeker.query.filter_by(username=username).first()
        elif usertype == 1:
            user = Enterpriser.query.filter_by(username=username).first()
        else: abort(404,"usertype not found")

        if user is None:
            error = "Incorrect username."
        elif not user.check_password(password):
            error = "Incorrect password."
        if error is None:
            session.clear()
            session["user_id"] = user.id
            session['usertype'] = usertype
            if usertype == 0:
                 return redirect(url_for("seeker.index"))
            else:
                return redirect(url_for("enterprise.index"))

        flash(error)
    return render_template('auth/login.html')

@bp_auth.route("/register/",methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        usertype = int(request.form['usertype'])
        print(type(usertype))
        print(usertype)
        error = None
        if not username:
            error = "Username is required."
        elif not password1:
            error = "Password is required."
        elif not password2:
            error = "Repeat password is required."
        elif not (password1 == password2):
            error = "Twice password not the same"
        else:
            if usertype == 0:
                user = Seeker.query.filter_by(username=username).first()
            else:
                user = Enterpriser.query.filter_by(username=username).first()

            if user is not None:
                error = "User {0} is already registered.".format(username)

        if error is None:
            # the name is available, store it in the database and go to
            # the login page
            if usertype == 0:
                user = Seeker(username=username,password=password1)
            else:
                enterprise_name = request.form.get('enterprise_name')
                user = Enterpriser(username=username,enterprise_name=enterprise_name,password=password1)
            if user.save(): # 成功保存到数据库
                return redirect(url_for("auth.login"))
            else:
                render_template('auth/register.html')

        flash(error)
    else:
        abort(401)
    return render_template('auth/register.html')


@bp_auth.route("/logout/")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    print("herere")
    return redirect(url_for("seeker.index"))


@bp_auth.route("/current_page_login/",methods=['GET','POST'])
def current_page_login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        job_id = request.form.get("job_id")
        error = None
        user = Seeker.query.filter_by(username=username).first()

        if user is None:
            error = "Incorrect username."
        elif not user.check_password(password):
            error = "Incorrect password."

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user.id
            session['usertype'] = 0
            return redirect(url_for("seeker.job_edit",ind=job_id))

        flash(error)
    return redirect(request.referrer) # 返回当前页面