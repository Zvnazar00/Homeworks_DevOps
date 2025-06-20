import csv
import os

csv_file = 'students.csv'

def create_csv():
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'first_name', 'last_name', 'age'])
            writer.writeheader()

def write_csv(students):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'first_name', 'last_name', 'age'])
        writer.writeheader()
        writer.writerows(students)

def generate_new_id(students):
    return str(max([int(s['id']) for s in students], default=0) + 1)

def read_students():
    with open(csv_file, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def delete_student(student_id):
    students = read_students()
    updated_students = [s for s in students if s['id'] != student_id]
    if len(updated_students) == len(students):
        return False
    write_csv(updated_students)
    return True
