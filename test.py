from bottle import route, run, request, template, static_file, response, redirect
import hashlib
import mysql_class
import time

#页面引用静态文件
@route('/static/:paths#[a-z]+#/:filename')
def send_static(paths,filename):
	return static_file('/static/'+paths+'/'+filename, root='')
#首页
@route('/')
def index():
	d = dict()
	d['islogin'] = checklogin.check()
	d['username']= request.get_cookie('username')
	return template('users', d)
#登录页
@route('/login')
def hello():
	if checklogin.check()
		return template('users')
	html = template('login')
	print(time.time())
	return html

#登录动作
@route('/login', method='POST')
def post():
	#获取表单值
	uname = request.forms.get('username')
	passwd= request.forms.get('passwd')
	#生成auth
	authStr = uname+'|'+request.remote_addr
	m = hashlib.md5()
	m.update(authStr.encode('utf-8'))
	auth = m.hexdigest()
	#设置cookie
	response.set_cookie('username',uname)
	response.set_cookie('auth',auth)
	db = mysql_class.Mysql(host='localhost', username='root', password='flake', dbname='test')
	db.connect()
	sql = "replace into session (sid, lasttime) values (%s,%s)"
	db.insert_single(sql, (auth, int(time.time())))
	redirect('/')

@route('/logout')
def logout():
	pass
#检查登录
class checklogin:
	username = ''
	auth     = ''
	def check(self):
		self.username = request.get_cookie('username')
		self.auth     = request.get_cookie('auth')
		if not self.username or not self.auth:
			return False
		db = mysql_class.Mysql(host='localhost', username='root', password='flake', dbname='test')
		db.connect()
		sql = "select * from session where sid='"+auth+"'"
		if db.fetch_all(sql):
			return True
		return False
def check_login():
	username = request.get_cookie('username')
	auth     = request.get_cookie('auth')
	if not uname or not auth:
		return False
	db = mysql_class.Mysql(host='localhost', username='root', password='flake', dbname='test')
	db.connect()
	sql = "select * from session where sid='"+auth+"'"
	if db.fetch_all(sql):
		return True
	return False
	
run(host='localhost', port=8080, debug=True)
