<!DOCTYPE html>
<html>
<head>
	<title>登录</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
</head>
<body>
	<div class="container" style="margin:0 auto 30px; max-width:300px">
		<h1 class="page-header">Login</h1>
		<form method="post">
			<fieldset>
				<div class="control-group"><div class="controls"><input type="text" name="username" id="username" placeholder="请输入用户名"/></div></div>
				<div class="control-group"><div class="controls"><input type="password" name="passwd" id="passwd" placeholder="请输入密码"/></div></div>
			</fieldset>
			<button type="submit" class="btn btn-large btn-primary">登录</button>
		</form>
	</div>
	<script src="static/js/bootstrap.min.js"></script>
	<script src="static/js/jquery.js"></script>
</body>
</html>
