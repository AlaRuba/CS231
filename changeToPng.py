import numpy as np
import os
import scipy
from scipy import ndimage
from scipy import misc
from PIL import Image

os.chdir('Pictures')
os.chdir('chagall')
count = 0
for filename in os.listdir(os.getcwd()):
	print filename
	image = Image.open(filename)
	(name, extension) = os.path.splitext(filename)
	image.save(name + '.png')

os.chdir('../kand')
print 'kand'
for filename in os.listdir(os.getcwd()):
	print filename
	image = Image.open(filename)
	(name, extension) = os.path.splitext(filename)
	image.save(name + '.png')

os.chdir('../klimt')
for filename in os.listdir(os.getcwd()):
	print filename
	image = Image.open(filename)
	(name, extension) = os.path.splitext(filename)
	image.save(name + '.png')

os.chdir('../mond')
for filename in os.listdir(os.getcwd()):
	print filename
	image = Image.open(filename)
	(name, extension) = os.path.splitext(filename)
	image.save(name + '.png')
