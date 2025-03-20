from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
import json

app = Flask('api-workshop')
CORS(app)

mock_db = {
    'john_cloudcomputing@student.uml.edu': {
        'name': 'John CloudComputing',
        'major': 'Computer Science',
        'year': 'Senior',
    }
}

transactions = []

@app.route('/users', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def users_interaction():
    email = request.args.get('email')
    name = request.args.get('name')
    major = request.args.get('major')
    year = request.args.get('year')

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    status_code = None
    if request.method == 'GET':
        data = {}
        if email in mock_db.keys():
            data = {
                'username': email,
                'name': mock_db[email]['name'],
                'major': mock_db[email]['major'],
                'year': mock_db[email]['year'],
            }
            status_code = 200
        else:
            status_code = 404

        transactions.append(f'GET for {email} @ {time}, Status: {status_code}')

        return app.response_class(
            response=json.dumps(data),
            status=status_code,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        if None not in [email, name, major, year]:
            mock_db[email] = {
                'name': name,
                'major': major,
                'year': year,
            }
            status_code = 201
        else:
            status_code = 500

        transactions.append(f'POST creating {email} @ {time}, Status: {status_code}')

        return app.response_class(status=status_code)
    elif request.method == 'PATCH':
        new_data = {
            'name': name,
            'major': major,
            'year': year,
        }
        for key in new_data.keys():
            if new_data[key] != None:
                mock_db[email][key] = new_data[key]
        status_code = 200

        transactions.append(f'PATCH on {email} @ {time}, Status: {status_code}')

        return app.response_class(status=200)
    elif request.method == 'DELETE':
        if email in mock_db.keys():
            mock_db.pop(email)
            status_code = 200
        else:
            status_code = 500

        transactions.append(f'DELETE on {email} @ {time}, Status: {status_code}')

        return app.response_class(status=status_code)
    
@app.route('/database', methods=['GET'])
def database_interaction():
    data = [{
        'username': key,
        'email': mock_db[key]['name'],
        'age': mock_db[key]['major'],
        'gpa': mock_db[key]['year']
    } for key in mock_db.keys()]

    transactions_copy = transactions
    transactions_copy.reverse()

    return app.response_class(
        response=json.dumps({'items': data, 'transactions': transactions_copy}),
        status=200,
        mimetype='application/json'
    )
