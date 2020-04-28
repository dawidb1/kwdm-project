# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:03:13 2020

@author: Dawid
"""

from keras.applications import ResNet50
# from keras.models import model_from_json

model = ResNet50(weights='imagenet')

# # save model and weights
# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")


# # load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
