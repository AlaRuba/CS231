import numpy as np
import os
import scipy
import PIL
import random
from scipy import ndimage
from scipy import misc
from PIL import Image



train = []
test = []
#images = np.zeros([469,10000])

os.chdir('Pictures')

os.chdir('chagall')

os.chdir('../kand')

path = "/Users/alaruba/CS231/Pictures/images/"
kand = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		kand.append(filename + " 0"+"\n")
print(len(kand))
random.shuffle(kand)
kand_train = []
kand_test = []
for i in range(0,255):
	kand_train.append(path + kand[i])

for i in range(256,426):
	kand_test.append(path + kand[i])

train.extend(kand_train)
test.extend(kand_test)

os.chdir('../klimt')
klimt = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		klimt.append(filename + " 1" +"\n")
print(len(klimt))
random.shuffle(klimt)
klimt_train = []
klimt_test = []
for i in range(0,80):
	klimt_train.append(path + klimt[i])
for i in range(81,135):
	klimt_test.append(path + klimt[i])

train.extend(klimt_train)
test.extend(klimt_test)

os.chdir('../manet')
manet = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		manet.append(filename + " 2" +"\n")
print(len(manet))
random.shuffle(manet)
manet_train = []
manet_test = []
for i in range(0,27):
	manet_train.append(path + manet[i])
for i in range(28,47):
	manet_test.append(path + manet[i])

train.extend(manet_train)
test.extend(manet_test)

os.chdir('../monet')
monet = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		monet.append(filename + " 3"+"\n")
print(len(monet))
random.shuffle(monet)
monet_train = []
monet_test = []
for i in range(0,37):
	monet_train.append(path + monet[i])
for i in range(28,47):
	monet_test.append(path + monet[i])
train.extend(monet_train)
test.extend(monet_test)

os.chdir('../mond')
mond = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		mond.append(filename +" 4"+"\n")
print len(mond)
random.shuffle(mond)
mond_train = []
mond_test = []
for i in range(0,46):
	mond_train.append(path + mond[i])
for i in range(37,77):
	mond_test.append(path + mond[i])

train.extend(mond_train)
test.extend(mond_test)


os.chdir('../picasso')
picasso = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		picasso.append(filename + " 5"+"\n")
print(len(picasso))
random.shuffle(picasso)
picasso_train = []
picasso_test = []
for i in range(0,84):
	picasso_train.append(path + picasso[i])
for i in range(85,143):
	picasso_test.append(path + picasso[i])

os.chdir('../../')
f1 = open('./train.txt', 'w+')
f2 = open('./test.txt', 'w+')
print os.getcwd()
for filename in train:
	f1.write(filename)
for filename in test:
	f2.write(filename)
f1.close()
f2.close()
