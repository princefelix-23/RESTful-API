
from flask import Flask, jsonify, request, abort

# Initialize the Flask app
app = Flask(__name__)



students = [
    {"id": 1, "name": "Alice", "grade": "A", "email": "alice@email.com"},
    {"id": 2, "name": "Bob", "grade": "A", "email": "bob@email.com"},
]


@app.route('/')
def index():
    return "Welcome to Flask REST API Demo! Try accessing /students to see all students."



@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200  # 200 is the HTTP status code for 'OK'


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    # Using a list comprehension to find the student by ID
    student = next((student for student in students if student['id'] == student_id), None)
    if student is None:
        abort(404)  # If the student is not found, return a 404 error (Not Found)
    return jsonify(student), 200  # Return the student as a JSON object with a 200 status code (OK)


@app.route('/students', methods=['POST'])
def create_student():
    if not request.json or not 'name' in request.json:
        abort(400)
    
    new_student = {
        'id': students[-1]['id'] + 1 if students else 1,
        'name': request.json['name'],  # The name is provided in the POST request body\
        'grade': request.json['grade'],
        'email': request.json['email']
    }
    # Add the new student to the students list
    students.append(new_student)
    return jsonify(new_student), 201  # 201 is the HTTP status code for 'Created'

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    # Find the student by their ID

    student = next((student for student in students if student['id'] == student_id), None)
    if student is None:
        abort(404)  # If the student is not found, return a 404 error (Not Found)
    

    # If the request body is missing or not in JSON format, return a 400 error (Bad Request)
    if not request.json:
        abort(400)

    
    student['name'] = request.json.get('name', student['name'])
    student['grade'] = request.json.get('grade', student['grade'])
    student['email'] = request.json.get('email', student['email'])
    return jsonify(student), 200  # Return the updated student data with a 200 status code (OK)


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students  # Reference the global students list

    students = [student for student in students if student['id'] != student_id]
    return '', 204  # 204 is the HTTP status code for 'No Content', indicating the deletion was successful


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)