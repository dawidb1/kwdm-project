# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:33:57 2020

@author: Dawid
"""

import os, csv, random, gc, pickle

# Import image data
data_path = 'C:\dane\BRATS-2017-data\MICCAI_BraTS_2019_Data_Training\HGG'

HGG_path_list = [study_dir.path + '\\' + study_dir.name for study_dir in os.scandir(data_path)]
for study_dir in os.scandir(data_path):
    if study_dir.is_dir():
        mask = study_dir.path + '\\' + study_dir.name + '_seg.nii.gz';
        img_t2 = study_dir.path + '\\' + study_dir.name + '_t2.nii.gz';

image_filename = 'C:\dane\BRATS-2017-data\MICCAI_BraTS_2019_Data_Training\LGG\BraTS19_2013_16_1\BraTS19_2013_16_1_t1.nii.gz'
mask_filename = 'C:\dane\BRATS-2017-data\MICCAI_BraTS_2019_Data_Training\LGG\BraTS19_2013_16_1\BraTS19_2013_16_1_seg.nii.gz'
survival_csv_path = "C:\dane\BRATS-2017-data\MICCAI_BraTS_2019_Data_Training\survival_data.csv"

import nibabel as nib
data_types = ['flair', 't1', 't1ce', 't2']

data_temp_list = []
# for i in data_types:
i = 'flair'
for study_dir in os.scandir(data_path):
    print(os.path.join(study_dir.path, study_dir.name + '_' + i + '.nii.gz'));
    img_path = os.path.join(study_dir.path, study_dir.name + '_' + i + '.nii.gz')
    img = nib.load(img_path).get_data()
    data_temp_list.append(img)
        
img = nib.load(mask)
hdr = img.header
data = img.get_fdata()

import matplotlib.pyplot as plt

plt.figure()
img2d = data[:, :, 10]
plt.imshow(img2d)
plt.show()