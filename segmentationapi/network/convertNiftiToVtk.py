# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:33:57 2020

@author: Dawid
"""

# Sample run
# 'python convertNiftiToVtk
# C:\dane\BRATS-2019-data\MICCAI_BraTS_2019_Data_Training\HGG\BraTS19_2013_5_1\BraTS19_2013_5_1_t1.nii.gz
# output.vtk'

import sys
import os
import nibabel as nib
import SimpleITK as sitk

if len(sys.argv) < 3:
    print("Not enought input arguments: 1. img_path 2. outputFileName")
    sys.exit(1)

img_path = sys.argv[1]
outputFileName = sys.argv[2]

img3d_nib = nib.load(img_path).get_fdata()
imgSitk = sitk.GetImageFromArray(img3d_nib)

sitk.WriteImage(imgSitk, 'outputs/' + outputFileName)
