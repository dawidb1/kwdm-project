from api_service import ApiService
from flask import jsonify
import json
from find_tool import FindToolBuilder
from find_tool import QueryToolBuilder


ORTHANC_URL = "http://localhost/orthanc"
PATIENTS_URL = ORTHANC_URL + "/patients"
INSTANCE_URL = ORTHANC_URL + "/instances"
FIND = ORTHANC_URL + "/tools/find"


class OrthancService:

    def __init__(self):
        self.apiService = ApiService('demo', 'demo')

    def getPatientList(self):
        return self.apiService.get(PATIENTS_URL)

    def getInstanceById(self, instanceId):
        path = INSTANCE_URL + "/" + instanceId + "/file"
        return self.apiService.get(path)

    def getInstanceIdByStudyIdAndModality(self, studyId, modality):
        query = QueryToolBuilder().setStudyId(
            studyId).setModality(modality).build()

        body = FindToolBuilder().setLevel("Instance").setQuery(query.toJsonable()).build()

        return self.apiService.post(FIND, body.toJson())

    def postImage(self, image):
        headers = {'Content-Type': 'application/dicom'}
        return self.apiService.post(INSTANCE_URL, image, headers)

    def tests(self):
        print("ORTHANC API ALL REQUESTS TEST")
        patientList = self.getPatientList()
        print(patientList)
        id = "8163f709-7a92e4ec-ac21e7df-b8f77b7f-83fbe251"
        image = self.getInstanceById(id)
        print(image)
        postImageResponse = self.postImage(image)
        print(postImageResponse)
        studyId = "751f0eaf-29aa-4e9c-bff5-da20e9205737"
        dicomFlair = self.getInstanceIdByStudyIdAndModality(
            studyId, "FLAIR")
        print(dicomFlair)


if __name__ == "__main__":
    print(("* OrthancService execute *"))
    orthancService = OrthancService()
