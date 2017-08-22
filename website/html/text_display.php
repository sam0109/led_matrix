<?php
	$command = escapeshellcmd('sudo /home/sam/Documents/led_matrix/text_led.py ' . '"' . escapeshellarg($_POST["input_text"]) . '"');
	$output = shell_exec($command);
	header( 'Location: /index.php' ) ;
?>