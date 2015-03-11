import numpy as np
import os
import scipy
import PIL
import random
from scipy import ndimage
from scipy import misc
from PIL import Image



train_x = []
train_y = []
test_x = []
test_y = []
#images = np.zeros([469,10000])

os.chdir('Pictures')

os.chdir('chagall')

os.chdir('../kand')
print len(os.listdir(os.getcwd()))
kand_x = [];
kand_y = [];
for filename in os.listdir(os.getcwd()):
	kand_x.append("/Users/alaruba/CS231/Pictures/kand/"+filename +"\n")
	kand_y.append("0" + "\n")
random.shuffle(kand_x)
kand_train_x = kand_x[0:255]
kand_train_y = kand_y[0:255]
kand_test_x = kand_x[256:426]
kand_test_y = kand_y[256:426]
train_x.extend(kand_train_x)
test_x.extend(kand_test_x)
train_y.extend(kand_train_y)
test_y.extend(kand_test_y)

os.chdir('../klimt')
klimt_x = [];
klimt_y = [];
print len(os.listdir(os.getcwd()))
for filename in os.listdir(os.getcwd()):
	klimt_x.append("/Users/alaruba/CS231/Pictures/klimt/"+filename +"\n")
	klimt_y.append("1" + "\n")
random.shuffle(klimt_x)
klimt_train_x = klimt_x[0:84]
klimt_train_y = klimt_y[0:84]
klimt_test_x = klimt_x[85:141]
klimt_test_y = klimt_y[85:141]
train_x.extend(klimt_train_x)
test_x.extend(klimt_test_x)
train_y.extend(klimt_train_y)
test_y.extend(klimt_test_y)

os.chdir('../manet')
manet_x = [];
manet_y = [];
print len(os.listdir(os.getcwd()))
for filename in os.listdir(os.getcwd()):
	manet_x.append("/Users/alaruba/CS231/Pictures/manet/"+filename +"\n")
	manet_y.append("2" + "\n")
random.shuffle(manet_x)
manet_train_x = manet_x[0:29]
manet_train_y = manet_y[0:29]
manet_test_x = manet_x[30:50]
manet_test_y = manet_y[30:50]
train_x.extend(manet_train_x)
test_x.extend(manet_test_x)
train_y.extend(manet_train_y)
test_y.extend(manet_test_y)

os.chdir('../monet')
monet_x = [];
monet_y = [];
print len(os.listdir(os.getcwd()))
for filename in os.listdir(os.getcwd()):
	monet_x.append("/Users/alaruba/CS231/Pictures/monet/"+filename +"\n")
	monet_y.append("3" + "\n")
random.shuffle(monet_x)
monet_train_x = monet_x[0:38]
monet_train_y = monet_y[0:38]
monet_test_x = monet_x[39:65]
monet_test_y = monet_y[39:65]
train_x.extend(monet_train_x)
test_x.extend(monet_test_x)
train_y.extend(monet_train_y)
test_y.extend(monet_test_y)

os.chdir('../mond')
mond_x = [];
mond_y = [];
print len(os.listdir(os.getcwd()))
for filename in os.listdir(os.getcwd()):
	mond_x.append("/Users/alaruba/CS231/Pictures/mond/"+filename +"\n")
	mond_y.append("4" + "\n")
random.shuffle(mond_x)
mond_train_x = mond_x[0:46]
mond_train_y = mond_y[0:46]
mond_test_x = mond_x[37:78]
mond_test_y = mond_y[37:78]
train_x.extend(mond_train_x)
test_x.extend(mond_test_x)
train_y.extend(mond_train_y)
test_y.extend(mond_test_y)

os.chdir('../picasso')
picasso_x = [];
picasso_y = [];
print len(os.listdir(os.getcwd()))
for filename in os.listdir(os.getcwd()):
	picasso_x.append("/Users/alaruba/CS231/Pictures/picasso/"+filename +"\n")
	picasso_y.append("5" + "\n")
random.shuffle(picasso_x)
picasso_train_x = picasso_x[0:86]
picasso_train_y = mond_y[0:86]
picasso_test_x = mond_x[87:144]
picasso_test_y = mond_y[87:144]
train_x.extend(picasso_train_x)
test_x.extend(picasso_test_x)
train_y.extend(picasso_train_y)
test_y.extend(picasso_test_y)
f1 = open('images_train.txt', 'w')
f2 = open('val_train.txt', 'w')
f3 = open('images_test.txt', 'w')
f4 = open('val_test.txt', 'w')

for filename in train_x:
	f1.write(filename)
for filename in train_y:
	f2.write(filename)
for filename in test_x:
	f3.write(filename)
for filename in test_y:
	f4.write(filename)
f1.close()
f2.close()
f3.close()
f4.close()
