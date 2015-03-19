import numpy as np
from PIL import Image
import glob
import os
import PIL as PIL

class Normalizer:
	def normalize(arr):
	    """
	    Linear normalization
	    http://en.wikipedia.org/wiki/Normalization_%28image_processing%29
	    """
	    arr = arr.astype('float')
	    # Do not touch the alpha channel
	    for i in range(3):
	        minval = arr[...,i].min()
	        maxval = arr[...,i].max()
	        if minval != maxval:
	            arr[...,i] -= minval
	            arr[...,i] *= (255.0/(maxval-minval))
	    return arr

	def demo_normalize(filename):
	    img = Image.open(filename).convert('RGBA')
	    arr=np.array(np.asarray(img).astype('float'))
	    new_img = Image.fromarray(normalize(arr).astype('uint8'),'RGBA')
	    new_img = PIL.ImageOps.autocontrast(new_image, cutoff = 0, ignore = None);
	    return new_img
