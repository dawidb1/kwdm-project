# studyID as parameter
# get 4 modalities by studyID from orthanc

# save on disc in folder as niigz - example flair.nii.gz
# call my_predict from my_predict_data
# send returned dicom to orthanc
# return instanceID of dicom

from orthanc_service import OrthancService
import SimpleITK as sitk
import os


class SegmentationService:

    def __init__(self):
        self.orthancService = OrthancService()

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
        path = os.path.abspath(os.path.join(
            "to_predict_data", filename + format))
        with open(path, 'wb') as f:
            f.write(content)


if __name__ == "__main__":
    print(("* SegmentationService execute *"))
    segmentationService = SegmentationService()
    studyId = "751f0eaf-29aa-4e9c-bff5-da20e9205737"
    segmentationService.getAllModalities(studyId)
