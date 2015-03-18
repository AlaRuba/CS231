import numpy as np
import os
import scipy
import PIL
from scipy import ndimage
from scipy import misc
from PIL import Image



images = []
os.chdir('Pictures/images/train')
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		print filename
		img = Image.open(filename)
		img = img.resize((256,256), PIL.Image.ANTIALIAS)
		img.save(filename)
os.chdir('../val')
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		print filename
		img = Image.open(filename)
		img = img.resize((256,256), PIL.Image.ANTIALIAS)
		img.save(filename)