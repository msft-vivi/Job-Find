# -*- coding:utf-8 -*-
# @Time : 2020/3/13 20:23
# @Author : Bravezhangw
# @File : data_process.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import random
from datetime import datetime

import pymysql


def generate_fake_data():
	job_name_category_list = []
	with open("./job_data.txt", "r", encoding='utf-8') as f:
		for line in f.readlines():
			job_name_category_list.append(line.strip().split())
	city_list = ['北京', '上海', '深圳', '南京', '武汉', '广州', '天津', '杭州', '成都', '西安']
	job_data = []
	times = 3  # 数据组数
	for i in range(times):
		for j in range(len(job_name_category_list)):
			rand_city = random.randrange(len(city_list))
			rand_month = random.randrange(1, 4)
			rand_day = random.randrange(1, 29)
			if rand_month < 10:
				rand_month = "0%s" %(rand_month)
			if rand_day < 10:
				rand_day = "0%s" % (rand_day)
			date = "2020-%s-%s" % (rand_month, rand_day)  # 字符串

			# cur_date = datetime.strptime(date,"%Y-%m-%d") # 字符串转 datetime
			cur_city = city_list[rand_city]
			job_data.append([job_name_category_list[j][0], job_name_category_list[j][1], job_name_category_list[j][2],cur_city, date])

	with open("valid_job_data.txt", "w", encoding="utf-8") as f:
		for i in range(len(job_data)):
			f.write(" ".join(job_data[i]) + "\n")


def load_job_data():
	with open("./valid_job_data.txt","r",encoding="utf-8") as f:
		data = []
		for line in f.readlines():
			data.append(line.split())
	return data


def connect_db():
	db = pymysql.connect("localhost", "root", "12345", "job_find")
	cursor = db.cursor()
	return db,cursor

def close_db(db):
	# 关闭数据库连接
	db.close()

def insert_data(db,cursor,data=None):
	# SQL 插入语句
	# , job_publisher_id
	for i in range(len(data)):
		job_name, job_category,job_type,workplace ,post_time = data[i]
		job_publisher_id = 2
		sql = "insert into job(job_name,job_category,job_type,workplace,post_time,job_publisher_id) values ('%s','%s','%s','%s','%s',%s)" % (job_name,job_category,job_type,workplace,datetime.strptime(post_time,"%Y-%m-%d"),job_publisher_id)
		# 执行sql语句
		cursor.execute(sql)
		# 提交到数据库执行
		db.commit()
		# try:
		#
		# except:
		# 	# 如果发生错误则回滚
		# 	db.rollback()

if __name__ == '__main__':
	# 1. 制造数据
	# generate_fake_data()

	# 2.插入数据库
	db,cursor = connect_db()
	data = load_job_data()
	insert_data(db,cursor,data=data)
	close_db(db)
