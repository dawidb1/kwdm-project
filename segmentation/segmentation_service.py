# studyID as parameter
# get 4 modalities by studyID from orthanc OK

# save on disc in folder as dicom OK
# call my_predict from my_predict_data OK
# send returned dicom to orthanc OK
# return instanceID of dicom

from orthanc_service import OrthancService
import SimpleITK as sitk
import os
from Unet3DCNN.brats.my_predict_data import my_predict


class SegmentationService:

    def __init__(self):
        self.__orthancService = OrthancService()
        self.__predictionImagesDir = os.path.abspath("to_predict_data")

    def makePrediction(self, studyId):
        self.__getAllModalities(studyId)
        url = self.__createPrediction()
        status = self.__sendPrediction(url)
        print(status)
        return status['ID']

    def __sendPrediction(self, image_url):
        return self.__orthancService.postImage(image_url).json()

    def __createPrediction(self):
        return my_predict(self.__predictionImagesDir, self.__predictionImagesDir)

    def __getAllModalities(self, studyId):
        modalities = ["t1", "t1ce", "flair", "t2"]
        for modality in modalities:
            response = self.__getModalityInstance(studyId, modality)
            if response.status_code == 200:
                self.__saveImage(response.content, modality)

    def __getModalityInstance(self, studyId, modality):
        instanceId = self.__orthancService.getInstanceIdByStudyIdAndModality(
            studyId, modality).json()[0]
        print(instanceId)
        return self.__orthancService.getInstanceById(instanceId)

    def __saveImage(self, content, filename, format=".dcm"):
        path = os.path.join(self.__predictionImagesDir, filename + format)
        with open(path, 'wb') as f:
            f.write(content)


if __name__ == "__main__":
    print(("* SegmentationService execute *"))
    segmentationService = SegmentationService()
    studyId = "751f0eaf-29aa-4e9c-bff5-da20e9205737"
    predictionId = segmentationService.makePrediction(studyId)
    print(predictionId)
