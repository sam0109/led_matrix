<?php
	$command = escapeshellcmd('sudo /home/sam/Documents/led_matrix/colors_led.py ' . '"' . escapeshellarg($_POST["input_color"]) . '"');
	$output = shell_exec($command);
	header( 'Location: /index.php' ) ;
?>