from flask import Flask, request

app = Flask(__name__)

@app.route("/members")
def members(message = ""):
    return {"Hello": message}

@app.route("/input", methods = ["POST", "GET"], strict_slashes= False)
def get_input():
    if request.method == "POST":

        reqContent = request.get_json()
        print(reqContent)
        return {"test1": "Sample"}
        
    if request.method == "GET":

        return {"test1": "Sample2"}

if __name__ == "__main__" :
    app.run(debug = True)
