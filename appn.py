from flask import Flask, request, render_template,  redirect, url_for
from datetime import datetime
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from bson.json_util import dumps
import json


load_dotenv()
URI=os.getenv('URI')

client = MongoClient(URI)

db = client["amar"]
collection = db["flask-tut"]



app = Flask(__name__)
    

@app.route('/login',methods =['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('index.html')

    name= request.values.get('name')
    password= request.values.get('password')
    if (not name or not password):
            return render_template('index.html', error="Missing username or password! Please try again.")
    try:
        result= {'Welcome User':name,'password':password}
        collection.insert_one(result)
        return redirect(url_for('success'))
        


    except Exception as e:
        print(f"Database insertion failed: {e}")
        return {
            "status": "error",
            "message": "An internal error occurred. Please try again later."
        }
    

@app.route('/success-page')
def success():
     return{'status':'Data submitted successfully'}
            


    
@app.route('/view')
def view():
    result=collection.find()
    print(result)
    data_list = list(result)
    clean_json_string = dumps(data_list)
    data = json.loads(clean_json_string)
    
    return {'Data retrived succssfully':data}


    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
