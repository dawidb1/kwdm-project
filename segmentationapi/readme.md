# About 
REST Api server for predicting existing tumors and/or its masks using model from local disc.

# Getting started:
Copy model.json and model.h5 to the workspace folder.

To run segmentation api use docker:

docker build -t segmentation-api:latest .
docker run -d -p 5000:5000 segmentation-api

# Test
using bash: curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'
using POSTMAN
using python running simple-request.py