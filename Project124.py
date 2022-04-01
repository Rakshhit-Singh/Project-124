from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Name': 'Raju',
        'Contact': '9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': 'Rahul',
        'Contact': '9876543222', 
        'done': False
    }
]

@app.route("/")
def abc():
    return "ABC"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please enter the data."
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"Success",
        "message":"Bingo! You did it."
    })
    
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run()