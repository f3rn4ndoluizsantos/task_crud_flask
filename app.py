from flask import Flask, request, jsonify
from models.tasks import Task

app = Flask(__name__)

tasks = [
]

task_id_control = 1

# @app.after_request
# def after_request(response):
#     print("After request: ", response.status)
#     return response

@app.route('/tasks', methods=['POST'])
def created():
    global task_id_control
    data = request.get_json()
    new_task = Task(
        id=task_id_control, title=data.get('title'), description=data.get('description')
        )
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({'message': "New task created"}), 201



@app.before_request
def before_request():
    print("Before request: ", request.url)


@app.route('/tasks', methods=['GET'])
def get_tasks():
    output = {
        'tasks': [task.to_dict() for task in tasks],
        'total_tasks': len(tasks)
    }
    return jsonify(output), 200


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = [task for task in tasks if task.id == id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify({'task': task[0].to_dict()}), 200


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):

    task = None
    t = [task for task in tasks if task.id == id]

    if len(t) == 0:
        return jsonify({'message': 'Task not found'}), 404
    else:
        task = t[0]

    new_data = request.get_json()

    task.title = new_data.get('title')
    task.description = new_data.get('description')
    task.completed = new_data.get('completed')

    # resultado = [(index, task) for index, task in enumerate(tasks) if task.id == id]
       
    # if len(resultado) == 0:
    #     return jsonify({'message': 'Task not found'}), 404
    

    # resultado[0][1].title = new_data.get('title')
    # resultado[0][1].description = new_data.get('description')
    # resultado[0][1].completed = new_data.get('completed')

    return jsonify({'message': 'Task updated'}), 202

app.run(debug=True, port=5000)