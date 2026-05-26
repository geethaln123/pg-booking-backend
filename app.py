from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

client = MongoClient("mongodb+srv://geethaln:Geethaln123@cluster0.idcf5jg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["pgbooking"]

collection = db["bookings"]


@app.route("/", methods=["GET"])
def home():
    return "Backend Running Successfully ✅"


@app.route("/", methods=["POST"])
def booking():

    data = request.get_json()

    collection.insert_one(data)

    return jsonify({
        "message": "Booking Added Successfully ✅",
        "data": data
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
