from flask import Flask, request

app = Flask(__name__)

@app.route("/members")
def members():
    return {"Hello": ["world1", "world2", "world3"]}

@app.route("/input", methods = ["POST"], strict_slashes= False)
def get_input():
    reqContent = request.get_json()
    print(reqContent)
    return {"test1": reqContent["data"]}

if __name__ == "__main__" :
    app.run(debug = True)
