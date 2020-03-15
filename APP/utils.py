# -*- coding:utf-8 -*-
# @Time : 2020/3/10 21:55
# @Author : Bravezhangw
# @File : utils.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import functools
from flask import redirect,url_for
from sqlalchemy import text

from APP.models.job_model import Job


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view

def search(category,type,workplace,search_input):
    if len(search_input.strip()) < 1:
        if category == "全部":
            if type == '不限':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
            elif type == '全职':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_type == "全职").order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_type == "全职").filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
            elif type == '实习':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_type == "实习").order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_type == "实习").filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
        else:
            if type == '不限':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_category.__eq__(category)).order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_category.__eq__(category)).filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
            elif type == '全职':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_category.__eq__(category)).filter(Job.job_type == "全职").order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_category.__eq__(category)).filter(Job.job_type == "全职").filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
            elif type == '实习':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_category.__eq__(category)).filter(Job.job_type == "实习").order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_category.__eq__(category)).filter(Job.job_type == "实习").filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
    else:
        if category == "全部":
            if type == '不限':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_name.contains(search_input)).order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
            elif type == '全职':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.job_type == "全职").order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.job_type == "全职").filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
            elif type == '实习':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.job_type == "实习").order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.job_type == "实习").filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
        else:
            if type == '不限':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.job_category.__eq__(category)).order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.job_category.__eq__(category)).filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
            elif type == '全职':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.job_category.__eq__(category)).filter(Job.job_type == "全职").order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.job_category.__eq__(category)).filter(Job.job_type == "全职").filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()
            elif type == '实习':
                if len(workplace) == 1 and workplace[0] == "不限":
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.job_category.__eq__(category)).filter(Job.job_type == "实习").order_by(text("-post_time")).all()
                else:
                    return Job.query.filter(Job.job_name.contains(search_input)).filter(Job.job_category.__eq__(category)).filter(Job.job_type == "实习").filter(Job.workplace.in_(workplace)).order_by(text("-post_time")).all()

def parse_workplace(data):
    '''
    :param data: str, eg.  '["研发","运营"]'
    :return: list , ['开发','运营']
    '''
    data = data.strip()
    data = data.replace('[','').replace(']','').replace("\"",'').split(",")
    return data