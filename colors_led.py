import time
from rgbmatrix import Adafruit_RGBmatrix


def display_color(matrix, color, duration = 0):
	# Rows and chain length are both required parameters:
	matrix = Adafruit_RGBmatrix(32, 1)

	# Flash screen red, green, blue (packed color values)
	matrix.Fill(color)
	if(duration > 0):
		time.sleep(duration * 1000)
		matrix.Clear()

if __name__ == "__main__":
	matrix = Adafruit_RGBmatrix(32, 4)
	if len(sys.argv) > 1:
		scroll_text(matrix, sys.argv[1])
	else:
		scroll_text(matrix, "No text recieved.")