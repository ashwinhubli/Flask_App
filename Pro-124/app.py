from flask import Flask, jsonify ,request 
app = Flask(__name__)

all_contacts = [{
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

@app.route('/add-data',methods = ["POST"])

def add_task():
    if not request.json :
        return jsonify({
            "status":"error",
            "message":"please provide the data!"
        },400)

    contact = {
    'id': all_contacts[-1]['id']+1,
    'Name': request.json['Name'],
    'Contact' : request.json.get('Contact',""),
    'done' : False
    }
    all_contacts.append(contact)

    return jsonify({
   "status": "Success",
   "message": "task added succesfully"
    })

@app.route('/get-data')

def get_task():
    return jsonify({
     "data": all_contacts        
    })
if __name__ == '__main__':
    app.run(debug = True)

     
