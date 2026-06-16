from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []
next_id = 1


def find_task(task_id):
    return next((t for t in tasks if t["id"] == task_id), None)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "El camp 'title' és obligatori"}), 400
    task = {"id": next_id, "title": data["title"], "done": False}
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = find_task(task_id)
    if not task:
        return jsonify({"error": "Tasca no trobada"}), 404
    data = request.get_json()
    if "title" in data:
        task["title"] = data["title"]
    if "done" in data:
        task["done"] = data["done"]
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = find_task(task_id)
    if not task:
        return jsonify({"error": "Tasca no trobada"}), 404
    tasks.remove(task)
    return jsonify({"message": "Tasca eliminada"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
