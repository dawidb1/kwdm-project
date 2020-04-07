import pydicom


def addTags(path, patient, modality):
    ds = pydicom.read_file(path)  # (rtplan.dcm is in the testfiles directory)

    ds[0x10, 0x10].value = patient.name
    ds[0x10, 0x20].value = patient.patientId
    ds[0x10, 0x30].value = patient.birth
    ds.StudyID = patient.studyId
    ds[0x08, 0x60].value = modality

    # print(f'Patientname: {ds[0x10, 0x10].value}, modality: {modality}')
    ds.save_as(path)
