#!/usr/bin/python

import Image
import ImageDraw
import ImageFont
import time
import sys
from rgbmatrix import Adafruit_RGBmatrix

def scroll_text(matrix, text):
	font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 31)
	(width, height) = font.getsize(text)
	txt = Image.new('RGBA', (width + 128, 32), (0, 0, 0, 0))
	draw = ImageDraw.Draw(txt)

	for n in range(width + 128):
		draw.text((0, -4), text, fill = (128, 128, 128, 0), font = font)
		matrix.SetImage(txt.im.id, 128 - n, 0)
		time.sleep(0.01)

	matrix.Clear()

if __name__ == "__main__":
	matrix = Adafruit_RGBmatrix(32, 4)
	if len(sys.argv) > 1:
		scroll_text(matrix, sys.argv[1])
	else:
		scroll_text(matrix, "Bush did 9/11 ;)")