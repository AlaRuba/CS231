import numpy
import os
import scipy
from scipy import ndimage
from scipy import misc



images = []
os.chdir('Pictures')
os.chdir('chagall')
print(os.listdir(os.getcwd()))
for filename in os.listdir(os.getcwd()):
	images.append(misc.imread(filename))
print(images[0])