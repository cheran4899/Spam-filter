from flask import Flask, request, jsonify
from model import models_response

app = Flask(__name__)

@app.route("/members")
def members(message = ""):
    return {"Hello": message}

@app.route("/input", methods = ["POST"], strict_slashes= False)
def get_input():
    if request.method == "POST":

        reqContent = request.get_json()
        print(reqContent)
        if models_response(reqContent['sentence']):
            ret = "It is a spam message"
        else:
            ret = "It is not a spam message"
        print(reqContent)

        return jsonify({"conversion": ret})

if __name__ == "__main__" :
    app.run(debug = True)
