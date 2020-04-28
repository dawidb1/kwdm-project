import requests
from requests.auth import HTTPBasicAuth

ORTHANC_URL = "http://localhost/orthanc"
PATIENTS_URL = ORTHANC_URL + "/patients"
INSTANCE_URL = ORTHANC_URL + "/instances"


def getPatientList():
    return requests.get(PATIENTS_URL, auth=HTTPBasicAuth('demo', 'demo')).json()


def getInstanceById(instanceId):
    path = INSTANCE_URL + "/" + instanceId + "/file"
    return requests.get(path, auth=HTTPBasicAuth('demo', 'demo'))


def postImage(image):
    headers = {'Content-Type': 'application/dicom'}
    return requests.post(INSTANCE_URL, image, headers=headers, auth=HTTPBasicAuth('demo', 'demo'))


# GET ALL MODALITIES BY STUDY_ID
if __name__ == "__main__":
    print("ORTHANC API ALL REQUESTS TEST")
    patientList = getPatientList()
    print(patientList)
    id = "8163f709-7a92e4ec-ac21e7df-b8f77b7f-83fbe251"
    image = getInstanceById(id)
    postImageResponse = postImage(image)
