import sys
import os
import glob
from PIL import Image

#sys arguments
#Here we are taking input
image_folder = sys.argv[1]
output_folder = sys.argv[2]


#check if new folder exist, if not then create one
if not (os.path.exists(output_folder)):
	os.makedirs(output_folder)

#Now loop through the image_folder and convert it
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
#Now save it
	img.save(f'{output_folder},{clean_name}.png','png')
