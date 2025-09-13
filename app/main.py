from flask import Flask, jsonify, request
from app.utils import add_task, list_tasks

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    return jsonify({"message": "Welcome to GitHub Masterclass To-Do API!"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": list_tasks(tasks)})

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "Task is required"}), 400
    task = add_task(tasks, data["task"])
    return jsonify({"task": task}), 201

if __name__ == "__main__":
    app.run(debug=True)
