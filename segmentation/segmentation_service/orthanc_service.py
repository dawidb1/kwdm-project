from .api_service import ApiService
from flask import jsonify
import json
from .find_tool import FindToolBuilder
from .find_tool import QueryToolBuilder


class OrthancService:

    def __init__(self, url):
        self.apiService = ApiService('demo', 'demo')

        self.OrthancUrl = url
        self.PATIENTS_URL = self.OrthancUrl + "/patients"
        self.INSTANCE_URL = self.OrthancUrl + "/instances"
        self.FIND = self.OrthancUrl + "/tools/find"

    def getPatientList(self):
        return self.apiService.get(self.PATIENTS_URL)

    def getInstanceById(self, instanceId):
        path = self.INSTANCE_URL + "/" + instanceId + "/file"
        return self.apiService.get(path)

    def getInstanceIdByStudyIdAndModality(self, studyId, modality):
        query = QueryToolBuilder().setStudyId(
            studyId).setModality(modality).build()

        body = FindToolBuilder().setLevel("Instance").setQuery(query.toJsonable()).build()

        return self.apiService.post(self.FIND, body.toJson())

    def postImage(self, imageUrl):
        data = open(imageUrl, 'rb').read()
        # r = requests.post(your_url, data=data)

        headers = {'Content-Type': 'application/dicom'}
        return self.apiService.post(self.INSTANCE_URL, data=data, headers=headers)

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
    orthancService = OrthancService("localhost/orthanc")
