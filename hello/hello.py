from flask import Flask,jsonify,request

app = Flask(__name__) #Flask

#127.0.0.1:5000/
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    dataDict = request.get_json()
    if "y" not in dataDict:
        return "ERROR", 305
    x = dataDict["x"]
    y = dataDict["y"]
    z = x+y
    retJSON = {
        "z": z
    }
    return jsonify(retJSON),200

@app.route('/bye')
def bye():
    #Prepare a response for the request that came to /bye
    c = 37*1
    s = str(c)
    age = s
    #c = 1/0
    #return "bye"
    retJson = {
        "Name": "Daniel Perez",
        "Age": age,
        "phones": [
            {
                "phoneName":"Home",
                "phoneNumber": "(664) 636-6792"
            },
            {
                "phoneName":"Mobile",
                "phoneNumber":"(664) 301-1076"
            }
        ]
    }
    return jsonify(retJson)

if __name__=="__main__":
    #app.run(host="127.0.0.1", port=80)
    app.run(debug=True)