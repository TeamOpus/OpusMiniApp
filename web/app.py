import os
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB using MONGO_URI env variable
mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["OpusMusicBot"]
queue_col = db["queue"]

@app.route("/")
def index():
    return "🎵 Opus Mini App is running!"

@app.route("/group/<int:chat_id>")
def group_player(chat_id):
    return render_template("index.html", chat_id=chat_id)

@app.route("/api/queue/<int:chat_id>")
def get_queue(chat_id):
    queue = list(queue_col.find({"chat_id": chat_id}))
    for track in queue:
        track["_id"] = str(track["_id"])
    return jsonify(queue)

@app.route("/api/pop/<int:chat_id>", methods=["POST"])
def pop_queue(chat_id):
    song = queue_col.find_one({"chat_id": chat_id})
    if song:
        queue_col.delete_one({"_id": song["_id"]})
        return jsonify({
            "status": "ok",
            "file_path": song["file_path"],
            "title": song["title"]
        })
    return jsonify({"status": "empty"})
