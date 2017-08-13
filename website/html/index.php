<!DOCTYPE html>
	<html lang="en">
	<?php include_once('header.php'); ?>
	<body>
		<div class="container-fluid">
			<?php include_once('navbar.php'); ?>
			<div class="row">
				<form action="/text_display.php" method="post">
					<div class="input-group">
						<input type="text" class="form-control" placeholder="Enter text..." name="input_text">
						<span class="input-group-btn">
							<button class="btn btn-default" type="submit">Send</button>
						</span>
					</div>
				</form>
			</div>
		</div>
		<?php include_once('footer.php'); ?>
	</body>
</html>