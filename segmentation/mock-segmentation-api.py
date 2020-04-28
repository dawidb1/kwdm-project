import flask
from flask import jsonify, Response
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


@app.route("/predict/<studyId>", methods=["GET"])
def predict(studyId):
    instanceId = "8163f709-7a92e4ec-ac21e7df-b8f77b7f-83fbe251"
    response = jsonify(instanceId=instanceId)
    response.status_code = 200
    return response


if __name__ == "__main__":
    print(("* Flask starting server *"))
    app.run(host='0.0.0.0')
