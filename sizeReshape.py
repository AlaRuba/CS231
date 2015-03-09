import numpy as np
import os
import scipy
import PIL
from scipy import ndimage
from scipy import misc
from PIL import Image




groundTruth = np.zeros([469, 1])
#images = np.zeros([469,10000])
images = []
os.chdir('Pictures')
os.chdir('mond')
count = 0
for filename in os.listdir(os.getcwd()):
	img = Image.open(filename)
	print filename
	img = img.resize((600,768), PIL.Image.ANTIALIAS)
	img.save(filename)
os.chdir('../klimt')
for filename in os.listdir(os.getcwd()):
	img = Image.open(filename)
	print filename
	img = img.resize((600,768), PIL.Image.ANTIALIAS)
	img.save(filename)