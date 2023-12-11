from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'Sample task 1.',
        'done': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'Sample task 2.',
        'done': False
    }
]

# Route to get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
