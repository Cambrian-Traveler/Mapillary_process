# -*- coding:utf-8_*-
"""
@Time: 2019.01.01
@Author: Cambrian-Traveler
@Function: delete copy move file
"""
import sys
import os
import shutil

path = './src/'
dst = './'
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
    #delete
    os.remove(imp)
    #copy
    #shutil.copy(imp, dst)
    #move
    #shutil.move(imp, dst)
    #delete dir
    #shutil.rmtree('./src/dd')

