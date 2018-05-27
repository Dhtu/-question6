#!/usr/bin/env python
# Path_generation
# use UTF-8
# Python 3.6.3

import cv2

# load images which is listed in data.txt
with open('data.txt', 'r') as data:
    lines = data.readlines()
    for line in lines:
        path, datatype = line.rstrip().split(',')
        img = cv2.imread(path)
