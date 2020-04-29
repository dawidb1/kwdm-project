import json


class QueryTool:

    def __init__(self, studyId, modality):
        self.studyId = studyId
        self.modality = modality

    def toJson(self):
        return json.dumps({
            'StudyID': self.studyId,
            'Modality': self.modality
        })


class QueryToolBuilder:

    def __init__(self):
        self.studyId = None
        self.modality = None

    def setStudyId(self, studyId):
        self.studyId = studyId
        return self

    def setModality(self, modality):
        self.modality = modality
        return self

    def build(self):
        return QueryTool(self.studyId, self.modality)


if __name__ == "__main__":
    query = QueryToolBuilder().setStudyId("Instance").setModality("FLAIR").build()
    print(query.toJson())
