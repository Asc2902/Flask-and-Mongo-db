from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/read-data')
def read_data():
    try:
        
        with open('data.json', 'r') as file:
            data = json.load(file) 
        
        
        return jsonify({"status": "success", "data": data})
        
    except FileNotFoundError:
        return jsonify({"error": "File not found"})




if __name__ == '__main__':
    app.run(debug=True)