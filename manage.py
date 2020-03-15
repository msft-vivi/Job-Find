# -*- coding:utf-8 -*-
# @Time : 2020/3/2 16:36
# @Author : Bravezhangw
# @File : manage.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import os

from flask_script import Manager
from APP import create_app
from flask_migrate import MigrateCommand

env = os.environ.get("FLASK_ENV","develop")
app = create_app(env)
manager = Manager(app)
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()
