import sys
from PIL import Image

newfile = open(sys.argv[2], "w+")
filename = sys.argv[1]
img = Image.open(filename)

pix = img.load()
width, height = img.size
for y in range(height):
	for x in range(width):
		r, g, b = pix[x,y]
		color = r << 16 | g << 8 | b
		if x != width - 1:
			newfile.write("0,"+str(hex(color))+" ")
		else :
			newfile.write("0,"+str(hex(color))+"\n")
newfile.close()