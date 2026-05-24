from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
client = MongoClient("mongodb+srv://geethaln:Geethaln123@cluster0.idcf5jg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["pgbooking"]

collection = db["bookings"]

bookings = []

@app.route('/')
def home():
    return "Backend Running Successfully"

@app.route('/booking', methods=['POST'])
def booking():

    data = request.json

    collection.insert_one(data)

    return jsonify({
        "message": "Booking Added Successfully",
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True)
