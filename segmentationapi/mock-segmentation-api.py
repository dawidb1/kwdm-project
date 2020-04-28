import flask


app = flask.Flask(__name__)


@app.route("/predict/<studyId>", methods=["GET"])
def predict(studyId):
    return {
        "instanceId": "8163f709-7a92e4ec-ac21e7df-b8f77b7f-83fbe251",
        "status": 200
    }


if __name__ == "__main__":
    print(("* Flask starting server *"))
    # app.run(host='0.0.0.0')
    app.run()  # - use when working locally
