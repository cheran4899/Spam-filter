from flask import Flask, request, jsonify

import sys
import os
# Get the path to the data directory relative to this module
data_path = os.path.join(os.path.dirname(__file__), '..', 'spam_detection_model')

# Add the data directory to sys.path
sys.path.append(data_path)

from spam_detection_model.model import models_response

app = Flask(__name__)

@app.route("/members")
def members(message = ""):
    return {"Hello": message}

@app.route("/input", methods = ["POST"], strict_slashes= False)
def get_input():
    if request.method == "POST":

        reqContent = request.get_json()
        if models_response([reqContent]):
            ret = "It is a spam message"
        else:
            ret = "It is not a spam message"
        print(reqContent)

        return jsonify({"conversion": ret})

if __name__ == "__main__" :
    app.run(debug = True)
