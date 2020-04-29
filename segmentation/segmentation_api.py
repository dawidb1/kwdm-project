import flask
from flask import jsonify, Response
from flask_cors import CORS
from .segmentation_service import SegmentationService

app = flask.Flask(__name__)
CORS(app)


@app.route("/predict/<studyId>", methods=["GET"])
def predict(studyId):
    segmentationService = SegmentationService()
    predictionId = segmentationService.makePrediction(studyId)

    response = jsonify(instanceId=predictionId)
    response.status_code = 200
    return response


if __name__ == "__main__":
    print(("* Flask starting server *"))
    app.run(host='0.0.0.0')
