# studyID as parameter
# get 4 modalities by studyID from orthanc

# save on disc in folder as niigz - example flair.nii.gz
# call my_predict from my_predict_data
# send returned dicom to orthanc
# return instanceID of dicom

from orthanc_service import OrthancService


class SegmentationService:

    def __init__(self):
        self.orthancService = OrthancService()
        self.orthancService.tests()


if __name__ == "__main__":
    print(("* SegmentationService execute *"))
    segmentationService = SegmentationService()
