from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Verifica se o arquivo de dados existe, caso contrário cria um novo
DATA_FILE = 'tasks.json'
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({"tasks": []}, f)

def read_tasks():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_tasks(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    data = read_tasks()
    return jsonify(data['tasks'])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = read_tasks()
    new_task = request.json
    
    # Adiciona campos automáticos
    new_task['id'] = len(data['tasks']) + 1
    new_task['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task['completed'] = False
    
    data['tasks'].append(new_task)
    write_tasks(data)
    
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    data = read_tasks()
    for task in data['tasks']:
        if task['id'] == task_id:
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = read_tasks()
    update_data = request.json
    
    for i, task in enumerate(data['tasks']):
        if task['id'] == task_id:
            # Mantém o ID e a data de criação original
            update_data['id'] = task_id
            update_data['created_at'] = task['created_at']
            update_data['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            data['tasks'][i] = update_data
            write_tasks(data)
            return jsonify(update_data)
            
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    data = read_tasks()
    
    for i, task in enumerate(data['tasks']):
        if task['id'] == task_id:
            deleted_task = data['tasks'].pop(i)
            write_tasks(data)
            return jsonify(deleted_task)
            
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/status/<status>', methods=['GET'])
def filter_by_status(status):
    data = read_tasks()
    status_bool = status.lower() == 'true'
    filtered_tasks = [task for task in data['tasks'] if task['completed'] == status_bool]
    return jsonify(filtered_tasks)

if __name__ == '__main__':
    app.run(debug=True)
