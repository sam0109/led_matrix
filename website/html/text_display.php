<?php
	$command = escapeshellcmd('/home/sam/Documents/led_matrix/text_led.py');
	$output = shell_exec($command);
	echo $output;
	//header( 'Location: /index.php' ) ;
?>