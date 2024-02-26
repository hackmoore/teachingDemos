<?PHP
	// This is a bit of PHP code to artificially slow down the loading of the page
	// This was tailored to my M2 Macbook and may by too slow or fast for your personal machine.
	// Tailor the CYCLES as required
	$CYCLES = 30000000;
	$current = 0;

	while(true){

		$current += rand(0,$CYCLES);
		$current %= $CYCLES;

		if ($current === 0)
			break;

	}
?>
<html>
	<head>
		<title>Buy Taylor Swift Tickets Now!</title>
	</head>
	<body>
		<img src="il_1588xN.4570498307_7e1o.jpg" width="100%" />
	</body>
</html>
