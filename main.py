import numpy as np
import pandas as pd
from scipy.ndimage import imread
import canvas

params = pd.read_csv('utils/classifierLlayerReg.csv',header=None)
params = params.as_matrix().ravel()

L = 4
n = [784, 300, 200, 110, 10]

def relu(z):    #leaky relu
    return np.maximum(0.01*z,z)

def sigmoid(z):
    return 1/(1+np.exp(-z))

def forward(X, params, n, L):
    A_cache = []
    A_cache.append(X)
    idx = 0
    for i in range(1,L):
        Wi = params[idx : idx + n[i]*n[i-1]].reshape((n[i], n[i-1]))
        idx += n[i]*n[i-1]
        bi = params[idx : idx + n[i]].reshape((n[i], 1))
        idx += n[i]
        Zi = Wi.dot(A_cache[i-1]) + bi
        Ai = relu(Zi)
        A_cache.append(Ai)
    WL = params[idx : idx + n[L]*n[L-1]].reshape((n[L], n[L-1]))
    idx += n[L]*n[L-1]
    bL = params[idx : idx + n[L]].reshape((n[L], 1))
    ZL = WL.dot(A_cache[L-1]) + bL
    AL = sigmoid(ZL)
    A_cache.append(AL)

    return A_cache

ch = 'y'
while ch=='y':
    canvas.get_image()
    img = imread('utils/temp.jpg', flatten=True)
    img = img.reshape((784,1))
    img = (255.0 - img)/255.0
    A_cache = forward(img, params, n, L)
    pred = A_cache[L].argmax(axis=0)
    print "Prediction:", pred[0],'\tConfidence:',A_cache[L][pred].squeeze()*100,'%\n'
    ch = raw_input("Want to try again?([y]/n):").strip().lower()
    if ch!='y':
        print "Aborting..."
        break
