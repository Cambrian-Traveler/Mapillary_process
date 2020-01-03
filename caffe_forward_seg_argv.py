from _future_ import division
sys.path.insert(0, '/media/data1/wyq/caffe/python')
import caffe
import numpy as np
import os
import sys
from datetime import datetime
from PIL import Image
import cv2
import pickle
import string

N = string.atoi(sys.argv[1])
print('The GPU number to be used is: ' + str(N))

GPU_ID = N
caffe.set_mode_GPU()
caffe.set_device(GPU_ID)
crop_size = 288
score_layer = 'score'
save_dir = './'
test_list = '/DATA/Seg10cData_TestSet/test.txt'

net_proto = '../deploy.prototxt'
net_weights_path = '../models/'
min_iter = 1000

path_files = os.listdir(net_weights_path)
net_weights = []
for i in path_files:
    if 'caffemodel' in i:
        net_weights.append(os.path.join(net_weights_path, i))
def fast_hist(a,b,n):
    k = (a >= 0)& (a < n)
    return np.bincount(n*a[k].astype(int) + b[k], minlength=n**2).reshape(n,n)