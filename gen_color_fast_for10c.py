# -*- coding:utf-8_*-
"""
@Time: 2019.01.01
@Author: Cambrian-Traveler
@Function: gen color according to the class value
"""
import os
import cv2
import numpy as np

#for 11c
color_map = {1: {0, 0, 255}, 2: {255, 0, 0}, 3: {0, 255, 0}, 4: {255, 255, 0}, 5: {0, 255, 255}, 6: {186, 231, 255},
             7: {255, 0, 255}, 8: {205, 90, 106}, 9: {117, 168, 211}, 10: {8, 101, 139}, 11: {236, 178, 250},
             255: {255, 255, 255}}
#for 4c
#color_map = {1: {0, 0, 255}, 2: {255, 0, 0}, 3: {0, 255, 0}, 4: {186, 231, 255}}
#for 6c
#color_map = {1: {0, 0, 255}, 2: {255, 0, 0}, 3: {0, 255, 0}, 4: {186, 231, 255}, 5: {255, 0, 255}, 6: {205, 90, 106}}
path = './annotation/'
img_list = []
for root, dirs, files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] == '.png'
            img_list.append(os.path.join(root, file))
count = 0
for imp in img_list:
    count += 1
    print(count)
    print(imp)
    newp = imp.replace('annotation/', 'mask/')
    print(newp)
    if os.path.exists(newp)
        print('newp does not exist!')
        contine
    anno = cv2.imread(imp)
    color = np.zeros(anno.shape) #anno.shape: (500, 500, 3)
    for k in color_map:
        color = color + ((anno == k) * color_map[k])
    cv2.imwrite(newp[:-4] + '.png', color)

