<!DOCTYPE html>
<html lang="en">
  <?php include_once('header.php'); ?>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/spectrum/1.8.0/spectrum.min.js"></script>
	<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/spectrum/1.8.0/spectrum.min.css">

  <body>
    <div class="container-fluid">
      <?php include_once('navbar.php'); ?>
      
      <row>
      	<input type='text' id='colorpicker' />
      </row>
    </div>

    <?php include_once('footer.php'); ?>

    <script type="text/javascript">
    	$("#colorpicker").spectrum({
  			preferredFormat: "hex",
		    flat: true,
		    showInput: true,
		    change: function(color){ 
				  $.ajax({
		        url: '/colors_display.php?input_color=' + color.toHexString(),
		        complete: function (response) {},
		        error: function () {}
			    });
				}
			});
    </script>

  </body>
</html>