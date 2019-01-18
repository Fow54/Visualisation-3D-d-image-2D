# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:28:44 2019

@author: Victor
"""

import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread("image.png")

a = np.zeros(shape=(len(img)*len(img[0]),len(img[0][0])+3))
for i in range(0,len(img)) :
    for j in range(0,len(img[0])) :
        a[i*len(img[0])+j][3:] =  img[i][j]
        a[i*len(img[0])+j][:3] =  [i,j,0]
np.savetxt('file1.txt', a )