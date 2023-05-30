from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/members")
def members(message = ""):
    return {"Hello": message}

@app.route("/input", methods = ["POST"], strict_slashes= False)
def get_input():
    if request.method == "POST":

        reqContent = request.get_json()
        print(reqContent)
        return jsonify({"conversion": "Sample"})

if __name__ == "__main__" :
    app.run(debug = True)
