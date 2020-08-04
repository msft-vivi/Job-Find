# -*- coding:utf-8 -*-
# @Time : 2020/3/2 16:39
# @Author : Bravezhangw
# @File : config.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_db_uri(db_info):
	engine = db_info.get("ENGINE") or "sqlite"
	driver = db_info.get("DRIVER") or "sqlite"
	username = db_info.get("USERNAME") or ""
	password = db_info.get("PASSWORD") or ""
	host = db_info.get("HOST") or ""
	port = db_info.get("PORT") or ""
	database = db_info.get("DATABASE") or ""
	return "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(engine,driver,username,password,host,port,database)

class Config:
	DEBUG = False
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	JSON_AS_ASCII = False  # 解决 jsonify(request.form) 乱码问题
	SECRET_KEY =  b'9527'
	ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg','ppt','pptx','doc','docx'}
	UPLOAD_FOLDER = os.path.join(BASE_DIR,"tmp")
	MAX_CONTENT_LENGTH = 8 * 1024 * 1024 # 设置网络传输的最大文件大小
	# SESSION_TYPE = 'redis'
	# SESSION_COOKIE_SECURE = True
	# SESSION_USE_SIGNER = True 设置为True session无法读取数据？？



# 开发环境
class DevelopConfig(Config):
	DEBUG = True
	db_info = {
		"ENGINE":"mysql",
		"DRIVER":"pymysql",
		"HOST":"47.99.198.164",
		"PORT":"3306",
		"DATABASE":"job_find",
		"USERNAME":"root",
		"PASSWORD":"zw12345"
	}

	SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


# 测试环境
class TestConfig(Config):
	TESTING = True
	db_info = {
		"ENGINE": "mysql",
		"DRIVER": "pymysql",
		"HOST": "127.0.0.1",
		"PORT": "3306",
		"DATABASE": "job_find",
		"USERNAME": "root",
		"PASSWORD": "12345"
	}

	SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


# 演示环境
class StagingConfig(Config):
	db_info = {
		"ENGINE": "mysql",
		"DRIVER": "pymysql",
		"HOST": "127.0.0.1",
		"PORT": "3306",
		"DATABASE": "english",
		"USERNAME": "root",
		"PASSWORD": "12345"
	}

	SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


# 生产环境
class ProductConfig(Config):
	db_info = {
		"ENGINE": "mysql",
		"DRIVER": "pymysql",
		"HOST": "127.0.0.1",
		"PORT": "3306",
		"DATABASE": "english",
		"USERNAME": "root",
		"PASSWORD": "12345"
	}

	SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)



# 传入 app
envs = {
	"develop":DevelopConfig,
	"testing":TestConfig,
	"staging":StagingConfig,
	"product":ProductConfig,
	"default":DevelopConfig
}