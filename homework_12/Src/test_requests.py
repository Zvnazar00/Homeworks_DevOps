import requests

base_url = 'http://127.0.0.1:5000/students'
post_url = 'http://127.0.0.1:5000/'
results_file= 'results.txt'


def init_log_file():
    open(results_file, 'w').close()


def log_response(response):
    method = response.request.method
    url = response.url
    status = response.status_code
    try:
        json_data = response.json()
    except ValueError:
        json_data = "No JSON response"
    output = f"\nMethod: {method}\nURL: {url}\nStatus Code: {status}\nResponse: {json_data}\n"
    print(output)
    with open(results_file, 'a', encoding='utf-8') as f:
        f.write(output)


def create_student(student_data):
    response = requests.post(post_url, json=student_data)
    log_response(response)
    return response.json().get("id")


def update_student_partial(student_id, data):
    response = requests.patch(f"{base_url}/{student_id}", json=data)
    log_response(response)


def update_student_full(student_id, data):
    response = requests.put(f"{base_url}/{student_id}", json=data)
    log_response(response)


def delete_student(student_id):
    response = requests.delete(f"{base_url}/{student_id}")
    log_response(response)


def get_students():
    response = requests.get(base_url)
    log_response(response)


def get_student_by_id(student_id):
    response = requests.get(f"{base_url}/{student_id}")
    log_response(response)


def main():
    init_log_file()
    get_students()
    students = [
        {"first_name": "Nazar", "last_name": "Zven", "age": "19"},
        {"first_name": "Ivan", "last_name": "Ivanov", "age": "25"},
        {"first_name": "Test", "last_name": "Test", "age": "19"}
    ]
    created_ids = [create_student(data) for data in students]

    get_students()

    update_student_partial(created_ids[1], {"age": "23"})

    get_student_by_id(created_ids[1])

    updated_data = {"first_name": "Alise", "last_name": "test_last_name", "age": "21"}
    update_student_full(created_ids[2], updated_data)

    get_student_by_id(created_ids[2])

    get_students()

    delete_student(created_ids[0])

    get_students()


if __name__ == "__main__":
    main()
