# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:33:57 2020

@author: Dawid
"""

import os
import nibabel as nib

# Import image data
data_path = 'C:\dane\BRATS-2017-data\MICCAI_BraTS_2019_Data_Training\HGG'
survival_csv_path = "C:\dane\BRATS-2017-data\MICCAI_BraTS_2019_Data_Training\survival_data.csv"

X_train = []
Y_train = []
# X_test = []
# Y_test = []
data_types = ['flair']
for i in data_types:
    for study_dir in os.scandir(data_path):
        if len(X_train) < 6:
            print(os.path.join(study_dir.path, study_dir.name + '_' + i + '.nii.gz'));
            img_path = os.path.join(study_dir.path, study_dir.name + '_' + i + '.nii.gz')
            img = nib.load(img_path).get_data()
            X_train.append(img)
        
for study_dir in os.scandir(data_path):
       if len(Y_train) < 6:
            print(os.path.join(study_dir.path, study_dir.name + '_seg.nii.gz'));
            img_path = os.path.join(study_dir.path, study_dir.name + '_seg.nii.gz')
            img = nib.load(img_path).get_data()
            Y_train.append(img)
        
X_train = X_train[0:5]
Y_train = Y_train[0:5]
        
# img = nib.load(img)
# hdr = img.header
# data = img.get_fdata()

# import matplotlib.pyplot as plt

# plt.figure()
# img2d = data[:, :, 10]
# plt.imshow(img2d)
# plt.show()