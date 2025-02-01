from flask import Flask, request, jsonify
import json

app = Flask(__name__)

EMPLOYEES = [
 { 'id': 1, 'name': 'Ashley' },
 { 'id': 2, 'name': 'Kate' },
 { 'id': 3, 'name': 'Joe' }
]

NEXT_ID = 4

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(EMPLOYEES)

@app.route('/employees', methods=['POST'])
def create_employee():
    global NEXT_ID

    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Campo 'name' é obrigatório"}), 400

    employee = {'id': NEXT_ID, 'name': data['name']}
    NEXT_ID += 1
    EMPLOYEES.append(employee)

    return jsonify(employee), 201