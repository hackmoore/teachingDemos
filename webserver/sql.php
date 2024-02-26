<!DOCTYPE html>
	<head>
		<title>SQL Injection</title>
		<style>
			input {
				width: 300px;
				height: 30px;
				font-size: 20px;
				margin: 10px;
			}
		</style>
	</head>

	<body>
		<h1>SQL Injection</h1>
		<p>SQL injection is a code injection technique, used to attack data-driven applications, in which malicious SQL statements are inserted into an entry field for execution (e.g. to dump the database contents to the attacker).</p>
		<p>For example, if you have a login form, and you use the following SQL statement to check if the user exists:</p>
		<code>SELECT * FROM users WHERE username = '$_POST['username']'</code>
		<p>And the user enters the following username:</p>
		<code>admin' OR '1'='1</code>
		<p>The SQL statement will become:</p>
		<code>SELECT * FROM users WHERE username = 'admin' OR '1'='1'</code>
		<p>Which will return all the users in the database.</p>
		<p>Try it yourself:</p>
		<form method="POST">
			<input placeholder="Username" name="username">
		</form>
		<?php
			if (count($_POST) > 0) {
				echo "The SQL statement will be: <br/>";
				echo "SELECT * FROM users WHERE username = ".$_POST['username'];
			}
		?>
	</body>
</html>
