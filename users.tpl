<!DOCTYPE html>
<html>
<head>
	<title>用户中心</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
</head>
<body>
	<div class="container">
		<h3 class="page-header">User Center</h3>
		<div>
		%if islogin:
			欢迎您：{{username}}
		%else:
			您可以<a href="/login" class="btn btn-mini">登录</a>或<a href="/reg" class="btn btn-mini">注册</a>
		%end
		</div>
	</div>
	<script src="static/js/bootstrap.min.js"></script>
	<script src="static/js/jquery.js"></script>
</body>
</html>
