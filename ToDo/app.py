from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form['description']
    task = {'id': len(tasks) + 1,
            'description': task_description, 'completed': False}
    tasks.append(task)
    return jsonify({'message': 'Tarea agregada correctamente'})


@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return jsonify({'message': 'Tarea marcada como completada'})
    return jsonify({'error': 'Tarea no encontrada'}), 404


@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Tarea eliminada correctamente'})


if __name__ == '__main__':
    app.run(debug=True)
