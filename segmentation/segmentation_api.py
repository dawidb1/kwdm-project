import flask
from flask import jsonify, Response
from flask_cors import CORS
from segmentation_service import SegmentationService
from segmentation_service import OrthancService

app = flask.Flask(__name__)
CORS(app)


@app.route("/predict/<studyId>", methods=["GET"])
def predict(studyId):
    # localOrthancService = OrthancService("http://localhost/orthanc")
    dockerOrthancService = OrthancService("http://orthanc:8042")

    segmentationService = SegmentationService(dockerOrthancService)
    predictionId = segmentationService.makePrediction(studyId)

    response = jsonify(instanceId=predictionId)
    response.status_code = 200
    return response


if __name__ == "__main__":
    print(("* Flask starting server *"))
    app.run(host='0.0.0.0', threaded=False)
