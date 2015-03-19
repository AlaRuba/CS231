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

os.chdir('/Users/alaruba/CS231/Pictures/')
path = "/Users/alaruba/CS231napoli/Pictures/images/"


os.chdir('chagall')
chagall = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		chagall.append(filename + " 0"+"\n")
print(len(chagall))
random.shuffle(chagall)
chagall_train = []
chagall_test = []
for i in range(0,23):
	chagall_train.append(path + chagall[i])

for i in range(24,39):
	chagall_test.append(path + chagall[i])

train.extend(chagall_train)
test.extend(chagall_test)

os.chdir('../braque')
braque = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		braque.append(filename + " 1"+"\n")
print(len(braque))
random.shuffle(braque)
braque_train = []
braque_test = []
for i in range(0,13):
	braque_train.append(path + braque[i])

for i in range(14,23):
	braque_test.append(path + braque[i])

train.extend(braque_train)
test.extend(braque_test)

os.chdir('../seurat')
seurat = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		seurat.append(filename + " 2"+"\n")
print(len(seurat))
random.shuffle(seurat)
seurat_train = []
seurat_test = []
for i in range(0,145):
	seurat_train.append(path + seurat[i])

for i in range(146,243):
	seurat_test.append(path + seurat[i])

train.extend(seurat_train)
test.extend(seurat_test)



os.chdir('../gogh')

gogh = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		gogh.append(filename + " 3"+"\n")
print(len(gogh))
random.shuffle(gogh)
gogh_train = []
gogh_test = []
for i in range(0,28):
	gogh_train.append(path + gogh[i])

for i in range(29,48):
	gogh_test.append(path + gogh[i])

train.extend(gogh_train)
test.extend(gogh_test)

os.chdir('../kand')

kand = [];
for filename in os.listdir(os.getcwd()):
	if not filename.startswith('.'):
		kand.append(filename + " 4"+"\n")
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
		klimt.append(filename + " 5" +"\n")
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
		manet.append(filename + " 6" +"\n")
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
		monet.append(filename + " 7"+"\n")
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
		mond.append(filename +" 8"+"\n")
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
		picasso.append(filename + " 9"+"\n")
print(len(picasso))
random.shuffle(picasso)
picasso_train = []
picasso_test = []
for i in range(0,84):
	picasso_train.append(path + picasso[i])
for i in range(85,143):
	picasso_test.append(path + picasso[i])

train.extend(picasso_train)
test.extend(picasso_test)

os.chdir('/Users/alaruba/CS231napoli/')
f1 = open('./train.txt', 'w+')
f2 = open('./test.txt', 'w+')
print os.getcwd()
for filename in train:
	f1.write(filename)
for filename in test:
	f2.write(filename)
f1.close()
f2.close()
