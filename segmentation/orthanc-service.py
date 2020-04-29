from apiservice import ApiService

ORTHANC_URL = "http://localhost/orthanc"
PATIENTS_URL = ORTHANC_URL + "/patients"
INSTANCE_URL = ORTHANC_URL + "/instances"


class OrthancService:

    def __init__(self):
        self.apiService = ApiService('demo', 'demo')

    def getPatientList(self):
        return self.apiService.get(PATIENTS_URL).json()

    def getInstanceById(self, instanceId):
        path = INSTANCE_URL + "/" + instanceId + "/file"
        return self.apiService.get(path)

    def getInstanceByStudyIdAndModality(self, studyId, modality):
        pass

    def postImage(self, image):
        headers = {'Content-Type': 'application/dicom'}
        return self.apiService.post(INSTANCE_URL, image, headers=headers)

    def tests(self):
        print("ORTHANC API ALL REQUESTS TEST")
        patientList = self.getPatientList()
        print(patientList)
        id = "8163f709-7a92e4ec-ac21e7df-b8f77b7f-83fbe251"
        image = self.getInstanceById(id)
        postImageResponse = self.postImage(image)
        print(postImageResponse)
