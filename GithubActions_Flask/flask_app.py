from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Build a DevOps pipeline", "completed": True},
]

# Routes
@app.route('/')
def home():
    return "Welcome to the Task Manager App!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        abort(404, description="Task not found")
    return jsonify(task)

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or "title" not in request.json:
        abort(400, description="Invalid input")
    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "title": request.json["title"],
        "completed": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id < 1 or task_id > len(tasks):  # Check if task_id is valid
        return jsonify({"error": "Task not found"}), 404

    task = tasks[task_id - 1]  # Adjust for 0-based index in the list
    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["completed"] = data.get("completed", task["completed"])
    return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        abort(404, description="Task not found")
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"result": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)
