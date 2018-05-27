#!/usr/bin/env python
# Path_generation
# use UTF-8
# Python 3.6.3

import cv2 as cv
import numpy as np

# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
inner_conner_num = (9, 6)
inner_conner_width = 9
inner_conner_hight = 6
# initial the vector of objectpoints
obpoint = np.zeros((9 * 6, 3), np.float32)
obpoint[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
# obpoint *= 30
objpoints = []
imgpoints = []
tempimg=cv.imread('data\left\left01.jpg')

# print(obpoint)


def loadimg(img):
    # grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    retval, corners = cv.findChessboardCorners(img, inner_conner_num)
    # corners2 = cv.cornerSubPix(grayimg, corners, (11, 11), (-1, -1), criteria)
    objpoints.append(obpoint)
    imgpoints.append(corners)


# load images which is listed in data.txt
with open('data.txt', 'r') as data:
    lines = data.readlines()
    for line in lines:
        path, datatype = line.rstrip().split(',')
        # only process the left data
        if datatype == '0':
            tempimg = cv.imread(path)
            loadimg(tempimg)
    # camera calibration
    retval, camtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, tempimg.shape[:2], None, None)
    # np.save("camera_matrix", camtx)  # Internal parameter matrix
    # np.save("distortion_cofficients", dist)  # distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
    # np.save("rotation_vectors", rvecs)  # rotation vectors
    # np.save("translation_vectors", tvecs)  # translation vectors

    # undistort
    tempimg = cv.imread('data\left\left01.jpg')
    hight,width=tempimg.shape[:2]
