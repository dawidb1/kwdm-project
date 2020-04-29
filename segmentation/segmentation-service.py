# studyID as parameter
# get 4 modalities by studyID from orthanc OK

# save on disc in folder as dicom OK
# call my_predict from my_predict_data OK
# send returned dicom to orthanc
# return instanceID of dicom

from orthanc_service import OrthancService
import SimpleITK as sitk
import os
from Unet3DCNN.brats.my_predict_data import my_predict


class SegmentationService:

    def __init__(self):
        self.orthancService = OrthancService()
        self.predictionImagesDir = os.path.abspath("to_predict_data")

    def createPrediction(self):
        my_predict(self.predictionImagesDir, self.predictionImagesDir)

    def getAllModalities(self, studyId):
        modalities = ["t1", "t1ce", "flair", "t2"]
        for modality in modalities:
            response = self.getModalityInstance(studyId, modality)
            if response.status_code == 200:
                self.saveImage(response.content, modality)

    def getModalityInstance(self, studyId, modality):
        instanceId = self.orthancService.getInstanceIdByStudyIdAndModality(
            studyId, modality).json()[0]
        print(instanceId)
        return self.orthancService.getInstanceById(instanceId)

    def saveImage(self, content, filename, format=".dcm"):
        path = os.path.join(self.predictionImagesDir, filename + format)
        with open(path, 'wb') as f:
            f.write(content)


if __name__ == "__main__":
    print(("* SegmentationService execute *"))
    segmentationService = SegmentationService()
    studyId = "751f0eaf-29aa-4e9c-bff5-da20e9205737"
    segmentationService.getAllModalities(studyId)
    segmentationService.createPrediction()
