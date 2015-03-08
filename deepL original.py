import numpy as np
import os
import scipy
from scipy import ndimage
from scipy import misc



groundTruth = np.zeros([1, 496])
images = np.zeros([496,1382400])
os.chdir('Pictures')
os.chdir('chagall')
count = 0
for filename in os.listdir(os.getcwd()):
	image = misc.imread(filename)
	image = np.reshape(image, [1,-1])
	images[:,count] = image.astype(np.float64) / 255
	groundTruth[0,count] = 1
	count = count + 1
os.chdir('../kand')
for filename in os.listdir(os.getcwd()):
	image = misc.imread(filename)
	image = np.reshape(image, [1,-1])
	images[:,count] = image.astype(np.float64) / 255
	groundTruth[0,count] = 2
	count = count + 1
groundTruth = groundTruth.astype(int)
print count
print groundTruth.shape

from random import shuffle
trX = images
teX = images
trY = groundTruth
teY = groundTruth
print trX.shape
print teX.shape
print trY.shape
print teY.shape
import theano
from theano import tensor as T

def floatX(X):
    return np.asarray(X, dtype=theano.config.floatX)

def init_weights(shape):
    return theano.shared(floatX(np.random.randn(*shape) * 0.01))

def model(X, w):
    return T.nnet.softmax(T.dot(X, w))

X = T.fmatrix()
Y = T.fmatrix()

w = init_weights((784, 10))

py_x = model(X, w)
y_pred = T.argmax(py_x, axis=1)

cost = T.mean(T.nnet.categorical_crossentropy(py_x, Y))
gradient = T.grad(cost=cost, wrt=w)
update = [[w, w - gradient * 0.05]]

train = theano.function(inputs=[X, Y], outputs=cost, updates=update, allow_input_downcast=True)
predict = theano.function(inputs=[X], outputs=y_pred, allow_input_downcast=True)

for i in range(100):
    for start, end in zip(range(0, len(trX), 128), range(128, len(trX), 128)):
        cost = train(trX[start:end], trY[start:end])
    print i, np.mean(np.argmax(teY, axis=1) == predict(teX))