#!/usr/bin/env python
import mysql.connector
class Mysql :
	def __init__(self,host, username, password, dbname):
		self.host=host
		self.username=username
		self.password=password
		self.database=dbname

	def connect(self):
		self.conn = mysql.connector.connect(host=self.host, user=self.username, password=self.password, database=self.database)
		self.cursor = self.conn.cursor()

	def insert_many(self, sql, li):
		self.check_conn()
		self.cursor.executemany(sql, li)
	
	def insert_single(self, sql, tup):
		self.cursor.execute(sql, tup)

	def fetch_all(self, sql):
		self.check_conn()
		self.cursor.execute(sql)
		return self.cursor.fetchall()
	def check_conn(self):
		if not self.conn:
			self.connect()