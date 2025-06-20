from flask import Flask, request, jsonify
from csv_utils import create_csv, write_csv, generate_new_id, read_students, delete_student

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_student():
     data = request.get_json()
     test = data.keys()
     if not data:
        return jsonify({'error': 'Invalid fields'}), 400
     students = read_students()
     new_id = generate_new_id(students)
     new_student = {'id': new_id, **data}
     students.append(new_student)
     write_csv(students)
     return jsonify(new_student), 201


@app.route('/students', methods=['GET'])
def all_sudents():
     students = read_students()
     return jsonify(students), 200

@app.route('/students/<id_or_lastname>', methods=['GET'])
def get_student(id_or_lastname):
    students = read_students()
    results = [s for s in students if s['id'] == id_or_lastname or s['last_name'] == id_or_lastname]
    if not results:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(results), 200


@app.route('/students/<id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid fields'}), 400
    students = read_students()
    updated = False
    for student in students:
        if student in students:
            if student['id'] == id:
                student.update(data)
                updated = True
                break
    if not updated:
        return jsonify({'error': 'Student not found'}), 404
    write_csv(students)
    return  jsonify(student), 200

@app.route('/students/<id>', methods=['PATCH'])
def update_student_age(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid fields'}), 400
    students = read_students()
    for student in students:
        if student in students:
            if student['id'] == id:
                student['age'] = data['age']
                write_csv(students)
                return jsonify(student), 200
    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<id>', methods=['DELETE'])
def delete_student_route(id):
    if delete_student(id):
        return jsonify({'message': 'Student deleted successfully'}), 200
    return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    create_csv()
    app.run(debug=True)