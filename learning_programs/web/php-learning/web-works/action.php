<!DOCTYPE html>
<html>
	<head>
		<title>my form</title>
	</head>
<body>
Здравствуйте, <?php echo htmlspecialchars($_POST['name']); ?>.
Вам <?php echo (int)$_POST['age']; ?> лет.
</body>
</html>
