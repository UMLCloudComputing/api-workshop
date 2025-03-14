from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
import json

app = Flask('api-workshop')
CORS(app)

mock_db = {
    'johncloudcomputing': {
        'email': 'john_cloud@computing.tech',
        'age': '20',
        'gpa': '3.25',
    }
}

transactions = []

@app.route('/users', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def users_interaction():
    username = request.args.get('username')
    email = request.args.get('email')
    age = request.args.get('age')
    gpa = request.args.get('gpa')

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    status_code = None
    if request.method == 'GET':
        data = {}
        if username in mock_db.keys():
            data = {
                'username': username,
                'email': mock_db[username]['email'],
                'age': mock_db[username]['age'],
                'gpa': mock_db[username]['gpa'],
            }
            status_code = 200
        else:
            status_code = 404

        transactions.append(f'GET for {username} @ {time}, Status: {status_code}')

        return app.response_class(
            response=json.dumps(data),
            status=status_code,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        if None not in [username, email, age, gpa]:
            mock_db[username] = {
                'email': email,
                'age': age,
                'gpa': gpa,
            }
            status_code = 201
        else:
            status_code = 500

        transactions.append(f'POST creating {username} @ {time}, Status: {status_code}')

        return app.response_class(status=status_code)
    elif request.method == 'PATCH':
        new_data = {
            'email': email,
            'age': age,
            'gpa': gpa,
        }
        for key in new_data.keys():
            if new_data[key] != None:
                mock_db[username][key] = new_data[key]
        status_code = 200

        transactions.append(f'PATCH on {username} @ {time}, Status: {status_code}')

        return app.response_class(status=200)
    elif request.method == 'DELETE':
        if username in mock_db.keys():
            mock_db.pop(username)
            status_code = 200
        else:
            status_code = 500

        transactions.append(f'DELETE on {username} @ {time}, Status: {status_code}')

        return app.response_class(status=status_code)
    
@app.route('/database', methods=['GET'])
def database_interaction():
    data = [{
        'username': key,
        'email': mock_db[key]['email'],
        'age': mock_db[key]['age'],
        'gpa': mock_db[key]['gpa']
    } for key in mock_db.keys()]

    transactions_copy = transactions
    transactions_copy.reverse()

    return app.response_class(
        response=json.dumps({'items': data, 'transactions': transactions_copy}),
        status=200,
        mimetype='application/json'
    )
