import numpy as np
import os
import scipy
import PIL
from scipy import ndimage
from scipy import misc
from PIL import Image



images = []
os.chdir('Pictures/images/train')
print "train"
for filename in os.listdir(os.getcwd()):
	img = Image.open(filename)
	print filename
	img = img.resize((256,256), PIL.Image.ANTIALIAS)
	img.save(filename)
os.chdir('../val')
print "val"
for filename in os.listdir(os.getcwd()):
	print filename
	img = Image.open(filename)
	img = img.resize((256,256), PIL.Image.ANTIALIAS)
	img.save(filename)