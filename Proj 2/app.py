import pandas as pd
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, jsonify

app = Flask(__name__)
mongo = PyMongo(app, uri='mongodb://localhost:27017/project2_db')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/v1.0/restaurantes')
def get_data():
    data = mongo.db.restaurantes.find_one()
    print(data)
    df = pd.DataFrame(data).to_dict(orient='record')
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)