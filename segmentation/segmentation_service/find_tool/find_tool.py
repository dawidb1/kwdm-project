import json
from .query_tool import QueryToolBuilder


class FindTool:

    def __init__(self, level, query):
        self.Level = level
        self.Query = query

    def toJson(self):
        return json.dumps({
            'Level': self.Level,
            'Query': self.Query
        })


class FindToolBuilder:

    def __init__(self):
        self.Level = None
        self.Query = None

    def setLevel(self, level):
        self.Level = level
        return self

    def setQuery(self, query):
        self.Query = query
        return self

    def build(self):
        return FindTool(self.Level, self.Query)


if __name__ == "__main__":
    query = QueryToolBuilder().setModality("FLAIR").setStudyId(
        "751f0eaf-29aa-4e9c-bff5-da20e9205737").build()
    find = FindToolBuilder().setLevel("Instance").setQuery(query.toJsonable()).build()
    print(find.toJson())
